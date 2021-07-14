import turtle

# x = - 1
# y = - 1
turtle.speed(1)


# def cir(a):
#     for _ in range(8):
#         turtle.circle(45 * a, 100)
#         turtle.right(145)
def cir(a):
    for _ in range(8):
        turtle.circle(45, 100 + a)
        turtle.right(145)


for i in range(1, 1000):
    cir(i * 0.6)
    print(turtle.position())
    turtle.goto(x, y)
    x -= 1
    y -= 1

# def element():
#     turtle.forward(a)
#     turtle.right(145)
#     turtle.circle(45, 77.27)
#     turtle.right(145)
#     turtle.forward(a)
#     turtle.right(180)
#
# for i in range(1, 100000, 5):
#     element(100)
#
#
