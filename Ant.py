import turtle

class Ant:
    """
    instantiate a turtle.Turtle() as a single ant
    ant should contain all logic for an ant
    ant should be separate from other ants
    ant should be able to be instantiated and manipulated
    from the screen class
    """
    def __init__(self, shape="square", shapesize=0.5, speed=1000000, pos=(0,0), steps=10):
        self.ant = turtle.Turtle()
        self.set_ant_attributes(shape, shapesize, speed, pos)
        self.steps = steps

    def set_ant_attributes(self, shape="square", shapesize=0.5, speed=1000000, pos=(0,0)):
        self.ant.shape(shape)
        self.ant.shapesize(shapesize)
        self.ant.speed(speed)
        self.ant.setpos(pos)

    def move(self, map):

        if self.get_pos() not in map or map[self.get_pos()] == "white":

            self.ant.fillcolor("black")
            self.ant.stamp()
            invert(map, self.ant, "black")
            self.ant.right(90)

        elif map[self.get_pos()] == "black":
            self.ant.fillcolor("white")
            self.ant.stamp()
            invert(map, self.ant, "white")
            self.ant.left(90)

        self.ant.forward(self.steps)

    def get_pos(self):
        return coordinate(self.ant)


def invert(graph, ant, color):
    graph[coordinate(ant)] = color


def coordinate(ant):
    return round(ant.xcor()), round(ant.ycor())


ant1 = Ant(pos=(0, 1))
