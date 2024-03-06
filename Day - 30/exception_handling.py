try:
    file = open("new_file.txt")
    file.read()
    my_dict = {'one':1,'two':2}
    print(my_dict['three'])
except FileNotFoundError:
    file = open("new_file.txt", 'w')
    file.write("Content")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")