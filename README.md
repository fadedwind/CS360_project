# Optimal Samples Selection System
# 样本最优选择系统

## 项目描述 | Project Description
一个基于 Python 的样本最优化选择系统，集成了 OR-Tools CP-SAT 算法、SQLite 数据库存储及 Tkinter GUI 界面。  
A Python-based optimal sample selection system integrating OR-Tools CP-SAT algorithm, SQLite database storage, and Tkinter GUI.

- 使用混合贪心提示与 CP-SAT 精确集覆盖算法进行最优样本组合计算。  
  Use a hybrid greedy hint + CP-SAT exact set cover algorithm to compute optimal sample combinations.

- 提供多样化 k-组生成以提高覆盖度。  
  Provides diverse k-group generation to enhance coverage.

- 支持结果持久化存储与查询。  
  Supports persistence and query of results.

## 功能亮点 | Features

1. **compute_optimized_samples**：计算满足覆盖约束的最优样本组合。  
   **compute_optimized_samples**: Computes optimal sample combinations satisfying coverage constraints.

2. **generate_diverse_k_groups**：生成多样化 k-组集合。  
   **generate_diverse_k_groups**: Generates a diverse set of k-groups.

3. **DatabaseManager**：基于 SQLite 存储与检索计算结果。  
   **DatabaseManager**: Manages storage and retrieval of results using SQLite.
   
4. **Tkinter GUI**：直观易用的图形界面，支持参数输入、进度展示和结果查看。  
   **Tkinter GUI**: Intuitive GUI supporting parameter input, progress display, and result viewing.

## 安装与依赖 | Installation & Dependencies

- Python 3.7+  
- OR-Tools：`pip install --upgrade ortools`  
- Tkinter (included in Python standard library)

## 快速开始 | Quick Start

```bash
# 克隆或下载代码库 / Clone or download the repository
cd 项目根目录 / cd to project root

# 安装 OR-Tools / Install OR-Tools
pip install --upgrade ortools

# 启动应用 / Run the application
python test.py
```

在 GUI 中设置参数 m, n, k, j, s 后点击“计算”，即可查看最优样本组合与分组结果，并支持保存与加载。

## 文件结构 | File Structure

```
vb/  
├── algorithm.py    # 算法逻辑：compute_optimized_samples, generate_diverse_k_groups  
├── database.py     # 数据库管理：DatabaseManager  
├── ui.py           # GUI 界面：OptimalSamplesSelectionSystem、ModernUI、ParameterInput  
├── test.py         # 入口文件，启动 Tkinter 应用  
└── README.md       # 项目说明文档  
```

## 贡献与反馈 | Contribution & Feedback

欢迎提交 issue 或 pull request，共同改进项目功能与用户体验。

## 许可证 | License

本项目采用 MIT 许可证，详情见 LICENSE 文件。
