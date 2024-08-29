# Read from the file file.txt and output all valid phone numbers to stdout.
#!/bin/bash


while IFS= read -r line; do
    
    if [[ "$line" =~ ^[0-9]{3}-[0-9]{3}-[0-9]{4}$ || "$line" =~ ^\([0-9]{3}\)\ [0-9]{3}-[0-9]{4}$ ]]; then
        echo "$line"
    fi
done < file.txt