from turtle import *
import turtle as tu
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
tu.getcanvas().postscript(file='blume.ps')
done()
