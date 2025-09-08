import os
import sys
import json
import customtkinter as ctk
from tkinter import filedialog, messagebox
import tkinter as tk

# -------------------------
# Utility for PyInstaller resources
# -------------------------
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):  # Running from PyInstaller bundle
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# -------------------------
# Load templates from JSON
# -------------------------
with open(resource_path("templates.json"), "r") as f:
    templates = json.load(f)

# -------------------------
# Main Application Class
# -------------------------
class FolderTemplateApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Try to set icon (ICO preferred for Windows, PNG fallback for others)
        try:
            self.iconbitmap(resource_path("assets/icon.ico"))  # Windows
        except Exception:
            try:
                self.iconphoto(False, tk.PhotoImage(file=resource_path("assets/icon.png")))  # Fallback
            except Exception as e:
                print("Icon could not be loaded:", e)

        self.title("Folder Template Generator (By Abdullah)")
        self.geometry("800x600")
        ctk.set_appearance_mode("System")  # Default: "System", can switch to "Light" or "Dark"
        ctk.set_default_color_theme("blue")

        # Scrollable main frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=780, height=580)
        self.scrollable_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Title label
        self.title_label = ctk.CTkLabel(self.scrollable_frame, text="Folder Template Generator", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        # Theme switch button
        self.theme_button = ctk.CTkButton(self.scrollable_frame, text="Toggle Theme (Light/Dark)", command=self.toggle_theme)
        self.theme_button.pack(pady=5)

        # Template Selection
        self.template_label = ctk.CTkLabel(self.scrollable_frame, text="Choose a template:", font=("Arial", 14))
        self.template_label.pack(pady=5)

        self.template_var = ctk.StringVar()
        self.template_dropdown = ctk.CTkOptionMenu(self.scrollable_frame, variable=self.template_var,
                                                   values=[f"{num} → {t['folder']}" for num, t in templates.items()],
                                                   command=self.show_preview)
        self.template_dropdown.pack(pady=5)

        # Preview area with scrollbar
        self.preview_label = ctk.CTkLabel(self.scrollable_frame, text="Template Preview:", font=("Arial", 14, "bold"))
        self.preview_label.pack(pady=5)

        self.preview_textbox = ctk.CTkTextbox(self.scrollable_frame, width=700, height=200, wrap="word")
        self.preview_textbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.preview_textbox.configure(state="disabled")

        # Number of copies input
        self.copies_label = ctk.CTkLabel(self.scrollable_frame, text="How many copies do you need? (Default: 1)", font=("Arial", 14))
        self.copies_label.pack(pady=5)
        self.copies_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="1")
        self.copies_entry.pack(pady=5)

        # Project folder name input
        self.rename_label = ctk.CTkLabel(self.scrollable_frame, text="Enter your project folder name:", font=("Arial", 14))
        self.rename_label.pack(pady=5)
        self.rename_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Project Name")
        self.rename_entry.pack(pady=5)

        # Destination path selection
        self.path_label = ctk.CTkLabel(self.scrollable_frame, text="Choose destination path:", font=("Arial", 14))
        self.path_label.pack(pady=5)

        self.path_frame = ctk.CTkFrame(self.scrollable_frame)
        self.path_frame.pack(pady=5)

        self.path_var = ctk.StringVar(value=os.getcwd())
        self.path_entry = ctk.CTkEntry(self.path_frame, textvariable=self.path_var, width=400)
        self.path_entry.pack(side="left", padx=5)

        self.browse_button = ctk.CTkButton(self.path_frame, text="Browse", command=self.browse_path)
        self.browse_button.pack(side="left", padx=5)

        # Generate button
        self.generate_button = ctk.CTkButton(self.scrollable_frame, text="Generate Template", command=self.generate_template,
                                            font=("Arial", 14, "bold"))
        self.generate_button.pack(pady=20)

    # -------------------------
    # Toggle theme between Light and Dark
    # -------------------------
    def toggle_theme(self):
        current = ctk.get_appearance_mode()
        if current == "Light":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    # -------------------------
    # Show preview of template
    # -------------------------
    def show_preview(self, event=None):
        selected_value = self.template_var.get()
        if not selected_value:
            return

        chosen_index = selected_value.split(" → ")[0]
        chosen_template = templates[chosen_index]

        preview_content = f"📂 Folder: {chosen_template['folder']}\n"

        if "subfolders" in chosen_template:
            preview_content += "\n📁 Subfolders:\n"
            for sub in chosen_template["subfolders"]:
                preview_content += f"   └─ {sub}\n"

        if "files" in chosen_template:
            preview_content += "\n📄 Files:\n"
            for f in chosen_template["files"]:
                preview_content += f"   └─ {f}\n"

        self.preview_textbox.configure(state="normal")
        self.preview_textbox.delete("1.0", "end")
        self.preview_textbox.insert("end", preview_content)
        self.preview_textbox.configure(state="disabled")

    # -------------------------
    # Browse for destination path
    # -------------------------
    def browse_path(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_var.set(folder)

    # -------------------------
    # Main logic for generating folders
    # -------------------------
    def generate_template(self):
        selected_value = self.template_var.get()
        if not selected_value:
            messagebox.showerror("Error", "Please choose a valid template.")
            return

        chosen_index = selected_value.split(" → ")[0]
        chosen_template = templates[chosen_index]

        # Handle number of copies
        copies_input = self.copies_entry.get().strip()
        if copies_input == "":
            copies = 1
        elif copies_input.isdigit() and int(copies_input) > 0:
            copies = int(copies_input)
        else:
            messagebox.showerror("Error", "Please enter a positive number for copies.")
            return

        # Handle rename input
        rename_template = self.rename_entry.get().strip()
        if rename_template == "":
            rename_template = chosen_template["folder"]

        # Handle path input
        destined_path = self.path_var.get().strip()
        if destined_path == "" or not os.path.exists(destined_path):
            destined_path = os.getcwd()

        # Create folders and files
        for i in range(1, copies + 1):
            folder_name = rename_template if copies == 1 else f"{rename_template}_{i}"
            folder_path = os.path.join(destined_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            # Subfolders
            if "subfolders" in chosen_template:
                for subfolder in chosen_template["subfolders"]:
                    os.makedirs(os.path.join(folder_path, subfolder), exist_ok=True)

            # Files
            for file, content in chosen_template['files'].items():
                file_path = os.path.join(folder_path, file)
                with open(file_path, 'w') as f:
                    f.write(content)

        messagebox.showinfo("Success", f"Project(s) Template created successfully at: {destined_path}")

# -------------------------
# Run the application
# -------------------------
if __name__ == "__main__":
    app = FolderTemplateApp()
    app.mainloop()
