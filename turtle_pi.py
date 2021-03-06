import turtle as tu

with open("pi.txt", "r") as f:
    pi = f.read()

lines = 100_000

tu.mode('logo')
tu.tracer(False)
tu.screensize(5000,5000, 'black')
tu.colormode(255)

for n in range(lines):
    color = int(n/(lines/255))
    tu.pencolor(255,225-120,color)
    zahl = int(pi[n])
    rotation = zahl * 36
    tu.setheading(rotation)
    tu.forward(5)
    if n % 10_000 == 0:
        tu.update()

tu.getcanvas().postscript(file='PI_bild.jpg')
tu.done()