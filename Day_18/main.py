import turtle as turtle_module
import random
# import colorgram
#
# rgb_colors =[]
# colors = colorgram.extract('Image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append((new_color))
#
# print(rgb_colors)

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(251, 250, 247), (241, 242, 246), (230, 216, 101), (238, 248, 245), (153, 80, 40), (246, 235, 240),
            (208, 158, 103), (178, 176, 19), (109, 165, 210), (27, 90, 159), (107, 176, 124), (194, 91, 106),
            (14, 36, 97), (71, 44, 25), (51, 120, 24), (184, 128, 149), (95, 192, 47), (106, 33, 56), (195, 91, 72),
            (100, 120, 170), (26, 97, 24), (25, 53, 110), (180, 206, 171), (250, 170, 165), (249, 170, 173),
            (148, 192, 244), (103, 59, 19), (89, 28, 48), (135, 77, 90), (19, 74, 105)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
