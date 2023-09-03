import os

def create_root_folder(project_name):
    """
    Create the root folder for the MBSE project.

    Args:
        project_name (str): The name of the MBSE project.

    Returns:
        str: The path to the created root folder.
    """
    root_folder = os.path.join(".", project_name)
    os.mkdir(root_folder)
    return root_folder

def create_default_structure(parent_folder):
    """
    Create the default folder structure for the MBSE project.

    Args:
        parent_folder (str): The path to the parent folder.

    Returns:
        None
    """

def create_folder(parent_folder, folder_name):
    """
    Create a subfolder within a parent folder.

    Args:
        parent_folder (str): The path to the parent folder.
        folder_name (str): The name of the subfolder to create.

    Returns:
        str: The path to the created subfolder.
    """
    folder_path = os.path.join(parent_folder, folder_name)
    os.mkdir(folder_path)
    return folder_path

def get_existing_structure():
    """
    Define the existing folder structure and content.

    Returns:
        dict: The existing folder structure and content.
    """
    existing_folders_and_files = {
        "System_Definition": {
            "project_name_objectives.docx": [
                "System Objectives",
                "Scope",
                "Requirements",
                "Table of Contents (TOC)",
            ],
            "data.xlsx": [
                ["Data1", "Data2", "Data3"],
                [1, 2, 3],
                ["A", "B", "C"],
            ],
        },
        "Requirements": {},
        "System_Architecture_Design": {},
        "Detailed_Design": {},
        "Verification_and_Validation": {},
        "Integration_and_Testing": {},
        "Documentation_and_Reporting": {},
        "Configuration_Management": {},
        "Lifecycle_Management": {},
        "Risk_Management": {},
        "Collaboration_and_Communication": {},
    }
    return existing_folders_and_files
