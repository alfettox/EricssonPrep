# Directory Management Shell Script

This is a simple shell script for managing directories and files. It provides options to create directories, move files, copy files, and delete files.

## Prerequisites

- A Unix-like operating system (Linux, macOS, Git Bash on Windows).
- A working shell environment (bash).

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the directory where the script is located.

3. Make the script executable (if needed):

   ```bash
   chmod +x manageFiles.sh
Run the script:

bash
Copy code
./manageFiles.sh
You will be presented with a menu to select an operation:

1 - Create a directory
2 - Move a file
3 - Copy a file
4 - Delete a file
Follow the prompts and provide the required inputs as specified for each operation.

Commands and Parameters
Operation 1: Create a directory
Description: Creates a new directory.
Command: 1
Parameters:
Enter directory name: - Enter the name of the directory you want to create.
Operation 2: Move a file
Description: Moves a file from one location to another.
Command: 2
Parameters:
Enter source file path: - Enter the path to the source file.
Enter destination path: - Enter the path to the destination directory where the file should be moved.
Operation 3: Copy a file
Description: Copies a file to another location.
Command: 3
Parameters:
Enter source path: - Enter the path to the source file.
Enter destination directory: - Enter the path to the destination directory where the file should be copied.
Operation 4: Delete a file
Description: Deletes a file.
Command: 4
Parameters:
Enter file to be deleted: - Enter the path to the file you want to delete.
Example
To create a directory named "my_directory," select operation 1 and enter my_directory as the directory name.

To move a file named "my_file.txt" from the current directory to a directory named "my_destination," select operation 2, enter my_file.txt as the source file path, and enter the full path to the "my_destination" directory as the destination path.

To copy a file named "document.doc" from the current directory to a directory named "backup," select operation 3, enter document.doc as the source path, and enter the full path to the "backup" directory as the destination directory.

To delete a file named "old_file.txt," select operation 4 and enter old_file.txt as the file to be deleted.