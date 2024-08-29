# Read from the file file.txt and output all valid phone numbers to stdout.
#!/bin/bash


while IFS= read -r line; do
    
    if [[ "$line" =~ ^[0-9]{3}-[0-9]{3}-[0-9]{4}$ || "$line" =~ ^\([0-9]{3}\)\ [0-9]{3}-[0-9]{4}$ ]]; then
        echo "$line"
    fi
done < file.txt


#sol 2


#!/bin/bash

# Define the regex pattern for valid phone numbers
pattern='^([0-9]{3}-[0-9]{3}-[0-9]{4}|\([0-9]{3}\) [0-9]{3}-[0-9]{4})$'

# Read the file line by line and filter valid phone numbers
while IFS= read -r line; do
    # Use regex to check if the line matches the valid phone number pattern
    [[ $line =~ $pattern ]] && echo "$line"
done < file.txt



#sol 3  the best and the simplest and optimised one

#!/bin/bash

grep -E '^[0-9]{3}-[0-9]{3}-[0-9]{4}$|^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$' file.txt
