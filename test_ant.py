from ant import Ant
import turtle

ant1 = Ant()
window = turtle.Screen()
window.bgcolor('white')
window.screensize(1000, 1000)
maps = {}

while True:
    ant1.move(maps)

