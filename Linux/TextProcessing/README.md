# Text Processing Script

This script is a versatile text processing tool that allows you to perform various operations on text files. It supports operations such as word count, character count, line count, grep search, word frequency analysis, and file backup. This README provides instructions on how to use the script and make it executable.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Supported Operations](#supported-operations)
- [Making the Script Executable](#making-the-script-executable)

## Prerequisites

Before using this script, ensure you have the following prerequisites:

- A Unix-like operating system (Linux, macOS, or similar).
- Bash (Bourne-Again Shell) installed on your system.

## Usage

To use the `textProcessing.sh` script, follow these instructions:

1. Download the `textProcessing.sh` script to your project directory.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.

### Basic Usage

You can use the script with the following format:

```bash
./textProcessing.sh <operation> <file_path> [additional_parameters]
<operation> Choose one of the supported operations (e.g., word_count, char_count, line_count, grep_search, word_frequency, or file_copy).

<file_path>: Specify the path to the text file you want to process.
[additional_parameters]: Additional parameters required for specific operations (e.g., search pattern for grep_search).
```
Examples
Count the number of words in a text file:

./textProcessing.sh word_count sample.txt
Find the number of lines in a text file:

./textProcessing.sh line_count sample.txt
Perform a case-insensitive word frequency analysis:

./textProcessing.sh word_frequency sample.txt
Create a backup copy of a text file:

./textProcessing.sh file_copy sample.txt
Please refer to the Supported Operations section for more details on each operation.


Supported Operations
The script supports the following operations:

Word Count (word_count): Count the number of words in a text file.
Character Count (char_count): Count the number of characters in a text file.

Line Count (line_count): Count the number of lines in a text file.
Grep Search (grep_search): Search for a pattern in the text file and count occurrences.

Word Frequency (word_frequency): Perform word frequency analysis (case-insensitive).

File Copy (file_copy): Create a backup copy of a text file.
Please specify the desired operation when using the script.

Making the Script Executable
Before using the script, you need to make it executable. Use the chmod command to set the execute permission:

```
chmod +x textProcessing.sh
```
This allows you to run the script with the ./ prefix.

For example:

./textProcessing.sh word_count sample.txt
Now you're ready to use the textProcessing.sh script for various text processing tasks!

Commands
echo: The echo command is used to print messages or text to the console.

Example:

```
echo "OPERATIONS: word_count | char_count | line_count | grep_search | word_frequency | file_copy"
```
read: The read command allows users to enter input interactively. It stores user input into variables.

Example:

```
read -p "Please select an option: " choice 
if-elif-else-fi: ``` These are conditional statements that control the flow of the script. They are used for making decisions based on the values of variables or conditions.

Example:

```
if [ "$1" == "word_count" ]; then
wc: ``` The wc command is used to count words, characters, or lines in a text file.

Example:


wc -w "$2"
grep:
 The grep command searches for patterns in text. It can be used to count occurrences of a pattern in a file.

Example:

bash
Copy code
grep -c "$3" "$2"
tr: The tr command is used for character translation. It can replace or delete characters in text.

Example:

bash
Copy code
tr -cs '[:alpha:]' '\n' < "$2"
sort: The sort command is used to sort lines of text files.

Example:

bash
Copy code
sort | uniq -c | sort -nr
cp: The cp command is used to copy files or directories.

Example:

bash
Copy code
cp "$2" "${2}.backup"
Parameters
$#: This parameter represents the number of arguments passed to the script.

$1, $2, $3, ...: These parameters represent the values of the script's arguments. For example, $1 is the first argument, $2 is the second argument, and so on.

$0: This parameter represents the name of the script itself.

Control Flow
The script uses conditional statements (if-elif-else-fi) to control its flow. It checks the value of the first argument ($1) to determine which operation to perform. Based on the operation, the script executes different commands. If the operation is not recognized, it displays an error message.

Data Structures
The script primarily deals with text data from files. It counts words, characters, and lines, searches for patterns, performs word frequency analysis, and creates backup copies of text files. It uses variables to store user input, file paths, and search patterns.

In the case of word frequency analysis, it processes text data through a series of commands (tr, sort, uniq) to calculate the frequency of words.

The script also uses conditional statements to control the flow and make decisions based on the chosen operation.