import time
from random import randint
from turtle import Turtle
laura = Turtle()
laura.color('red')
laura.shape('turtle')
rik = Turtle()
rik.color('green')
rik.shape('turtle')
lauren = Turtle()
lauren.color('blue')
lauren.shape('turtle')
carrieanne = Turtle()
carrieanne.color('yellow')
carrieanne.shape('turtle')
laura.goto(-200,75)
rik.goto(-200,25)
lauren.goto(-200,-25)
carrieanne.goto(-200,-75)
for movement in range(30):
    laura.forward(randint(10,50))
    rik.forward(randint(1,5))
    lauren.forward(randint(1,5))
    carrieanne.forward(randint(1,5))