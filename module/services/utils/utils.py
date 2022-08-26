from tokenize import String

def set_first_letter_upper_and_remove_first_space(text: String):
    str_list = list(text)
    if(str_list[0]==' '):
        str_list[0] = ''
        str_list[1] = str_list[1].upper()
    else:
        str_list[0] = str_list[0].upper()
    return ''.join(str_list)