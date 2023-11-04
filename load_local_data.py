import os
from typing import List

def load_local_data(files_names: List[str], path_files: str = "upload_files/") -> bool:
    """Load the local files to a SQL database.

    Args:
        files_names (List[str]): Files names list in order of upload.
        path_files (str, optional): Path directory folder to the files. Defaults to "upload_files/".

    Returns:
        bool: Return a boolean value that determine uf the load is completed.
    """

    for file_name in files_names:
        path_file = f"{path_files}{file_name}"
        with open(path_file, "r") as file:
            rows = file.readlines()
            print(len(rows))
            print(rows[:5])
    
    return True

if __name__ == "__main__":
    files_names = ["departments.csv", "jobs.csv", "hired_employees.csv"]
    path_files = "upload_files/"
    load_local_data(files_names=files_names, path_files=path_files)