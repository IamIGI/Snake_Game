from turtle import  Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__() #by using super you inherited all methods from class Turtle
        self.score = 0
        # self.shape("turtle")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.text = "Score : 0"
        self.write(arg=self.text, move=True, align="center", font=("Arial", 16, "normal"))

    def increase(self):
        self.score += 1
        self.text = f"Score: {self.score}"
        self.clear()
        self.goto(0, 270)
        self.write(arg=self.text, move=True, align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=True, align="center", font=("Arial", 16, "normal"))