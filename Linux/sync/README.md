# Directory Synchronization Bash Script

## Overview

This is a Bash script that uses `rsync` to synchronize the contents of two directories. It checks if the source directory exists, and if not, it creates the destination directory. Then, it uses `rsync` to copy the contents of the source directory to the destination directory.

## Script Explanation

Here is an explanation of the key components of the script:

- It takes two command-line arguments, which are the source directory and the destination directory.

- It checks if the source directory exists using the `-d` flag with the `[ -d "$source_directory" ]` conditional statement.

- If the source directory does not exist, it exits with an error message.

- It also checks if the destination directory exists. If it doesn't, the script creates it using `mkdir -p "$destination_directory"`.

- Finally, it uses `rsync` to synchronize the source and destination directories: `rsync -avh "$source_directory/" "$destination_directory/"`. The `-avh` options stand for archive mode, verbose output, and human-readable file sizes.

## Difficulties Encountered

- One of the difficulties encountered was ensuring that the source and destination directories are provided as full paths. This is essential for the script to work correctly in a Windows environment when using WSL.

- Handling spaces and special characters in directory paths can be challenging. It's important to use double quotes (`"$source_directory"`) to handle paths with spaces or special characters correctly.

## Usage

1. Save the script to a file, for example, `sync_directories.sh`.

2. Make the script executable using `chmod +x sync_directories.sh`.

3. Run the script, providing the source and destination directories as command-line arguments:

```bash
./sync_directories.sh /mnt/c/dev/EricssonPrep/EricssonPrep/Linux/sync/dirA /mnt/c/dev/EricssonPrep/EricssonPrep/Linux/sync/dirB
Simpler Synchronization
Keep in mind that if you have a simpler requirement for directory synchronization, you can use the rsync command directly in the terminal, as shown below:

bash
Copy code
rsync -avh /source/directory/ /destination/directory/
This command directly synchronizes the contents of the source and destination directories without the need for a separate Bash script.

Conclusion
This script provides a simple way to synchronize the contents of two directories using rsync. It can be used to ensure that the contents of the source and destination directories are identical.