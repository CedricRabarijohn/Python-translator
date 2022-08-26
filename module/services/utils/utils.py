from tokenize import String

def set_first_letter_upper_and_remove_spaces(text: String):
    str_list = list(text)
    if(str_list[0]==' '):
        str_list[0] = ''
        str_list[1] = str_list[1].upper()
    else:
        str_list[0] = str_list[0].upper()
    if(str_list[len(str_list)-1]==' '):
        str_list[len(str_list)-1] = ''
    return ''.join(str_list)