import tkinter as tk
from ui import OptimalSamplesSelectionSystem


def main():
    root = tk.Tk()
    app = OptimalSamplesSelectionSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()