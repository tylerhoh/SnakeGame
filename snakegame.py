# Snake Game by Tyler Hoh
# Start: 6/11/19 end:6/12/19

# Part 1: building a frame
import turtle

window = turtle.Screen()
window.title("Snake Game by @Tlerhoh")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.tracer(0)//turns off screen updates

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#main game loop
while True:
    window.update()
window.mainloop()