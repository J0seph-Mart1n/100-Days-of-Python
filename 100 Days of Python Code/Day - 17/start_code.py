class User:

    def __init__(self,roll_no,name):
        self.roll_no = roll_no
        self.name = name

student = User(12,'Joseph')
print(student.roll_no)