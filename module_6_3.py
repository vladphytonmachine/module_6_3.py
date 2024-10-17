class Horse:
    def __init__(self ):   # конструктор обьектов класса
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx):    # метод класса для указания дистанции
        self.x_distance += dx

class Eagle:
    def __init__(self ):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):       # указание наследуемых классов

    def __init__(self ):
        super().__init__()    

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self ):
        return self.x_distance,self.y_distance

    def voice(self):
        print(self.sound)






p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(5 , 10)
print(p1.get_pos())
p1.voice()