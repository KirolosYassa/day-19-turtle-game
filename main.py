from turtles_race import *


def ask_for_bet():
    user_betting = screen.textinput(title="Bet your winner turtle", prompt=f"What color will the winner turtle be?\n {colors} ")
    # print(user_betting)
    return user_betting


def begin_race(is_race_onn):
    winner_winner = ""
    while is_race_onn:
        for player in turtles:
            random_steps = r.randint(0, max_steps)
            player.move(random_steps)
            if player.arrived():
                # print(f"Turtle {player.get_color()} has arrived!")
                winner_winner = player.get_color()
                is_race_onn = False
                break
    return winner_winner


is_race_on = False
screen = Screen()
screen.setup(width=width, height=height)
user_bet = ask_for_bet()

while user_bet not in colors:
    user_bet = ask_for_bet()

if user_bet in colors:
    generate_turtles()
    is_race_on = True
    winner = begin_race(is_race_on)
    if winner == user_bet:
        print(f"You win. The {winner} turtle is the winner")
    else:
        print(f"You lose. The {winner} turtle is the winner")

screen.exitonclick()
