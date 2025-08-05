def get_word_count(text):
    return len(text.split())

def character_count(text):
    chars = {}
    for i in text:
        if i.lower() in chars.keys():
            chars[i.lower()] += 1
        else:
            chars[i.lower()] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort_by_count(characters):
    tmp_list = []
    for i in characters:
        tmp_list.append({"char": i, "num": characters[i]})
    tmp_list.sort(reverse=True, key=sort_on)
    return tmp_list