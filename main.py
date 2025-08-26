import os 

templates={
    1:{
        "folder":"Python Project",
        "files":["main.py", "Requirements.txt", "README.md", ".gitignore"]
    },
    2:{
        "folder":"Web Project",
        "files":["index.html", "style.css", "script.js", ".gitignore", "README.md"]
    }
}

print("Hello, Welcome to the Folder Template Generator (Made by Abdullah): ")
for number, template in templates.items():
    print(f"{number} → {template['folder']}")
print("Which template would you like to choose (1-2) ?")

# Asking the user to choose a template
chosen_template=int(input("Choose any one of the above: "))

# Asking the user for the path for the project folder
destined_path=input("Enter the path where you want to create the project folder (leave blank for current directory): ")

if destined_path.strip()=="":
    destined_path=os.getcwd()


if chosen_template in templates:

    # Overwriting chosen_template from an integer to the dictionary of the template
    chosen_template= templates[chosen_template]

    # Making Folder
    folder_path=os.path.join(destined_path, chosen_template['folder'])
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)

    # Making Files
    for file in chosen_template['files']:
        file_path=os.path.join(folder_path,file)
        with open(file_path,'w') as f:
            pass
else:
    print("Error, no template with this input found")

