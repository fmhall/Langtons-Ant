import turtle
import tkinter


class langtons:
    def __init__(self, id=1, ants=[], speed=0, duration="inf", filename=""):
        self.ants = ants
        self.maps = {}
        self.speed = speed
        self.duration = duration
        self.saveto = filename
        self.id = id

    # def reset(self):

    def addAnt(self, xcor, ycor):
        ant = turtle.Turtle()
        ant.shape("square")
        ant.shapesize(0.5)
        ant.speed(self.speed)
        ant.setpos(xcor, ycor)
        self.ants.append(ant)

    def listAnts():
        print(self.ants)

    def main(self):

        window = turtle.Screen()
        window.bgcolor("white")
        window.screensize(1000, 1000)

        flag = True

        if self.duration == "inf":
            while True:
                if self.saveto != "":
                    ts = turtle.getscreen()
                    ts.getcanvas().postscript(file=self.saveto)

                steps = 10
                for ant in self.ants:
                    pos = coordinate(ant)
                    if pos not in self.maps or self.maps[pos] == "white":

                        ant.fillcolor("black")
                        ant.stamp()
                        invert(self.maps, ant, "black")
                        ant.right(90)

                    elif self.maps[pos] == "black":
                        ant.fillcolor("white")
                        ant.stamp()
                        invert(self.maps, ant, "white")
                        ant.left(90)

                    ant.forward(steps)
        else:
            while self.duration > 0:
                if self.saveto != "":
                    ts = turtle.getscreen()
                    ts.getcanvas().postscript(file=self.saveto)

                steps = 10
                for ant in self.ants:
                    pos = coordinate(ant)
                    if pos not in self.maps or self.maps[pos] == "white":

                        ant.fillcolor("black")
                        ant.stamp()
                        invert(self.maps, ant, "black")
                        ant.right(90)

                    elif self.maps[pos] == "black":
                        ant.fillcolor("white")
                        ant.stamp()
                        invert(self.maps, ant, "white")
                        ant.left(90)

                    ant.forward(steps)
                self.duration -= 1

        for t in self.ants:
            t.reset()
        for t in window.turtles():
            t.reset()
        self.ants = []
        self.maps = {}

        turtle.clearscreen()


def invert(graph, ant, color):
    graph[coordinate(ant)] = color


def coordinate(ant):
    if ant:
        return (round(ant.xcor()), round(ant.ycor()))
    else:
        print("error")
        return None


if __name__ == "__main__":
    langtons()
