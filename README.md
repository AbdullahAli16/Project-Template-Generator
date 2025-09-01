# Project Template Generator

A Python script to quickly create project folder structures from predefined templates.  
Instead of manually setting up folders and files every time, use this generator to save time.  

---

## Features
- Choose from predefined project templates (`templates.json`).
- Automatically create folders, subfolders, and files.
- Supports multiple copies of the same project template.
- Allows custom project names and target directory.
- Handles invalid inputs gracefully.

---

## Requirements
- Python 3.x
- `templates.json` file (included in the project)

---

## Usage

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/project-template-generator.git
cd project-template-generator
```

### 2. Run the Script
```bash
python generator.py
```

### 3. Example Run
```text
Hello, Welcome to the Project Template Generator (Made by Abdullah): 
1 → Python Project
2 → Web Project
3 → React Project
...
Which template would you like to choose (1-6)? 1
How many copies do you need ? (Default : 1): 2
Enter your project folder name: MyApp
Enter the path where you want to create the project folder (leave blank for current directory): 

Project(s) Template created successfully at: /your/path
```

---

## Customizing Templates

Templates are stored in the `templates.json` file.  
Each template can define:

* **folder** → main folder name  
* **subfolders** → list of subfolders  
* **files** → files to be created with optional starter content  

**Example (`templates.json`):**
```json
{
  "1": {
    "folder": "PythonProject",
    "subfolders": ["src", "tests"],
    "files": {
      "README.md": "# Python Project",
      "main.py": "print('Hello World')"
    }
  }
}
```

---

## Future Improvements
- Add argparse support for CLI arguments.
- More built-in templates.
- Option to save custom templates directly from the script.

---

## Author
Made with ❤️ by Abdullah
