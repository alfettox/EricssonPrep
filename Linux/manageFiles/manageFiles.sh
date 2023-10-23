#!/bin/bash

#Menu
echo "Directory management shell script"

echo "___________________________"
echo "1- Create a directory"
echo "2- Move file"
echo "3- Copy file"
echo "4- Delete file"
read -p "Please select an option: " choice

case $choice in
    1) echo "DIRECTORY CREATE TOOL" 
    read -p "Enter directory name: " directory_name
    if [ -d "$directory_name" ]; then
        echo "Directory '$directory_name' already exists"
    else
        mkdir "$directory_name"
        echo "Directory '$directory_name' created"
    fi
    ;;

    2) echo "FILE MOVE TOOL" 
    read -p "Enter source file path: " source_file
        read -p "Enter destination path: " destination_dir
       if [ -f "$source_file" ]; then
            mv "$source_file" "$destination_dir"
            echo "File moved successfully"
        else
            echo "Source file or destination directory not existing"
        fi
        ;;
        
    3) echo "FILE COPY TOOL"
        read -p "Enter source path: " source_file
        read -p "Enter destination directory:" destination_dir
             if [ -f "$source_file" ] && [ -d "$destination_dir" ]; then
            cp "$source_file" "$destination_dir"
            echo "File copied successfully"
        else
            echo "Source file or destination direcotry not existing"
        fi
        ;;

    4) echo "DELETE FILE TOOL"
        read -p "Enter file to be deleted: " file_to_delete
        if [ -f "$file_to_delete" ]; then
            rm "$file_to_delete"
            echo "File '$file_to_delete' deleted successfully"
        else
            echo "File not existing"
        fi
        ;;

    *) echo "Invalid choice"
esac