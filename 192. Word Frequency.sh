# Read from the file words.txt and output the word frequency list to stdout.

file="words.txt"


awk '{
    for (i=1; i<=NF; i++) {
        words[$i]++
    }
}
END {
    for (word in words) {
        print word, words[word]
    }
}' "$file" | sort -k2,2nr -k1
