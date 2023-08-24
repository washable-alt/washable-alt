from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score_to_game()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        self.reset()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.write_high_score_to_file()
        self.score = 0
        self.update_scoreboard()
        

    #def game_over(self):
        # self.goto(0,0)
        # self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        #self.clear()
        self.update_scoreboard()

    def write_high_score_to_file(self):
        # Relative path
        with open( '.\\highscore.txt', 'w') as f:
            f.write(str(self.high_score))

    def read_high_score_to_game(self):
        with open('.\\highscore.txt', 'r') as f:
            self.high_score = int(f.read())
        return self.high_score
    