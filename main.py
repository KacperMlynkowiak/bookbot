def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    num_char = get_num_char(text)
    print(f"{num_char}")
    sorted_chars = sort_char_counts(num_char)
    print_char_counts(sorted_chars)



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_char(text):
    lowered_string = text.lower()
    char_counts = {}
    for char in lowered_string:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] +=1
            else:
                char_counts[char] = 1
    return char_counts


def sort_char_counts(char_counts):
    char_count_list = list(char_counts.items())
    char_count_list.sort(key=lambda item:item[1], reverse = True)
    return char_count_list


def print_char_counts(sorted_chars):
    print(f"The character counts are:")
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")








main()