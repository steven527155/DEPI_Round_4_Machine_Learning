import tkinter as tk
from tkinter import ttk, messagebox
from main import EmployeeManager

class EmployeeGUI:
    WINDOW_SIZE = "950x600"
    TITLE = "Employee Management System"

    def __init__(self, root):
        self.root = root
        self.manager = EmployeeManager()
        self._configure_window()
        self._create_widgets()
        self._update_table()

    def _configure_window(self):
        self.root.title(self.TITLE)
        self.root.geometry(self.WINDOW_SIZE)

    def _create_widgets(self):
        self._create_input_section()
        self._create_buttons()
        self._create_table()
        self._create_status_bar()

    def _create_input_section(self):
        frame = tk.LabelFrame(self.root, text="Employee Details", padx=10, pady=10)
        frame.pack(fill="x", padx=20, pady=10)
        self.entries = {}
        for index, field in enumerate(self.manager.FIELDS):
            row, col = index // 3, (index % 3) * 2
            tk.Label(frame, text=f"{field}:").grid(row=row, column=col, padx=5, pady=5)
            entry = tk.Entry(frame)
            entry.grid(row=row, column=col + 1, padx=5, pady=5)
            self.entries[field] = entry

    def _create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)
        btn_config = [
            ("Add", self.do_add, "#d4edda"),
            ("Update", self.do_update, "#fff3cd"),
            ("Delete", self.do_delete, "#f8d7da"),
            ("Search", self.do_search, None),
            ("Clear Fields", self.do_clear, "#e2e3e5")
        ]
        for text, cmd, clr in btn_config:
            tk.Button(frame, text=text, command=cmd, width=12, bg=clr).pack(side="left", padx=5)

    def _create_table(self):
        self.tree = ttk.Treeview(self.root, columns=self.manager.FIELDS, show="headings")
        for field in self.manager.FIELDS:
            self.tree.heading(field, text=field)
            self.tree.column(field, width=140)
        self.tree.pack(fill="both", expand=True, padx=20, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self._on_row_click)

    def _create_status_bar(self):
        self.status_var = tk.StringVar()
        tk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor="w").pack(side="bottom", fill="x")

    def _update_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for emp in self.manager.get_all_employees():
            row = [emp.get(f, "") for f in self.manager.FIELDS]
            self.tree.insert("", tk.END, values=row)
        self.status_var.set(f" Total Records: {len(self.manager.employees)}")

    def _on_row_click(self, event):
        selected = self.tree.focus()
        if not selected: return
        values = self.tree.item(selected, "values")
        for i, field in enumerate(self.manager.FIELDS):
            self.entries[field].delete(0, tk.END)
            self.entries[field].insert(0, values[i]) 

    def do_clear(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def do_add(self):
        data = {f: self.entries[f].get().strip() for f in self.manager.FIELDS}
        success, msg = self.manager.add_employee(data)
        if success:
            self._update_table()
            self.do_clear()
            messagebox.showinfo("Success", msg)
        else: messagebox.showerror("Error", msg)

    def do_update(self):
        emp_id = self.entries["ID"].get().strip()
        data = {f: self.entries[f].get().strip() for f in self.manager.FIELDS}
        if self.manager.update_employee(emp_id, data):
            self._update_table()
            messagebox.showinfo("Success", "Updated")
        else: messagebox.showerror("Error", "ID not found or invalid data")

    def do_delete(self):
        emp_id = self.entries["ID"].get().strip()
        if self.manager.delete_employee(emp_id):
            self._update_table()
            self.do_clear()
            messagebox.showinfo("Success", "Deleted")
        else: messagebox.showerror("Error", "ID not found")

    def do_search(self):
        emp_id = self.entries["ID"].get().strip()
        emp = self.manager.search_employee(emp_id)
        if emp: messagebox.showinfo("Found", str(emp))
        else: messagebox.showwarning("Not Found", "Employee not found")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeGUI(root)
    root.mainloop()