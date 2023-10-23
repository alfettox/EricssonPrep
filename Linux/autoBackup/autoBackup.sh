#!/bin/bash

if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <source_directory> <destination_directory> <backupNumber>"
  exit 1
fi

source_directory="$1"
destination_directory="$2"
backup_number="$3"
timestamp=$(date "+%Y%m%d%H%M%S")
backup_directory="${destination_directory}/backup_${timestamp}"

mkdir -p "$backup_directory"

cp -r "$source_directory" "$backup_directory"

backup_directories=($(ls -d "${destination_directory}"/backup_* | sort -r))

if [ "${#backup_directories[@]}" -gt "$backup_number" ]; then
  directories_to_delete=("${backup_directories[@]:$backup_number}")
  for dir in "${directories_to_delete[@]}"; do
    rm -r "$dir"
  done
fi

echo "Backup completed successfully in $backup_directory."
