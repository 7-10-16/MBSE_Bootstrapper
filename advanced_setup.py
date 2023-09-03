import folder_structure
import content_generation
import os

def setup_advanced(project_name):
    print("Advanced setup mode selected.")
    root_folder = folder_structure.create_root_folder(project_name)

    # Define the existing folder structure from folder_structure.py
    existing_folders_and_files = folder_structure.get_existing_structure()

    # Prompt the user for each folder
    custom_folders_and_files = {}
    for folder_name, files_and_content in existing_folders_and_files.items():
        include_folder = input(f"Include '{folder_name}' folder? (yes/no): ").strip().lower()
        if include_folder == 'yes':
            custom_folders_and_files[folder_name] = files_and_content

    # Create the customized folder structure and files based on user input
    for folder_name, files_and_content in custom_folders_and_files.items():
        folder_path = folder_structure.create_folder(root_folder, folder_name)
        for file_name, content_list in files_and_content.items():
            file_path = os.path.join(folder_path, file_name)
            if file_name.endswith('.docx'):
                content_generation.generate_docx_file(file_path, content_list)
            elif file_name.endswith('.txt'):
                content_generation.generate_txt_file(file_path, content_list)
            elif file_name.endswith('.xlsx'):
                content_generation.generate_excel_file(file_path, content_list)

    print(f"Advanced MBSE project setup completed in '{project_name}' folder.")

if __name__ == "__main__":
    setup_advanced("MyAdvancedProject")
