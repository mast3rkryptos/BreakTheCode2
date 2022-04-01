import turtle

phrase = "LASERLIGHTOFAMILLIONUSES"
phrase = "LASER"
rotateTurtle = True
lookup = {'A': (3, 1, 0),
          'B': (-1, 2, 3),
          'C': (-1, 2, 3),
          'D': (-1, 2, 3),
          'E': (4, 1, 1),
          'F': (3, 2, 3),
          'G': (-1, 2, 3),
          'H': (3, 2, 3),
          'I': (3, 2, 3),
          'J': (-1, 2, 3),
          'K': (3, 2, 3),
          'L': (2, 1, 0),
          'M': (4, 2, 3),
          'N': (3, 2, 3),
          'O': (-1, 2, 3),
          'P': (-1, 2, 3),
          'Q': (-1, 2, 3),
          'R': (-1, 1, 1),
          'S': (-1, 2, 3),
          'T': (2, 2, 3),
          'U': (-1, 2, 3),
          'V': (2, 2, 3),
          'W': (4, 2, 3),
          'X': (2, 2, 3),
          'Y': (3, 2, 3),
          'Z': (3, 2, 3)}

t = turtle.Turtle()


def f(letter):
    dirLeft = True
    if lookup[letter][2] == 0:
        dirLeft = False

    if letter == "S":
        return

    t.setheading(90) # North

    distance = 10 * lookup[letter][1]
    if 2 <= lookup[letter][0] <= 3:
        t.forward(distance)
        t.left(90) if dirLeft else t.right(90)
        t.forward(2 * distance)
        t.left(90) if dirLeft else t.right(90)
        t.forward(distance)
        t.left(90) if not dirLeft else t.right(90)
        t.forward(distance)
        t.left(90) if dirLeft else t.right(90)
        t.forward(2 * distance)
        t.left(90) if dirLeft else t.right(90)
        t.forward(distance)
        t.left(90) if not dirLeft else t.right(90)
        t.forward(distance)
    else:
        t.forward(distance)
        t.left(90) if dirLeft else t.right(90)
        t.forward(distance)
        t.left(90) if not dirLeft else t.right(90)
        t.forward(distance)
        t.left(90) if dirLeft else t.right(90)
        t.forward(distance)
        t.left(90) if not dirLeft else t.right(90)
        t.forward(distance)


for letter in phrase:
    f(letter)
turtle.done()
