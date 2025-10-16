import string

def count_words(filename):
    small_words = set()
    large_words = set()

    try:
        with open(filename, "r") as file:
            for line in file:
                # Remove punctuation and split into words
                words = line.strip().split()
                for word in words:
                    # Clean punctuation around the word (like "line." or "file?")
                    clean_word = word.strip(string.punctuation)
                    if not clean_word:
                        continue
                    # Sort words by length
                    if len(clean_word) < 3:
                        small_words.add(clean_word)
                    else:
                        large_words.add(clean_word)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return 0

    # Write large words to file
    with open("large-words.txt", "w") as lw:
        for w in sorted(large_words):
            lw.write(w + "\n")

    # Write small words to file
    with open("small-words.txt", "w") as sw:
        for w in sorted(small_words):
            sw.write(w + "\n")

    # Return total unique words
    return len(large_words.union(small_words))


# Usage
def ex3():
    total_words = count_words(r"C:\Users\Administrator\Desktop\input.txt")
    print(f"Total words: {total_words}.")


# Run
ex3()
