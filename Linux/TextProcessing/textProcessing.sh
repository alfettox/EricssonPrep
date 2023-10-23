#!/bin/bash
echo "OPERATIONS: word_count | char_count | line_count | grep_search | word_frequency | file_copy"
echo "Usage: $0 <operation> <file_path> [parameter]"

if [ "$#" -lt 2 ]; then
  exit 1
fi

if [ "$1" == "word_count" ]; then
  echo "Word count in $2:"
  wc -w "$2"

elif [ "$1" == "char_count" ]; then
  echo "Character count in $2:"
  wc -m "$2"

elif [ "$1" == "line_count" ]; then
  echo "Line count in $2:"
  wc -l "$2"

elif [ "$1" == "grep_search" ]; then
  if [ -z "$3" ]; then
    echo "Usage: $0 grep_search <file_path> <search_pattern>"
    exit 1
  fi
  echo "Occurrences of '$3' in $2:"
  grep -c "$3" "$2"

elif [ "$1" == "word_frequency" ]; then
  echo "Word frequency in $2:"
  tr -cs '[:alpha:]' '\n' < "$2" | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr

elif [ "$1" == "file_copy" ]; then
  cp "$2" "${2}.backup"
  echo "Backup copy created as ${2}.backup"

else
  echo "Invalid operation. Supported operations: word_count, char_count, line_count, grep_search, word_frequency, file_copy"
  exit 1
fi
