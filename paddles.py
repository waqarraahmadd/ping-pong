from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        # self.resizemode("auto")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setx(x_cor)

    def up(self):
        if self.ycor() > 300:
            pass
        else:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() < -300:
            pass
        else:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)


