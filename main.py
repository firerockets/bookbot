def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_map = {}
    for char in text:
        lowercased = char.lower()
        if lowercased in char_map:
            char_map[lowercased] += 1
        else:
            char_map[lowercased] = 1
    return char_map

def count_alphabetical(text):
    char_map = {}
    for char in text:
        lowercased = char.lower()
        if ord(lowercased) >= ord("a") and ord(lowercased) <= ord("z"):
            if lowercased in char_map:
                char_map[lowercased] += 1
            else:
                char_map[lowercased] = 1
    return char_map

def generate_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document")
    print("")
    alphabetical_chars = count_alphabetical(text)
    for char in alphabetical_chars:
        print(f"The '{char}' character was found {alphabetical_chars[char]} times")
    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        generate_report(file_contents)

main()