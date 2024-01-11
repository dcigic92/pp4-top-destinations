#Function to capitalize Country names

def custom_title_function(string):
    words = string.split()
    title_words = [word.capitalize() if word.lower() != 'and' else word for word in words]
    result = ' '.join(title_words)
    return result