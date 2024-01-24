def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_to_dict = get_letter_count_to_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(letter_to_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")



def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count_to_dict(text): 
    chars = {}                      # en dictionary där sökningen sparas
    for c in text:                  # loop genom alla bokstäver i texten
        lowered = c.lower()         # bokstäverna blir gemener, döps om från c till lowered
        if lowered in chars:        
            chars[lowered] += 1     # om bokstäven redan finns i dictionaryn så ökar valuen till den keyn med en
        else:
            chars[lowered] = 1      # om bokstaven ej finns så skapar keyn med valuen 1
    return chars

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
