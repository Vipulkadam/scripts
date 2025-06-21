


#
# list = [2,3,4,5,6]
#
#
#
# string = "name123"



def diff_char_str(string):

    character = []

    number = []

    for char in string:
        if char.isalpha:
            character.append(char)
        else:
            number.append(char)

    return character

string = "name123"

diff_char_str(string)

