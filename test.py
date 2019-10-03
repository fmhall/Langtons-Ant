from multipleAnts import *
from PIL import Image

curfolder = "test1/"
iterations = 1
print("Launching test now.\nFiles will be saved in the {} folder".format(curfolder))


def makeImages(curfolder, iterations, i):
    curfile = curfolder + "eps/" + str(i) + ".eps"
    board = langtons(id=i, speed=2, duration=10, filename=curfile)
    board.addAnt(0, 0)
    # board.addAnt(0, i)
    print("Generating board {0}/{1}...".format(str(i), iterations))
    board.main()
    im = Image.open(curfile)
    im.save(curfolder + "pngs/" + str(i) + ".png", "PNG")


# for i in range(iterations + 1):
#     makeImages(curfolder, iterations, i)
makeImages(curfolder, iterations, 100)
makeImages(curfolder, iterations, 50)
