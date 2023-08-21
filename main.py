def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    #begin report
    book_report = report(text)
    print(book_report)
    #num_words = count_words(text)
    #print(num_words)
    
    #total_letters = count_letters(text)
    #print(total_letters)
    #chars_dict = count_letters(text)
    #chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(word):
    words = len(word.split())
    #ammt = 0
    return words

def count_letters(texts):
    #counts the number of individual letters
    letters_dict = {}
    for letter in texts:
        lower_case = letter.lower()
        if(lower_case in letters_dict):
            letters_dict[lower_case] += 1
        else:
            letters_dict[lower_case] = 1
        
    return letters_dict

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def estimated_time_to_read(book):
    wpm = int(input("What is your words per min: "))
    
    total_time = count_words(book) // wpm + 1

    if(total_time == 0):
        total_time = 1
    elif(total_time > 60):
        return (total_time // 60)
    #return str(total_time) + 'min'


def is_this_for_you(report):
    #My own preferences
    """
    Book has to be less than 10,000 words
    
    Book has to take less than 50 hours to read
    """
    total_est = estimated_time_to_read(report)
    if(count_words(report) >= 10000 and total_est <= 50):
        return f"This would be a great book for you to read because it is more than 10,000 words and takes {total_est} hours to read"
    else:
        return f"This would not be a good book for you to read because it is {count_words(report)} words long and takes {total_est} hours to read, well above your preferred time!"

def report(book):
    print(f"-- Report of books/frankenstein.txt --")
    #count words
    num_words = count_words(book)
    print(f"\n Total words: {num_words} words found in the document!")
    
    #count letters
    total_letters = count_letters(book)
    total_letters_sorted = chars_dict_to_sorted_list(total_letters)
    print("\n-- Individual letters found in report --")
    for item in total_letters_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")


    #print(total_letters)
    print("-- Final Thoughts --\n")
    print(is_this_for_you(book))
    print("-- End report --")


main()