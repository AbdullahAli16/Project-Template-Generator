import os 
import json

with open("templates.json", "r") as f:
    templates=json.load(f)

print("Hello, Welcome to the Folder Template Generator (Made by Abdullah): ")
for number, template in templates.items():
    print(f"{number} → {template['folder']}")
print("Which template would you like to choose (1-6) ?")

while True:
    
    # Asking the user to choose a template
    chosen_template= input("Choose any one of the above: ")
    
    # Handles wrong chosen template input
    if chosen_template in templates:
        break
    else:
        print("Invalid choice. Please pick a valid number from the list.")
    

if chosen_template in templates:
    
    # Handles wrong number of copies input
    while True:
        # Asking the user how many copies does he/she need
        copies=input("How many copies do you need ? (Default : 1): ")

        if copies.strip()=="":
            copies=1
            break
        elif copies.isdigit() and int(copies)>0:
            copies=int(copies)
            break
        else:
            print("Please enter a positive number.")
    
    # Overwriting chosen_template from an integer to the dictionary of the template
    chosen_template= templates[chosen_template]

    # Asking the user to custom name the template
    rename_template=input("Enter your project folder name: ")
    if rename_template.strip()=="":
        rename_template=chosen_template["folder"]

    # Asking the user for the path for the project folder
    destined_path=input("Enter the path where you want to create the project folder (leave blank for current directory): ")

    # If no path given then sets the current directory as default path
    if destined_path.strip()=="":
        destined_path=os.getcwd()

    # Handles incorrect path input and sets the current directory as default path
    elif not os.path.exists(destined_path):
        print("Given path is either empty or doe'nt exist. Using current directory instead. ")
        destined_path=os.getcwd()

    for i in range(1,copies+1):
        if copies==1:
            folder_name=rename_template
        else:
            folder_name=f"{rename_template}_{i}"

        # Making Folder
        folder_path=os.path.join(destined_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path, exist_ok=True)
        
        # Making Sub-Folders(If they exist)
        if "subfolders" in chosen_template:
            for subfolder in chosen_template["subfolders"]:
                os.makedirs(os.path.join(folder_path,subfolder),exist_ok=True)

        # Making Files
        for file, content in chosen_template['files'].items():
            file_path=os.path.join(folder_path,file)
            with open(file_path,'w') as f:
                f.write(content)
                
    print(f"\nProject(s) Template created successfully at: {destined_path}")
else:
    print("Error, no template with this input found")

