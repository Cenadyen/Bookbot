def get_num_words(book):
    word_list = book.split()
    return len(word_list)

def char_count(book):
    char_dict = {}
    for char in book:
        if char.lower() not in char_dict:
            char_dict[char.lower()] = 1
        else:
            char_dict[char.lower()] += 1
    return char_dict

def char_list(complete_char_dictionary):
    char_list = []
    for char, count in complete_char_dictionary.items():
        if char.isalpha():
            char_dict = {"char": char,
                          "num": count}
            char_list.append(char_dict)
    return char_list

def sort_on(items):
    return items["num"]