def alphabet_position(text):
    ''' alphabet_position returns a space separated string containing the 
    numerical position of alpha numeric characters in a given string. '''
    return " ".join([str(ord(c)&31) for c in text if c.isalpha()])
