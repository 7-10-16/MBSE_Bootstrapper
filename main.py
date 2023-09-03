import folder_structure
import content_generation
import advanced_setup 
import os

def main():
    print("Welcome to the MBSE Project Generator!")
    project_name = input("Enter the name of your MBSE project: ")
    setup_choice = input("Choose setup mode (quick/advanced): ").strip().lower()

    if setup_choice == 'quick':
        setup_quick(project_name)
    elif setup_choice == 'advanced':
        advanced_setup.setup_advanced(project_name)  # Call the advanced setup function
    else:
        print("Invalid choice. Please select 'quick' or 'advanced'.")

def setup_quick(project_name):
    # Create the root folder
    root_folder = folder_structure.create_root_folder(project_name)

    # Get the existing folder structure
    existing_folders_and_files = folder_structure.get_existing_structure()

    # Create the customized folder structure and files based on existing structure
    for folder_name, files_and_content in existing_folders_and_files.items():
        folder_path = folder_structure.create_folder(root_folder, folder_name)
        for file_name, content_list in files_and_content.items():
            file_path = os.path.join(folder_path, file_name)
            if file_name.endswith('.docx'):
                content_generation.generate_docx_file(file_path, content_list)
            elif file_name.endswith('.txt'):
                content_generation.generate_txt_file(file_path, content_list)
            elif file_name.endswith('.xlsx'):
                content_generation.generate_excel_file(file_path, content_list)

    print(f"Quick MBSE project setup completed in '{project_name}' folder.")


if __name__ == "__main__":
    main()
