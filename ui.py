import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, font
import itertools
import random
import datetime
import time
import sqlite3
import multiprocessing
from ortools.sat.python import cp_model
from database import DatabaseManager

class ModernUI(ttk.Frame):
    """Custom styling for a modern UI look"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.style = ttk.Style()
        # Configure colors
        self.bg_color = "#f5f5f7"
        self.accent_color = "#0066cc"
        self.success_color = "#34c759"
        self.warning_color = "#ff9500"
        self.error_color = "#ff3b30"
        self.text_color = "#333333"
        self.light_text = "#666666"
        # Frame
        self.style.configure("TFrame", background=self.bg_color)
        self.style.configure("TLabel", background=self.bg_color, foreground=self.text_color)
        self.style.configure("TNotebook", background=self.bg_color)
        self.style.configure("Accent.TButton", background=self.accent_color, foreground="white")
        self.style.map("Accent.TButton", background=[('active','#0055aa'),('pressed','#004488')])
        self.style.configure("Success.TButton", background=self.success_color)
        self.style.configure("Warning.TButton", background=self.warning_color)
        self.style.map("Warning.TButton", background=[('active','#e67e00'),('pressed','#cc7000')])
        # Additional styling omitted for brevity

class ParameterInput(ttk.Frame):
    """Custom widget for parameter input with label, spinbox, and range indicator"""
    def __init__(self, parent, label_text, var, from_, to_, width=10, range_var=None, tooltip_text=None):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)
        self.label = ttk.Label(self, text=label_text, font=('Helvetica', 10, 'bold'))
        self.label.grid(row=0, column=0, sticky=tk.W, padx=(0,5), pady=5)
        self.spinbox = ttk.Spinbox(self, from_=from_, to=to_, textvariable=var, width=width)
        self.spinbox.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        if range_var:
            self.range_label = ttk.Label(self, textvariable=range_var, foreground=self.light_text)
            self.range_label.grid(row=0, column=2, sticky=tk.W, padx=(0,10), pady=5)
        if tooltip_text:
            self.tooltip_text = tooltip_text
            self.label.bind("<Enter>", self.show_tooltip)
            self.label.bind("<Leave>", self.hide_tooltip)
    def show_tooltip(self, event):
        x,y,_w,_h = self.label.bbox("insert")
        x += self.label.winfo_rootx()+25
        y += self.label.winfo_rooty()+25
        self.tooltip = tk.Toplevel(self)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        ttk.Label(self.tooltip, text=self.tooltip_text, background="#ffffe0", relief="solid", borderwidth=1).pack()
    def hide_tooltip(self, event):
        if hasattr(self,'tooltip'):
            self.tooltip.destroy()

class OptimalSamplesSelectionSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Optimal Samples Selection System")
        self.root.geometry("1000x750")
        self.db = DatabaseManager()
        # UI setup omitted: build tabs, inputs, results, database view
        # Bind events: compute, save, load, delete using algorithm and db manager
        # For example:
        # self.compute_button.config(command=self.find_optimal_samples)

    def find_optimal_samples(self):
        # Retrieve params, call compute_optimized_samples, update UI
        pass

    def save_to_database(self):
        # Call db.save_result with params, samples, time and groups
        pass

    def refresh_database_list(self):
        # Load list via db.get_all_results and populate treeview
        pass

    # Other methods (clear_results, load_selected_result, delete_selected_result) omitted for brevity

class ModernUI(ttk.Frame):
    """Custom styling for a modern UI look"""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        
        # Define custom styles
        self.style = ttk.Style()
        
        # Configure colors
        self.bg_color = "#f5f5f7"
        self.accent_color = "#0066cc"
        self.success_color = "#34c759"
        self.warning_color = "#ff9500"
        self.error_color = "#ff3b30"
        self.text_color = "#333333"
        self.light_text = "#666666"
        
        # Configure theme
        self.style.configure("TFrame", background=self.bg_color)
        self.style.configure("TLabel", background=self.bg_color, foreground=self.text_color)
        self.style.configure("TLabelframe", background=self.bg_color)
        self.style.configure("TLabelframe.Label", background=self.bg_color, foreground=self.text_color, font=('Helvetica', 10, 'bold'))
        
        # Button styles
        self.style.configure("Accent.TButton", background=self.accent_color, foreground="white")
        self.style.map("Accent.TButton",
                  background=[('active', '#0055aa'), ('pressed', '#004488')])
        
        self.style.configure("Success.TButton", background=self.success_color)
        self.style.map("Success.TButton",
                  background=[('active', '#2eb04d'), ('pressed', '#27994b')])
        
        self.style.configure("Warning.TButton", background=self.warning_color)
        self.style.map("Warning.TButton",
                  background=[('active', '#e67e00'), ('pressed', '#cc7000')])
        
        # Notebook style
        self.style.configure("TNotebook", background=self.bg_color, borderwidth=0)
        self.style.configure("TNotebook.Tab", background=self.bg_color, foreground=self.text_color, padding=[12, 6])
        self.style.map("TNotebook.Tab",
                  background=[('selected', 'white')],
                  foreground=[('selected', self.accent_color)])
        
        # Spinbox style
        self.style.configure("TSpinbox", background="white", foreground=self.text_color, arrowcolor=self.accent_color)

class ParameterInput(ttk.Frame):
    """Custom widget for parameter input with label, spinbox, and range indicator"""
    def __init__(self, parent, label_text, var, from_, to_, width=10, range_var=None, tooltip_text=None):
        super().__init__(parent)
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)
        
        # Label
        self.label = ttk.Label(self, text=label_text, font=('Helvetica', 10, 'bold'))
        self.label.grid(row=0, column=0, sticky=tk.W, padx=(0, 5), pady=5)
        
        # Spinbox
        self.spinbox = ttk.Spinbox(self, from_=from_, to=to_, textvariable=var, width=width)
        self.spinbox.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Range indicator
        if range_var:
            self.range_label = ttk.Label(self, textvariable=range_var, foreground="#666666")
            self.range_label.grid(row=0, column=2, sticky=tk.W, padx=(0, 10), pady=5)
        
        # Tooltip
        if tooltip_text:
            self.tooltip_text = tooltip_text
            self.label.bind("<Enter>", self.show_tooltip)
            self.label.bind("<Leave>", self.hide_tooltip)
    
    def show_tooltip(self, event):
        x, y, _, _ = self.label.bbox("insert")
        x += self.label.winfo_rootx() + 25
        y += self.label.winfo_rooty() + 25

        # Create tooltip window
        self.tooltip = tk.Toplevel(self)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        
        # Create tooltip content
        frame = ttk.Frame(self.tooltip, borderwidth=1, relief="solid")
        frame.pack(ipadx=5, ipady=5)
        
        label = ttk.Label(frame, text=self.tooltip_text, wraplength=250, justify="left")
        label.pack()
    
    def hide_tooltip(self, event):
        if hasattr(self, 'tooltip'):
            self.tooltip.destroy()

# Replacement for scipy.special.comb
def combination_count(n, k):
    """Calculate binomial coefficient (n choose k)"""
    if k < 0 or k > n:
        return 0
    if k > n - k:
        k = n - k  # Use symmetry
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c

class OptimalSamplesSelectionSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Optimal Samples Selection System")
        self.root.geometry("1000x750")
        self.root.configure(bg="#f5f5f7")
        
        # Apply modern UI styling
        self.ui = ModernUI(self.root)
        
        # Custom fonts
        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.header_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.body_font = font.Font(family="Helvetica", size=10)
        self.small_font = font.Font(family="Helvetica", size=9)
        
        # Variables
        self.m_var = tk.IntVar(value=45)
        self.n_var = tk.IntVar(value=9)
        self.k_var = tk.IntVar(value=6)
        self.j_var = tk.IntVar(value=5)
        self.s_var = tk.IntVar(value=4)
        self.selected_samples = []
        self.results = []
        self.computation_time = 0
        
        # Range variables
        self.m_range = tk.StringVar(value="(45-54)")
        self.n_range = tk.StringVar(value="(7-25)")
        self.k_range = tk.StringVar(value="(4-7)")
        self.j_range = tk.StringVar(value="(4-6)")
        self.s_range = tk.StringVar(value="(3-5)")
        
        # Computation control
        self._cancel_computation = False
        self._computation_progress = "Starting..."
        
        # Setup database
        self.setup_database()
        
        # Create UI
        self.create_ui()
        
        # Set up dynamic validation
        self.setup_dynamic_validation()
    
    def setup_database(self):
        # Create database if it doesn't exist
        conn = sqlite3.connect('optimal_samples.db')
        cursor = conn.cursor()
        
        # Create table for results
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            m INTEGER,
            n INTEGER,
            k INTEGER,
            j INTEGER,
            s INTEGER,
            run_id TEXT,
            num_results INTEGER,
            samples TEXT,
            timestamp TEXT,
            computation_time REAL
        )
        ''')
        # 为现有数据库添加 computation_time 列（若不存在）
        try:
            cursor.execute("ALTER TABLE results ADD COLUMN computation_time REAL")
        except sqlite3.OperationalError:
            pass
        
        # Create table for result groups
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS result_groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            result_id INTEGER,
            group_num INTEGER,
            group_samples TEXT,
            FOREIGN KEY (result_id) REFERENCES results (id)
        )
        ''')
        
        conn.commit()
        conn.close()
    
    def create_ui(self):
        # App header
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill=tk.X, padx=20, pady=(20, 0))
        
        app_title = ttk.Label(header_frame, text="Optimal Samples Selection System", font=self.title_font)
        app_title.pack(side=tk.LEFT)
        
        # Main content with tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create tabs
        self.input_tab = ttk.Frame(self.notebook)
        self.results_tab = ttk.Frame(self.notebook)
        self.database_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.input_tab, text="Input Parameters")
        self.notebook.add(self.results_tab, text="Results")
        self.notebook.add(self.database_tab, text="Database")
        
        # Setup each tab
        self.setup_input_tab()
        self.setup_results_tab()
        self.setup_database_tab()
    
    def setup_input_tab(self):
        # Create a scrollable canvas for the input tab
        canvas = tk.Canvas(self.input_tab, bg="#f5f5f7", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.input_tab, orient="vertical", command=canvas.yview)
        content_frame = ttk.Frame(canvas)
        
        content_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Parameter section
        param_section = ttk.LabelFrame(content_frame, text="Parameter Settings", padding=(15, 10))
        param_section.pack(fill=tk.X, padx=10, pady=10)
        
        # Parameter grid layout
        param_grid = ttk.Frame(param_section)
        param_grid.pack(fill=tk.X, padx=5, pady=5)
        
        # Column titles
        ttk.Label(param_grid, text="Basic Parameters", font=self.header_font).grid(row=0, column=0, columnspan=3, sticky=tk.W, padx=5, pady=(5, 10))
        
        # Create parameter inputs with tooltips
        m_input = ParameterInput(
            param_grid, "Total samples (m):", self.m_var, 45, 54, 
            range_var=self.m_range,
            tooltip_text="The total number of available samples (45-54)"
        )
        m_input.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        
        n_input = ParameterInput(
            param_grid, "Select samples (n):", self.n_var, 7, 25,  # Increased upper limit
            range_var=self.n_range,
            tooltip_text="Number of samples to select from the total m samples (7-25)"
        )
        n_input.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Advanced parameters title
        ttk.Label(param_grid, text="Advanced Parameters", font=self.header_font).grid(row=2, column=0, columnspan=3, sticky=tk.W, padx=5, pady=(15, 10))
        
        k_input = ParameterInput(
            param_grid, "Group size (k):", self.k_var, 4, 7, 
            range_var=self.k_range,
            tooltip_text="Size of each group in the result (4-7, default is 6)"
        )
        k_input.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        
        j_input = ParameterInput(
            param_grid, "Subgroup size (j):", self.j_var, 4, 7, 
            range_var=self.j_range,
            tooltip_text="Size of the subgroups to cover (must be between s and k)"
        )
        j_input.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
        
        s_input = ParameterInput(
            param_grid, "Overlap size (s):", self.s_var, 3, 7, 
            range_var=self.s_range,
            tooltip_text="Minimum overlap between k-groups and j-groups (3-7, must be ≤ j)"
        )
        s_input.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        
        # Performance options
        perf_frame = ttk.Frame(param_grid)
        perf_frame.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)
        
        self.use_optimized = tk.BooleanVar(value=True)
        ttk.Checkbutton(perf_frame, text="Use optimized algorithm for large n", 
                        variable=self.use_optimized).pack(anchor=tk.W)
        
        # Store references to spinboxes
        self.j_spinbox = j_input.spinbox
        self.s_spinbox = s_input.spinbox
        self.k_spinbox = k_input.spinbox
        
        # Parameter descriptions
        desc_frame = ttk.LabelFrame(content_frame, text="Parameter Explanations", padding=(15, 10))
        desc_frame.pack(fill=tk.X, padx=10, pady=10)
        
        descriptions = [
            ("m", "Total number of available samples (universe size)", "The complete set from which we select our working samples"),
            ("n", "Number of samples to select from m", "The subset we'll work with for finding optimal groups"),
            ("k", "Size of each group in the result", "Default is 6 as per project requirements"),
            ("j", "Size of the subgroups to cover", "Must be between s and k"),
            ("s", "Minimum overlap size", "The minimum number of elements that must overlap between j-subgroups and k-groups")
        ]
        
        for i, (param, title, desc) in enumerate(descriptions):
            param_frame = ttk.Frame(desc_frame)
            param_frame.pack(fill=tk.X, padx=5, pady=5)
            
            ttk.Label(param_frame, text=param, font=('Helvetica', 11, 'bold'), foreground=self.ui.accent_color).pack(side=tk.LEFT, padx=(0, 5))
            ttk.Label(param_frame, text=f"- {title}:", font=('Helvetica', 10, 'bold')).pack(side=tk.LEFT, padx=(0, 5))
            ttk.Label(param_frame, text=desc, wraplength=600).pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Performance note for larger n values
        perf_note = ttk.Frame(desc_frame)
        perf_note.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(perf_note, text="⚠️ Performance Note:", font=('Helvetica', 11, 'bold'), foreground=self.ui.warning_color).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Label(perf_note, text="For n > 20, computation may take several minutes. The optimized algorithm uses approximation techniques for larger values of n to improve performance.", wraplength=600).pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Sample selection section
        sample_section = ttk.LabelFrame(content_frame, text="Sample Selection", padding=(15, 10))
        sample_section.pack(fill=tk.X, padx=10, pady=10)
        
        # Action buttons with modern styling
        action_frame = ttk.Frame(sample_section)
        action_frame.pack(fill=tk.X, padx=5, pady=5)
        
        validate_btn = ttk.Button(action_frame, text="✓ Validate Parameters", style="Accent.TButton", command=self.validate_parameters)
        validate_btn.pack(side=tk.LEFT, padx=5, pady=10)
        
        ttk.Button(action_frame, text="🎲 Generate Random Samples", command=self.generate_random_samples).pack(side=tk.LEFT, padx=5, pady=10)
        ttk.Button(action_frame, text="✏️ Input Samples Manually", command=self.input_samples_manually).pack(side=tk.LEFT, padx=5, pady=10)
        ttk.Button(action_frame, text="🔍 Find Optimal Samples", style="Success.TButton", command=self.find_optimal_samples).pack(side=tk.LEFT, padx=5, pady=10)
        
        # Selected samples display with better styling
        samples_frame = ttk.Frame(sample_section)
        samples_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(samples_frame, text="Selected Samples:", font=('Helvetica', 10, 'bold')).pack(anchor=tk.W, padx=5, pady=(5, 0))
        
        self.samples_display = tk.Text(samples_frame, height=3, width=60, bg="white", fg="#333333", relief="flat", borderwidth=1, highlightthickness=1, highlightbackground="#cccccc")
        self.samples_display.pack(fill=tk.X, padx=5, pady=5)
        
        # Status bar with styled appearance
        status_frame = ttk.Frame(content_frame)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=(0, 10))
        
        self.status_var = tk.StringVar(value="Ready")
        self.status_indicator = ttk.Label(status_frame, text="●", foreground=self.ui.success_color)
        self.status_indicator.pack(side=tk.LEFT, padx=(5, 0))
        ttk.Label(status_frame, textvariable=self.status_var).pack(side=tk.LEFT, padx=(5, 0))
    
    def setup_dynamic_validation(self):
        # Set up trace callbacks to update ranges when values change
        self.k_var.trace_add("write", self.update_j_range)
        self.j_var.trace_add("write", self.update_s_range)
        
        # Update n range - now allows up to 25
        self.n_range.set("(7-25)")
    
    def update_j_range(self, *args):
        try:
            k = self.k_var.get()
            s = self.s_var.get()
            
            # j must be between s and k
            min_j = max(4, s)
            max_j = k
            
            self.j_range.set(f"({min_j}-{max_j})")
            self.j_spinbox.config(from_=min_j, to=max_j)
            
            # Adjust j if needed
            current_j = self.j_var.get()
            if current_j < min_j:
                self.j_var.set(min_j)
            elif current_j > max_j:
                self.j_var.set(max_j)
        except:
            pass
    
    def update_s_range(self, *args):
        try:
            j = self.j_var.get()
            
            # s must be between 3 and j
            min_s = 3
            max_s = j
            
            self.s_range.set(f"({min_s}-{max_s})")
            self.s_spinbox.config(from_=min_s, to=max_s)
            
            # Adjust s if needed
            current_s = self.s_var.get()
            if current_s < min_s:
                self.s_var.set(min_s)
            elif current_s > max_s:
                self.s_var.set(max_s)
        except:
            pass
    
    def setup_results_tab(self):
        # Results header
        header_frame = ttk.Frame(self.results_tab)
        header_frame.pack(fill=tk.X, padx=15, pady=15)
        
        self.result_header_var = tk.StringVar(value="No results available")
        ttk.Label(header_frame, textvariable=self.result_header_var, font=self.header_font).pack(side=tk.LEFT)
        
        # Results content in a scrollable frame
        results_frame = ttk.LabelFrame(self.results_tab, text="Optimal Groups", padding=(15, 10))
        results_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(results_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.results_text = tk.Text(results_frame, height=20, width=60, bg="white", fg="#333333", 
                                    yscrollcommand=scrollbar.set, relief="flat", borderwidth=0, 
                                    highlightthickness=1, highlightbackground="#cccccc", padx=10, pady=10)
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.config(command=self.results_text.yview)
        
        # Configure text display tags
        self.results_text.tag_configure("group_number", foreground=self.ui.accent_color, font=('Helvetica', 10, 'bold'))
        self.results_text.tag_configure("group_content", foreground="#333333", font=('Helvetica', 10))
        self.results_text.tag_configure("summary", foreground="#666666", font=('Helvetica', 11, 'italic'))
        
        # Action buttons
        action_frame = ttk.Frame(self.results_tab)
        action_frame.pack(fill=tk.X, padx=15, pady=(0, 15))
        
        ttk.Button(action_frame, text="💾 Save to Database", style="Accent.TButton", command=self.save_to_database).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(action_frame, text="🗑️ Clear Results", command=self.clear_results).pack(side=tk.LEFT, padx=5, pady=5)
    
    def setup_database_tab(self):
        # Database controls
        control_frame = ttk.Frame(self.database_tab)
        control_frame.pack(fill=tk.X, padx=15, pady=15)
        
        ttk.Label(control_frame, text="Saved Results", font=self.header_font).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(control_frame, text="📂 Load Selected", style="Accent.TButton", command=self.load_results).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(control_frame, text="🗑️ Delete Selected", command=self.delete_selected_result).pack(side=tk.LEFT, padx=5, pady=5)
        
        # Search frame
        search_frame = ttk.Frame(self.database_tab)
        search_frame.pack(fill=tk.X, padx=15, pady=(0, 10))
        
        ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT, padx=(0, 5))
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=30)
        search_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="🔍 Search", command=self.search_database).pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="❌ Clear", command=self.clear_search).pack(side=tk.LEFT, padx=5)
        
        # Database results list
        list_frame = ttk.LabelFrame(self.database_tab, text="Result History", padding=(15, 10))
        list_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        
        # Create treeview with scrollbar
        scrollbar_y = ttk.Scrollbar(list_frame)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        scrollbar_x = ttk.Scrollbar(list_frame, orient="horizontal")
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.tree = ttk.Treeview(list_frame, columns=("ID", "Parameters", "Samples", "Groups", "Date", "Computation Time"), 
                                 show="headings", yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar_y.config(command=self.tree.yview)
        scrollbar_x.config(command=self.tree.xview)
        
        # Configure columns
        self.tree.heading("ID", text="ID")
        self.tree.heading("Parameters", text="Parameters")
        self.tree.heading("Samples", text="# Samples")
        self.tree.heading("Groups", text="# Groups")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Computation Time", text="Computation Time")
        
        self.tree.column("ID", width=50, minwidth=50)
        self.tree.column("Parameters", width=200, minwidth=150)
        self.tree.column("Samples", width=80, minwidth=80)
        self.tree.column("Groups", width=80, minwidth=80)
        self.tree.column("Date", width=150, minwidth=120)
        self.tree.column("Computation Time", width=150, minwidth=120)
        
        # Style the treeview rows
        self.tree.tag_configure('odd', background='#f5f5f7')
        self.tree.tag_configure('even', background='white')
        
        # Bind double-click event
        self.tree.bind("<Double-1>", lambda event: self.load_selected_result())
        
        # Load database entries
        self.refresh_database_list()
    
    def search_database(self):
        search_term = self.search_var.get().strip().lower()
        if not search_term:
            self.refresh_database_list()
            return
            
        # Clear current items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Search in database
        try:
            conn = sqlite3.connect('optimal_samples.db')
            cursor = conn.cursor()
            
            # Search by parameters or date
            cursor.execute('''
            SELECT id, m, n, k, j, s, num_results, timestamp, computation_time
            FROM results
            WHERE LOWER(timestamp) LIKE ? OR 
                  m LIKE ? OR n LIKE ? OR k LIKE ? OR j LIKE ? OR s LIKE ?
            ORDER BY timestamp DESC
            ''', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%', 
                  f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
            
            for i, row in enumerate(cursor.fetchall()):
                id, m, n, k, j, s, num_results, timestamp, computation_time = row
                self.tree.insert('', 'end', values=(
                    id,
                    f"m={m}, n={n}, k={k}, j={j}, s={s}",
                    n,
                    num_results,
                    timestamp,
                    f"{computation_time:.2f} seconds"
                ), tags=('even' if i % 2 == 0 else 'odd'))
            
            conn.close()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error searching database: {str(e)}")
    
    def clear_search(self):
        self.search_var.set("")
        self.refresh_database_list()
    
    def validate_parameters(self):
        try:
            m = self.m_var.get()
            n = self.n_var.get()
            k = self.k_var.get()
            j = self.j_var.get()
            s = self.s_var.get()
            
            valid = True
            message = ""
            
            if not (45 <= m <= 54):
                valid = False
                message += "m must be between 45 and 54\n"
            
            if not (7 <= n <= 25):  # Increased upper limit
                valid = False
                message += "n must be between 7 and 25\n"
            
            if not (4 <= k <= 7):
                valid = False
                message += "k must be between 4 and 7\n"
            
            if not (s <= j <= k):
                valid = False
                message += f"j must be between s ({s}) and k ({k})\n"
            
            if not (3 <= s <= j):
                valid = False
                message += f"s must be between 3 and j ({j})\n"
            
            # Performance warning for large n
            if n > 20:
                message += f"\nWarning: n={n} is large. Computation may take several minutes.\nThe optimized algorithm will be used."
            
            if valid:
                # Show success feedback
                self.status_indicator.config(foreground=self.ui.success_color)
                self.status_var.set("Parameters validated successfully!")
                
                if n > 20:  # Show warning but still valid
                    messagebox.showwarning("Performance Warning", message)
                else:
                    messagebox.showinfo("Validation", "Parameters are valid!")
                
                # Update ranges after validation
                self.update_j_range()
                self.update_s_range()
                return True
            else:
                # Show error feedback
                self.status_indicator.config(foreground=self.ui.error_color)
                self.status_var.set("Parameter validation failed")
                messagebox.showerror("Validation Error", message)
                return False
                
        except Exception as e:
            self.status_indicator.config(foreground=self.ui.error_color)
            self.status_var.set(f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))
            return False
    
    def generate_random_samples(self):
        try:
            if not self.validate_parameters():
                return
            
            m = self.m_var.get()
            n = self.n_var.get()
            
            all_samples = list(range(1, m+1))
            self.selected_samples = random.sample(all_samples, n)
            self.selected_samples.sort()
            
            # Display selected samples
            self.samples_display.delete(1.0, tk.END)
            self.samples_display.insert(tk.END, ', '.join(f"{s:02d}" for s in self.selected_samples))
            
            self.status_indicator.config(foreground=self.ui.success_color)
            self.status_var.set(f"Generated {n} random samples from {m} total samples")
            
        except Exception as e:
            self.status_indicator.config(foreground=self.ui.error_color)
            self.status_var.set(f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))
    
    def input_samples_manually(self):
        try:
            if not self.validate_parameters():
                return
            
            n = self.n_var.get()
            m = self.m_var.get()
            
            # Create a custom dialog for better user experience
            dialog = tk.Toplevel(self.root)
            dialog.title("Input Samples")
            dialog.geometry("500x300")
            dialog.transient(self.root)
            dialog.grab_set()
            
            # Dialog content
            ttk.Label(dialog, text=f"Enter {n} samples (1-{m}) separated by commas:", 
                      font=('Helvetica', 11, 'bold')).pack(pady=(20, 5), padx=20, anchor=tk.W)
            
            ttk.Label(dialog, text=f"Example: 1, 2, 3, 4, 5, 6, 7, 8, 9", 
                      foreground="#666666").pack(pady=(0, 10), padx=20, anchor=tk.W)
            
            # Input text with scrollbar
            input_frame = ttk.Frame(dialog)
            input_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
            
            scrollbar = ttk.Scrollbar(input_frame)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            samples_entry = tk.Text(input_frame, height=5, width=50, yscrollcommand=scrollbar.set)
            samples_entry.pack(fill=tk.BOTH, expand=True)
            scrollbar.config(command=samples_entry.yview)
            
            # Pre-fill with current samples if any
            if self.selected_samples:
                samples_entry.insert(tk.END, ', '.join(str(s) for s in self.selected_samples))
            
            # Dialog validation function
            def validate_and_close():
                samples_str = samples_entry.get(1.0, tk.END).strip()
                
                # Parse input
                try:
                    # Clean up input - allow various separators
                    cleaned_str = samples_str.replace(';', ',').replace(' ', ',')
                    while ',,' in cleaned_str:
                        cleaned_str = cleaned_str.replace(',,', ',')
                    
                    samples = [int(s.strip()) for s in cleaned_str.split(',') if s.strip()]
                except:
                    messagebox.showerror("Error", "Invalid input format. Please enter numbers separated by commas.", parent=dialog)
                    return
                
                # Validate number of samples
                if len(samples) != n:
                    messagebox.showerror("Error", f"You must enter exactly {n} samples", parent=dialog)
                    return
                
                # Validate sample values
                if any(s < 1 or s > m for s in samples):
                    messagebox.showerror("Error", f"Samples must be between 1 and {m}", parent=dialog)
                    return
                
                # Validate uniqueness
                if len(set(samples)) != len(samples):
                    messagebox.showerror("Error", "Samples must be unique", parent=dialog)
                    return
                
                # Success - store and close
                self.selected_samples = samples
                self.selected_samples.sort()
                
                # Display selected samples
                self.samples_display.delete(1.0, tk.END)
                self.samples_display.insert(tk.END, ', '.join(f"{s:02d}" for s in self.selected_samples))
                
                self.status_indicator.config(foreground=self.ui.success_color)
                self.status_var.set(f"Manually entered {n} samples")
                
                dialog.destroy()
            
            # Button frame
            button_frame = ttk.Frame(dialog)
            button_frame.pack(pady=15)
            
            ttk.Button(button_frame, text="Cancel", command=dialog.destroy).pack(side=tk.RIGHT, padx=5)
            ttk.Button(button_frame, text="OK", style="Accent.TButton", command=validate_and_close).pack(side=tk.RIGHT, padx=5)
            
            # Center dialog on parent window
            dialog.update_idletasks()
            x = self.root.winfo_x() + (self.root.winfo_width() - dialog.winfo_width()) // 2
            y = self.root.winfo_y() + (self.root.winfo_height() - dialog.winfo_height()) // 2
            dialog.geometry(f"+{x}+{y}")
            
            # Set focus to the text entry
            samples_entry.focus_set()
            
            # Wait for dialog to close
            self.root.wait_window(dialog)
            
        except Exception as e:
            self.status_indicator.config(foreground=self.ui.error_color)
            self.status_var.set(f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))
    
    def find_optimal_samples(self):
        try:
            if not self.selected_samples:
                messagebox.showerror("Error", "No samples selected")
                return
            
            if not self.validate_parameters():
                return
            
            m = self.m_var.get()
            n = len(self.selected_samples)
            k = self.k_var.get()
            j = self.j_var.get()
            s = self.s_var.get()
            
            # Estimate computation time based on n
            estimate_text = "a few seconds"
            if n > 15:
                estimate_text = "about a minute"
            if n > 20:
                estimate_text = "a few minutes"
            if n > 25:
                estimate_text = "several minutes"
            
            # Update status
            self.status_indicator.config(foreground=self.ui.warning_color)
            self.status_var.set(f"Computing optimal samples, may take {estimate_text}...")
            self.root.update()
            
            # Show loading dialog for long computations
            progress_dialog = tk.Toplevel(self.root)
            progress_dialog.title("Computing...")
            progress_dialog.geometry("400x200")
            progress_dialog.transient(self.root)
            progress_dialog.grab_set()
            
            ttk.Label(progress_dialog, text="Finding optimal sample groups...", 
                     font=('Helvetica', 11, 'bold')).pack(pady=(20, 5))
            
            progress = ttk.Progressbar(progress_dialog, mode="indeterminate")
            progress.pack(fill=tk.X, padx=20, pady=10)
            progress.start(10)
            
            info_var = tk.StringVar(value=f"Working with n={n}, k={k}, j={j}, s={s}\nThis may take {estimate_text}...")
            info_label = ttk.Label(progress_dialog, textvariable=info_var)
            info_label.pack(pady=5)
            
            cancel_button = ttk.Button(progress_dialog, text="Cancel", command=lambda: setattr(self, '_cancel_computation', True))
            cancel_button.pack(pady=15)
            
            # Center dialog
            progress_dialog.update_idletasks()
            x = self.root.winfo_x() + (self.root.winfo_width() - progress_dialog.winfo_width()) // 2
            y = self.root.winfo_y() + (self.root.winfo_height() - progress_dialog.winfo_height()) // 2
            progress_dialog.geometry(f"+{x}+{y}")
            
            self.root.update()
            
            # For cancellation
            self._cancel_computation = False
            
            # Set up a monitoring function for long computations
            def update_progress():
                if hasattr(self, '_computation_progress'):
                    # Update progress info if available
                    info_var.set(f"Working with n={n}, k={k}, j={j}, s={s}\n{self._computation_progress}")
                
                if not self._cancel_computation:
                    progress_dialog.after(500, update_progress)
            
            # Start progress updates
            update_progress()
            
            # Start computation in the main thread
            start_time = time.time()
            try:
                k_groups = self.compute_optimized_samples(k, j, s)
            except Exception as e:
                messagebox.showerror("Error", f"Computation error: {str(e)}")
                k_groups = []
            
            # Close progress dialog
            progress_dialog.destroy()
            
            if self._cancel_computation:
                self.status_indicator.config(foreground=self.ui.warning_color)
                self.status_var.set("Computation cancelled")
                return
            
            if not k_groups:
                messagebox.showinfo("Result", "No solution found")
                self.status_indicator.config(foreground=self.ui.error_color)
                self.status_var.set("No solution found")
                return
            
            self.results = k_groups
            
            # Switch to results tab
            self.notebook.select(self.results_tab)
            
            # Update results header
            self.result_header_var.set(f"Results for m={m}, n={n}, k={k}, j={j}, s={s}")
            
            # Display results with styled formatting
            self.results_text.delete(1.0, tk.END)
            for i, group in enumerate(k_groups, 1):
                formatted_group = ', '.join(f"{s:02d}" for s in group)
                self.results_text.insert(tk.END, f"{i}. ", "group_number")
                self.results_text.insert(tk.END, f"{formatted_group}\n", "group_content")
            
            computation_time = time.time() - start_time
            self.computation_time = computation_time
            self.results_text.insert(tk.END, f"\nFound {len(k_groups)} groups of {k} samples in {computation_time:.2f} seconds.", "summary")
            
            self.status_indicator.config(foreground=self.ui.success_color)
            self.status_var.set(f"Found {len(k_groups)} optimal groups in {computation_time:.2f} seconds")
            
        except Exception as e:
            self.status_indicator.config(foreground=self.ui.error_color)
            self.status_var.set(f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))
    
    def compute_optimized_samples(self, k, j, s):
        """Hybrid greedy hint + CP-SAT for exact set cover with upper bound"""
        samples = self.selected_samples
        n = len(samples)

        # 1. Generate all j-subsets
        j_subsets = list(itertools.combinations(range(n), j))
        # 2. Generate all k-groups
        k_groups = list(itertools.combinations(range(n), k))

        # 3. Compute coverage for each k-group and filter out those that cover nothing
        group_cov = []
        for kg in k_groups:
            cov_js = [idx for idx, js in enumerate(j_subsets) if len(set(kg) & set(js)) >= s]
            group_cov.append(cov_js)
        valid_idx = [i for i, covs in enumerate(group_cov) if covs]
        k_groups = [k_groups[i] for i in valid_idx]
        group_cov = [group_cov[i] for i in valid_idx]

        # 4. Create CP-SAT model and bool vars
        model = cp_model.CpModel()
        x_vars = [model.NewBoolVar(f'x{i}') for i in range(len(k_groups))]

        # 5. Cover constraints via AddBoolOr
        for j_idx in range(len(j_subsets)):
            cov_list = [x_vars[i] for i, covs in enumerate(group_cov) if j_idx in covs]
            if cov_list:
                model.AddBoolOr(cov_list)

        # Objective: minimize number of groups
        model.Minimize(sum(x_vars))

        # Solver parameters
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = 60
        # 使用所有 CPU 物理核心
        solver.parameters.num_search_workers = multiprocessing.cpu_count()

        status = solver.Solve(model)
        raw = []
        if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            for i, var in enumerate(x_vars):
                if solver.Value(var):
                    raw.append(k_groups[i])
        # 将索引组映射回实际样本值
        return [tuple(samples[idx] for idx in grp) for grp in raw]
    
    def generate_diverse_k_groups(self, n, k, max_groups):
        """Generate a diverse set of k-groups for better coverage"""
        all_indices = list(range(n))
        k_groups = []
        
        # Update status
        self._computation_progress = f"Generating diverse k-groups..."
        self.root.update()
        
        # Start with some random groups to ensure diversity
        initial_groups = min(max_groups // 4, 100)
        for i in range(initial_groups):
            if i % 10 == 0:
                self._computation_progress = f"Generating initial groups ({i}/{initial_groups})..."
                self.root.update()
                
                if self._cancel_computation:
                    return k_groups
                    
            k_groups.append(tuple(sorted(random.sample(all_indices, k))))
        
        # Then generate groups with more structure to improve coverage
        strategies = ["core", "spaced", "clusters", "random"]
        strategy_idx = 0
        
        while len(k_groups) < max_groups:
            strategy = strategies[strategy_idx % len(strategies)]
            strategy_idx += 1
            
            if len(k_groups) % 100 == 0:
                self._computation_progress = f"Generating k-groups: {len(k_groups)}/{max_groups} using {strategy} strategy"
                self.root.update()
                
                if self._cancel_computation:
                    return k_groups
            
            if strategy == "core":
                # Strategy 1: Build around a small core of 2-3 elements
                core_size = min(k-1, 3)
                core = random.sample(all_indices, core_size)
                remaining = [i for i in all_indices if i not in core]
                rest = random.sample(remaining, k-core_size)
                new_group = tuple(sorted(core + rest))
            
            elif strategy == "spaced":
                # Strategy 2: Ensure we have groups that maximize distance between elements
                # Take elements that are spaced apart
                step = max(1, n // k)
                start = random.randint(0, n-1)
                new_group = tuple(sorted((start + i*step) % n for i in range(k)))
            
            elif strategy == "clusters":
                # Strategy 3: Form clusters in different regions
                # Pick a region and select elements close to each other
                center = random.randint(0, n-1)
                window = min(n, k*2)  # Double the window size to ensure enough elements
                region = [(center + i) % n for i in range(-window//2, window//2)]
                if len(region) >= k:
                    new_group = tuple(sorted(random.sample(region, k)))
                else:
                    new_group = tuple(sorted(random.sample(all_indices, k)))
            
            else:  # "random"
                # Strategy 4: Pure random sampling
                new_group = tuple(sorted(random.sample(all_indices, k)))
            
            # Only add if this is a new group
            if new_group not in k_groups:
                k_groups.append(new_group)
        
        return k_groups
    
    def save_to_database(self):
        try:
            if not self.results:
                messagebox.showerror("Error", "No results to save")
                return
            
            m = self.m_var.get()
            n = len(self.selected_samples)
            k = self.k_var.get()
            j = self.j_var.get()
            s = self.s_var.get()
            
            # Generate a unique run ID
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            run_id = f"{m}-{n}-{k}-{j}-{s}-{timestamp}"
            
            # Save to database
            conn = sqlite3.connect('optimal_samples.db')
            cursor = conn.cursor()
            
            # Insert into results table
            cursor.execute('''
            INSERT INTO results (m, n, k, j, s, run_id, num_results, samples, timestamp, computation_time)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (m, n, k, j, s, run_id, len(self.results), 
                 ','.join(str(s) for s in self.selected_samples),
                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                 self.computation_time))
            
            result_id = cursor.lastrowid
            
            # Insert groups
            for i, group in enumerate(self.results, 1):
                cursor.execute('''
                INSERT INTO result_groups (result_id, group_num, group_samples)
                VALUES (?, ?, ?)
                ''', (result_id, i, ','.join(str(s) for s in group)))
            
            conn.commit()
            conn.close()
            
            # Display success message with custom dialog
            success_dialog = tk.Toplevel(self.root)
            success_dialog.title("Success")
            success_dialog.geometry("350x180")
            success_dialog.transient(self.root)
            success_dialog.grab_set()
            
            # Green check mark using unicode
            ttk.Label(success_dialog, text="✅", font=('Helvetica', 36)).pack(pady=(20, 0))
            ttk.Label(success_dialog, text=f"Results saved to database!", 
                     font=('Helvetica', 12, 'bold')).pack(pady=(5, 10))
            ttk.Label(success_dialog, text=f"ID: {result_id}").pack(pady=0)
            
            ttk.Button(success_dialog, text="OK", command=success_dialog.destroy).pack(pady=15)
            
            # Center dialog
            success_dialog.update_idletasks()
            x = self.root.winfo_x() + (self.root.winfo_width() - success_dialog.winfo_width()) // 2
            y = self.root.winfo_y() + (self.root.winfo_height() - success_dialog.winfo_height()) // 2
            success_dialog.geometry(f"+{x}+{y}")
            
            # Refresh database list
            self.refresh_database_list()
            
        except Exception as e:
            self.status_indicator.config(foreground=self.ui.error_color)
            self.status_var.set(f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))
    
    def clear_results(self):
        self.results = []
        self.results_text.delete(1.0, tk.END)
        self.result_header_var.set("No results available")
    
    def refresh_database_list(self):
        # Clear current items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get items from database
        try:
            conn = sqlite3.connect('optimal_samples.db')
            cursor = conn.cursor()
            
            cursor.execute('''
            SELECT id, m, n, k, j, s, num_results, timestamp, computation_time
            FROM results
            ORDER BY timestamp DESC
            ''')
            
            for i, row in enumerate(cursor.fetchall()):
                id, m, n, k, j, s, num_results, timestamp, computation_time = row
                self.tree.insert('', 'end', values=(
                    id,
                    f"m={m}, n={n}, k={k}, j={j}, s={s}",
                    n,
                    num_results,
                    timestamp,
                    f"{computation_time:.2f} seconds"
                ), tags=('even' if i % 2 == 0 else 'odd'))
            
            conn.close()
            
        except Exception as e:
            self.status_indicator.config(foreground=self.ui.error_color)
            self.status_var.set(f"Error loading database: {str(e)}")
            messagebox.showerror("Error", f"Error loading database: {str(e)}")
    
    def load_selected_result(self):
        try:
            selection = self.tree.selection()
            if not selection:
                messagebox.showerror("Error", "No item selected")
                return
            
            item = self.tree.item(selection[0])
            result_id = item['values'][0]
            
            # Load result from database
            conn = sqlite3.connect('optimal_samples.db')
            cursor = conn.cursor()
            
            # Get result info
            cursor.execute('''
            SELECT m, n, k, j, s, samples, computation_time
            FROM results
            WHERE id = ?
            ''', (result_id,))
            
            result_info = cursor.fetchone()
            if not result_info:
                messagebox.showerror("Error", "Result not found")
                conn.close()
                return
            
            m, n, k, j, s, samples_str, computation_time = result_info
            
            # Set parameters
            self.m_var.set(m)
            self.n_var.set(n)
            self.k_var.set(k)
            self.j_var.set(j)
            self.s_var.set(s)
            
            # Set samples
            self.selected_samples = [int(s) for s in samples_str.split(',')]
            self.samples_display.delete(1.0, tk.END)
            self.samples_display.insert(tk.END, ', '.join(f"{s:02d}" for s in self.selected_samples))
            
            # Get groups
            cursor.execute('''
            SELECT group_samples
            FROM result_groups
            WHERE result_id = ?
            ORDER BY group_num
            ''', (result_id,))
            
            groups = []
            for row in cursor.fetchall():
                group_samples = [int(s) for s in row[0].split(',')]
                groups.append(group_samples)
            
            conn.close()
            
            # Store and display results
            self.results = groups
            
            # Update results header
            self.result_header_var.set(f"Results for m={m}, n={n}, k={k}, j={j}, s={s}")
            
            # Display results with styled formatting
            self.results_text.delete(1.0, tk.END)
            for i, group in enumerate(groups, 1):
                formatted_group = ', '.join(f"{s:02d}" for s in group)
                self.results_text.insert(tk.END, f"{i}. ", "group_number")
                self.results_text.insert(tk.END, f"{formatted_group}\n", "group_content")
            
            self.results_text.insert(tk.END, f"\nFound {len(groups)} groups of {k} samples in {computation_time:.2f} seconds.", "summary")
            
            # Switch to results tab
            self.notebook.select(self.results_tab)
            
            # Update status
            self.status_indicator.config(foreground=self.ui.success_color)
            self.status_var.set(f"Loaded result ID {result_id} from database")
            
        except Exception as e:
            self.status_indicator.config(foreground=self.ui.error_color)
            self.status_var.set(f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))
    
    def load_results(self):
        self.load_selected_result()
    
    def delete_selected_result(self):
        try:
            selection = self.tree.selection()
            if not selection:
                messagebox.showerror("Error", "No item selected")
                return
            
            item = self.tree.item(selection[0])
            result_id = item['values'][0]
            
            # Confirm deletion with a custom dialog
            confirm_dialog = tk.Toplevel(self.root)
            confirm_dialog.title("Confirm Deletion")
            confirm_dialog.geometry("350x180")
            confirm_dialog.transient(self.root)
            confirm_dialog.grab_set()
            
            ttk.Label(confirm_dialog, text="⚠️", font=('Helvetica', 36)).pack(pady=(20, 0))
            ttk.Label(confirm_dialog, text=f"Delete result ID {result_id}?", 
                     font=('Helvetica', 12, 'bold')).pack(pady=(5, 10))
            ttk.Label(confirm_dialog, text="This action cannot be undone.").pack(pady=0)
            
            button_frame = ttk.Frame(confirm_dialog)
            button_frame.pack(pady=15)
            
            # Deletion function
            def confirm_delete():
                try:
                    # Delete from database
                    conn = sqlite3.connect('optimal_samples.db')
                    cursor = conn.cursor()
                    
                    cursor.execute('DELETE FROM result_groups WHERE result_id = ?', (result_id,))
                    cursor.execute('DELETE FROM results WHERE id = ?', (result_id,))
                    
                    conn.commit()
                    conn.close()
                    
                    # Refresh list
                    self.refresh_database_list()
                    
                    self.status_indicator.config(foreground=self.ui.success_color)
                    self.status_var.set(f"Deleted result ID {result_id}")
                    
                    confirm_dialog.destroy()
                    
                except Exception as e:
                    self.status_indicator.config(foreground=self.ui.error_color)
                    self.status_var.set(f"Error: {str(e)}")
                    messagebox.showerror("Error", str(e), parent=confirm_dialog)
            
            ttk.Button(button_frame, text="Cancel", command=confirm_dialog.destroy).pack(side=tk.LEFT, padx=10)
            ttk.Button(button_frame, text="Delete", style="Warning.TButton", command=confirm_delete).pack(side=tk.LEFT, padx=10)
            
            # Center dialog
            confirm_dialog.update_idletasks()
            x = self.root.winfo_x() + (self.root.winfo_width() - confirm_dialog.winfo_width()) // 2
            y = self.root.winfo_y() + (self.root.winfo_height() - confirm_dialog.winfo_height()) // 2
            confirm_dialog.geometry(f"+{x}+{y}")
            
        except Exception as e:
            self.status_indicator.config(foreground=self.ui.error_color)
            self.status_var.set(f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))