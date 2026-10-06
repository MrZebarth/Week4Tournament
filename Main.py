#############################################
# Name: Mr Zebarth
# Class: ICS3C
# Date: Friday Sept. 25
# Project Name: Week4Tournament
#
# Project Description: See the README file
#############################################

# THIS IS WHERE YOU CODE
full_dot = '●'
empty_dot = '○'

def create_character(name,strength,intelligence,charisma):
    if not isinstance(name,str):
        return "The character name should be a string"
    if name=="":
        return "The character should have a name"
    if len(name)>10:
        return "The character name is too long"
    if name.find(" ")>-1:
        return "The character name should not contain spaces"
    if not isinstance(strength,int) or not isinstance(intelligence,int) or not isinstance(charisma,int):
        return "All stats should be integers"
    if strength<1 or intelligence<1 or charisma<1:
        return "All stats should be no less than 1"
    if strength>4 or intelligence>4 or charisma>4:
        return "All stats should be no more than 4"
    if strength+intelligence+charisma!=7:
        return "The character should start with 7 points"

    output=f"{name}\n"
    output+="STR "
    for i in range(strength):
        output+=full_dot
    for i in range(10-strength):
        output+=empty_dot
    output+="\nINT "
    for i in range(intelligence):
        output+=full_dot
    for i in range(10-intelligence):
        output+=empty_dot
    output+="\nCHA "
    for i in range(charisma):
        output+=full_dot
    for i in range(10-charisma):
        output+=empty_dot
    return output

print(create_character("ren",4,2,1))
