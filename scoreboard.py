from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()
