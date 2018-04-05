def rectangle(turtle, x, y, width, height, color):
  turtle.penup()
  turtle.setx(x)
  turtle.sety(y)
  turtle.pendown()
  turtle.color(color, color)
  turtle.begin_fill()
  for i in range(2):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
  turtle.end_fill()
  
