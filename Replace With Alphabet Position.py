def alphabet_position(text):
    text = text.lower()
    import string
    text_ = []
    #create a dictionary of letters and their positions
    letters = dict(zip(string.ascii_lowercase, range(1,27)))
    for i in text:
        if i  in letters:
            text_.append(str(letters[i]))
    return str(" ".join(text_))

print(alphabet_position("abc'"))
