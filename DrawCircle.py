import turtle
import time

npa_screen = turtle.Screen()

turtle.pensize(5)

# Bước 2: Vẽ hình tròn đơn giản
turtle.pensize(5)
turtle.pencolor ("red")
turtle.fillcolor ("blue")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
time.sleep(1)
turtle.clear()

# Bước 3: Tùy chỉnh màu sắc và kích thước của hình tròn
turtle.pencolor ("blue")
turtle.fillcolor ("red")
turtle.begin_fill()
turtle.circle(150)
turtle.end_fill()
time.sleep(1)
turtle.clear()

# Tùy chỉnh thay đổi điểm bắt đầu

turtle.screensize(1000,1000)
turtle.penup()
turtle.goto(-40, 120)
turtle.pendown()
turtle.pencolor ("red")
turtle.fillcolor ("red")
turtle.begin_fill()
turtle.circle(150)
turtle.end_fill()

turtle.done()
