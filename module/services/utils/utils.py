from tokenize import String


def set_first_letter_upper(text: String):
    str_list = list(text)
    str_list[0] = str_list[0].upper()
    return ''.join(str_list)
    
print(set_first_letter_upper('bonjour'))