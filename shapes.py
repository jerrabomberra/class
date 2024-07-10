from turtle import Turtle, Screen

turtle = Turtle()


class Polygon:
    def __init__(self, sides, name, size=100, color="red", line_thickness=5) -> None:
        self.sides = sides
        self.line_thickness = line_thickness
        self.name = name
        self.size = size
        self.color = color
        self.interior_angles = (self.sides - 2) * 180
        self.angle = 180 - self.interior_angles / self.sides

    def draw(self):
        for i in range(self.sides):
            turtle.width(self.line_thickness)
            turtle.color(self.color)
            turtle.forward(self.size)
            turtle.right(self.angle)
        turtle


square = Polygon(4, "Square", 200, "red", 20)
pentagon = Polygon(5, "Pentagon")
hexagon = Polygon(6, "Hexagon")

hexagon.draw()
# pentagon.draw()
# square.draw()
# tim.home()

print(pentagon.angle)

screen = Screen()
screen.exitonclick()
