def alphabet_position(text):
    return " ".join([str(ord(c)&31) for c in text if c.isalpha()])
