# Automated Backup Script

Automate the backup process with this bash script that simplifies creating and managing backups for a specified directory.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Parameters](#parameters)
- [Examples](#examples)
- [Backup Retention](#backup-retention)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create backups with a single command.
- Organize backups by date and time.
- Automatically prune older backups to maintain a specified retention policy.
- User-friendly interface.

## Prerequisites

- Bash shell.
- Source directory to be backed up.
- Destination directory for storing backups.

## Usage

1. Clone this repository or download the script.

2. Make the script executable:

   ```bash
   chmod +x autobackup.sh
Run the script with the necessary parameters.

For example:


``./autobackup.sh /path/to/source /path/to/destination 5``

### Parameters
Source directory: The directory you want to back up.
Destination directory: The directory where backups will be stored.
Backup number: The number of backups to keep. Older backups are pruned to meet this policy.

### Examples
Create a backup of /data in /backups and retain the last 5 backups:


``./autobackup.sh /data /backups 5``

Backup Retention

The script automatically manages backup retention. Excess backups are pruned to maintain the specified number.

Error Handling
The script handles various scenarios