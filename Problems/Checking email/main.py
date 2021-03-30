def check_email(string):
    if ' ' not in string \
            and string.find('@') != -1 \
            and string.find('.', string.find('@')) != string.find('@') + 1 \
            and string.find('.', string.find('@') + 1) != - 1:
        return True
    else:
        return False
