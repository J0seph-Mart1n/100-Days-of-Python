#add function using *args
# def add(*args):
#     total = 0
#     for n in args:
#         total+=n
#     print(total)
#
# add(1,2,3,4,5,6)

#add function using *kwargs
def add(n,**kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

add(4,add=5,multiply=3)

class Car:

    def __init__(self, **kwargs):
        self.model = kwargs.get('model')
        self.make = kwargs.get('make')
        self.colour = kwargs.get('colour')

new_car = Car(make='Audi', model='R8')
print(new_car.colour)