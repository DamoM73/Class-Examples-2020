import random

class Bubble:
    def __init__(self):
        self.speedx = random.randrange(-10,10)
        self.speedy = random.randrange(-10,10)

bubble1 = Bubble()
bubble2 = Bubble()

print(bubble1.speedx)
print(bubble2.speedx)