from stats import count_words, count_characters

def main():
    # Read the book file
    with open("books/frankenstein.txt", "r", encoding="utf-8") as file:
        text = file.read()

    num_words = count_words(text)

    # Print exactly what the test expects
    print(f"{num_words} words found in the document")

    # character count 
    char_counts = count_characters(text)
    print(char_counts)


if __name__ == "__main__":
    main()

