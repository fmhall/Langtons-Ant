from multipleAnts import *
from PIL import Image

curfolder = "test1/"
iterations = 100
print("Launching test now.\nFiles will be saved in the {} folder".format(curfolder))
for i in range(iterations + 1):
    curfile = curfolder + "eps/" + str(i) + ".eps"
    board = langtons(duration=500, filename=curfile)
    board.addAnt(0, 0)
    board.addAnt(0, i)
    print("Generating board {0}/{1}...".format(str(i), iterations))
    board.main()

    im = Image.open(curfile)
    im.save(curfolder + "pngs/" + str(i) + ".png", "PNG")
