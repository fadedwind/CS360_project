import itertools
import random
from ortools.sat.python import cp_model
import multiprocessing

def compute_optimized_samples(selected_samples, k, j, s, max_time=60):
    """
    Hybrid greedy hint + CP-SAT for exact set cover with upper bound.
    selected_samples: list of sample values.
    """
    samples = selected_samples
    n = len(samples)

    # Generate j-subsets and k-groups
    j_subsets = list(itertools.combinations(range(n), j))
    k_groups = list(itertools.combinations(range(n), k))

    # Compute coverage for each k-group
    group_cov = []
    for kg in k_groups:
        cov_js = [idx for idx, js in enumerate(j_subsets) if len(set(kg) & set(js)) >= s]
        group_cov.append(cov_js)

    # Filter out groups that cover nothing
    valid_idx = [i for i, covs in enumerate(group_cov) if covs]
    k_groups = [k_groups[i] for i in valid_idx]
    group_cov = [group_cov[i] for i in valid_idx]

    # Build CP-SAT model
    model = cp_model.CpModel()
    x_vars = [model.NewBoolVar(f'x{i}') for i in range(len(k_groups))]

    # Cover constraints
    for j_idx in range(len(j_subsets)):
        cov_list = [x for x, covs in zip(x_vars, group_cov) if j_idx in covs]
        if cov_list:
            model.AddBoolOr(cov_list)

    # Objective: minimize number of groups
    model.Minimize(sum(x_vars))

    # Solve
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = max_time
    solver.parameters.num_search_workers = multiprocessing.cpu_count()
    status = solver.Solve(model)

    # Extract solution
    result = []
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        for var, grp in zip(x_vars, k_groups):
            if solver.Value(var):
                result.append(tuple(samples[idx] for idx in grp))

    return result

def generate_diverse_k_groups(n, k, max_groups):
    """
    Generate a diverse set of k-groups for better coverage.
    """
    all_indices = list(range(n))
    k_groups = []

    # Initial random groups
    initial = min(max_groups // 4, 100)
    for _ in range(initial):
        k_groups.append(tuple(sorted(random.sample(all_indices, k))))

    strategies = ["core", "spaced", "clusters", "random"]
    idx = 0
    while len(k_groups) < max_groups:
        strat = strategies[idx % len(strategies)]
        idx += 1

        if strat == "core":
            core_size = min(k - 1, 3)
            core = random.sample(all_indices, core_size)
            remaining = [i for i in all_indices if i not in core]
            rest = random.sample(remaining, k - core_size)
            new_group = tuple(sorted(core + rest))
        elif strat == "spaced":
            step = max(1, n // k)
            start = random.randint(0, n - 1)
            new_group = tuple(sorted((start + i * step) % n for i in range(k)))
        elif strat == "clusters":
            center = random.randint(0, n - 1)
            window = min(n, k * 2)
            region = [(center + i) % n for i in range(-window // 2, window // 2)]
            if len(region) >= k:
                new_group = tuple(sorted(random.sample(region, k)))
            else:
                new_group = tuple(sorted(random.sample(all_indices, k)))
        else:
            new_group = tuple(sorted(random.sample(all_indices, k)))

        if new_group not in k_groups:
            k_groups.append(new_group)

    return k_groups
