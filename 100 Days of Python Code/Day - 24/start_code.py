# file = open('my_file.txt')
# contents = file.read()
# print(contents)

with open("../../my_file.txt") as file:
    content = file.read()
    print(content)
