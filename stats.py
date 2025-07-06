def count_words(text):
    split_text = text.split()
    return len(split_text)
def count_letters(text):
    letters_dict = {}
    for letter in text:
        if letter.lower() in letters_dict:
            letters_dict[letter.lower()] += 1
        elif letter.isalpha() :
            letters_dict[letter.lower()] = 1
    return letters_dict
def listed_letters(text):
    num_list = []
    for key in text:
        num = text[key]
        num_list.append({"char" : key, "num" : num})
    return num_list
#def main():
#    d = "d"
#    print(d.isalpha())
#main()