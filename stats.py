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