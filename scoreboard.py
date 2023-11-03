from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_player_score = 0
        self.l_player_score = 0
        self.update_score()

    def point_r(self):
        self.r_player_score += 1

    def point_l(self):
        self.l_player_score += 1

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_player_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_player_score, align="center", font=("Courier", 80, "normal"))

