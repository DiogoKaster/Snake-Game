from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            highest = int(file.read())
            self.high_score = highest
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(x=0, y=280)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Arial", 12, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"Your final score is: {self.score}", align="center", font=("Arial", 12, "normal"))
    #     self.goto(0, -40)
    #     self.write("GAME OVER", align="center", font=("Arial", 12, "normal"))
