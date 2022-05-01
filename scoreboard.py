from turtle import Turtle,Screen
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.write(arg="scoreBoard", align="center")
        self.goto(0,270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score is : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game is over",align="center",font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


