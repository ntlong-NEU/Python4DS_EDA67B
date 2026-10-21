def normalize(text):

    text_norm = text.lower()
    for char in {'.', '.','?',"*",'-'}:
        text_norm  = text_norm.replace(char,' ')
    return text_norm
def count_word(text, normlized = True):
    if normlized:
        text = normalize(text)
    words = text.split()
    fre_words = {} # = dict()
    for w in words:
        if w in fre_words:
            fre_words[w] += 1
        else: 
            fre_words[w] = 1
    return fre_words

Data = [1,2,23,3,4,2,3,42,3,2,3,42,3,234,234,234,23,54]

print('The module is imported!')