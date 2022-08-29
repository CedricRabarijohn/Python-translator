from tokenize import String

def set_first_letter_upper_and_remove_spaces(text: String):
    # Remove useless spaces
    text = str(text).strip()
    # Convert the text to list
    str_list = list(text)
    # Set the first string of the sentence upper
    str_list[0] = str(str_list[0]).upper()
    return ''.join(str_list)