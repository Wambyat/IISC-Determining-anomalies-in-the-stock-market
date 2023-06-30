def remove_special_characters(string):
    special_characters = ['.com','.org','.net','.edu','.gov','Inc','Corp',',','.','!']
    for i in special_characters:
        string = string.replace(i,'')
    return string
