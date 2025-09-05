from stats import count_words

def main():
    # Read the book file
    with open("books/frankenstein.txt", "r", encoding="utf-8") as file:
        text = file.read()

    num_words = count_words(text)

    # Print exactly what the test expects
    print(f"{num_words} words found in the document")


if __name__ == "__main__":
    main()

