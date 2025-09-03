# 📂 Auto File Sorter

A simple Python script that automatically organizes files in a given directory into categorized folders based on their extensions.  

---

## 🚀 Features
- Sorts files into categories:
  - **Pictures** (`.jpg`, `.png`, `.gif`, etc.)
  - **Videos** (`.mp4`, `.mkv`, `.avi`, etc.)
  - **Audios** (`.mp3`, `.wav`, `.flac`, etc.)
  - **Documents** (`.pdf`, `.docx`, `.txt`, `.csv`, etc.)
  - **Applications** (`.exe`, `.apk`, `.msi`, etc.)
  - **Archives** (`.zip`, `.rar`, `.7z`, etc.)
  - **Others** (for unrecognized file types)
- Creates folders automatically if they don’t exist.
- Prevents moving the script file itself.
- Works on **Windows, Linux, and macOS**.

---

## 🛠️ Requirements
- Python 3.x
- Built-in libraries only: `os`, `shutil`

---

## 📥 Installation, ▶️ Usage, and Example (single terminal)

```bash
# 1) Clone the repository
git clone https://github.com/your-username/auto-file-sorter.git

# 2) Enter the project folder
cd auto-file-sorter

# 3) Check Python version
python --version
Python 3.10.12

# 4) Run the script
python auto_file_sorter.py
Welcome to the Sorting program (Made by Abdullah)

# 5) Provide the directory to sort when prompted
Which directory/folder do you want to sort: C:\Users\YourName\Downloads

# 6) Example result
Sorting done Successfully !
Exiting ...

# 7) Example directory BEFORE sorting
Downloads/
├── song.mp3
├── picture.jpg
├── movie.mkv
├── notes.pdf
├── setup.exe

# 8) Example directory AFTER sorting
Downloads/
├── Audios/
│   └── song.mp3
├── Pictures/
│   └── picture.jpg
├── Videos/
│   └── movie.mkv
├── Documents/
│   └── notes.pdf
├── Applications/
│   └── setup.exe

# --- Contributing ---
# Contributions, issues, and feature requests are welcome!
# Feel free to fork the repo and submit a pull request.

# --- License ---
# This project is licensed under the MIT License – you’re free to use and modify it.

# --- Author ---
# 👨‍💻 Made with ❤️ by Abdullah