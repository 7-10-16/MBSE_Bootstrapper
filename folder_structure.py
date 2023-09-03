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
            "system_objectives.docx": [
                {"type": "heading", "text": "System Objectives"},
                {"type": "paragraph", "text": "Define the objectives of the system."},
            ],
            "scope.docx": [
                {"type": "heading", "text": "Scope"},
                {"type": "paragraph", "text": "Describe the scope of the project."},
            ],
            "requirements.docx": [
                {"type": "heading", "text": "Requirements"},
                {"type": "paragraph", "text": "List the high-level requirements."},
            ],
            "toc.docx": [
                {"type": "heading", "text": "Table of Contents (TOC)"},
                {"type": "paragraph", "text": "Add a table of contents here."},
            ],
        },
        "Requirements": {
            "software_requirements_specification.docx": [
                {"type": "heading", "text": "Software Requirements Specification"},
                {"type": "paragraph", "text": "Specify the software requirements."},
            ],
            "use_cases.docx": [
                {"type": "heading", "text": "Use Cases"},
                {"type": "paragraph", "text": "Define use cases for the system."},
            ],
            "user_stories.docx": [
                {"type": "heading", "text": "User Stories"},
                {"type": "paragraph", "text": "Create user stories for the project."},
            ],
        },
        "System_Architecture_Design": {
            "architecture_diagram.png": [],
            "components.docx": [
                {"type": "heading", "text": "System Components"},
                {"type": "paragraph", "text": "Describe the system components."},
            ],
            "interfaces.docx": [
                {"type": "heading", "text": "Interfaces"},
                {"type": "paragraph", "text": "Define the system interfaces."},
            ],
        },
        "Detailed_Design": {
            "detailed_design.docx": [
                {"type": "heading", "text": "Detailed Design"},
                {"type": "paragraph", "text": "Provide detailed design specifications."},
            ],
        },
        "Verification_and_Validation": {
            "test_plan.docx": [
                {"type": "heading", "text": "Test Plan"},
                {"type": "paragraph", "text": "Define the testing strategy."},
            ],
            "test_cases.xlsx": [],
        },
        "Integration_and_Testing": {
            "integration_plan.docx": [
                {"type": "heading", "text": "Integration Plan"},
                {"type": "paragraph", "text": "Plan the system integration."},
            ],
            "test_results.xlsx": [],
        },
        "Documentation_and_Reporting": {
            "user_manual.docx": [
                {"type": "heading", "text": "User Manual"},
                {"type": "paragraph", "text": "Create a user manual for the system."},
            ],
            "project_report.docx": [
                {"type": "heading", "text": "Project Report"},
                {"type": "paragraph", "text": "Prepare a project report."},
            ],
        },
        "Configuration_Management": {
            "config_plan.docx": [
                {"type": "heading", "text": "Configuration Management Plan"},
                {"type": "paragraph", "text": "Define the configuration management process."},
            ],
        },
        "Lifecycle_Management": {
            "lifecycle_plan.docx": [
                {"type": "heading", "text": "Lifecycle Management Plan"},
                {"type": "paragraph", "text": "Outline the project's lifecycle management."},
            ],
        },
        "Risk_Management": {
            "risk_register.xlsx": [],
        },
        "Collaboration_and_Communication": {
            "meeting_minutes.docx": [],
            "communication_plan.docx": [
                {"type": "heading", "text": "Communication Plan"},
                {"type": "paragraph", "text": "Establish a communication plan for the project."},
            ],
        },
    }
    return existing_folders_and_files
