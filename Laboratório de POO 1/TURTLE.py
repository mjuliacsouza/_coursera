from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(100)
    if abs(pos()) < 1:
        break
end_fill()
done()