import turtle
import pandas as pd

def main():

    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.setup(width=700, height=700)
    image = f".\\Day25\\us-states-game-start\\blank_states_img.gif"

    #new method to add turtle object shape 
    screen.addshape(image)

    turtle.shape(image)

    #def get_mouse_click_coor(x, y):
    #    print(x, y)

    # on screen click, print the x and y coordinates
    #turtle.onscreenclick(get_mouse_click_coor)

    try:
        data = pd.read_csv(f".\\Day25\\us-states-game-start\\50_states.csv")
        # filter by attribute
        print(data.state)
        print(type(data.state))
        # filter by column
        print(data['state'])
        # Data type - Series
        print(type(data['state']))
        # convert series to a list
        all_states = data.state.to_list()
        print(all_states)
        print(type(all_states))

        guessed_states = []
        states_to_learn_dict={}
        #missing_states = []

        while len(guessed_states) < 50:
            answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                            prompt="What's another state's name?").title()
            #print(answer_state)
            # it will convert to first letter of the word as capital letter
            if answer_state == 'Exit':

                states_to_learn = [state for state in all_states if state not in guessed_states]
                for index, element in enumerate(states_to_learn):
                    states_to_learn_dict[str(index)] = [element]
                print(states_to_learn_dict)
                data_dict = pd.DataFrame(states_to_learn_dict)
                data_dict_transposed = data_dict.transpose()
                print(data_dict_transposed)
                data_dict_transposed.to_csv(f".\\Day25\\us-states-game-start\\states_to_learn.csv")

                #for state in all_states:
                #    if state not in guessed_states:
                #        missing_states.append(state)
                #new_data = pd.DataFrame(missing_states)
                #new_data.to_csv(f".\\Day25\\us-states-game-start\\states_to_learn.csv")
                break

            if answer_state in all_states:
                guessed_states.append(answer_state)
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                # filter when data.state = input of the guessed state
                state_data = data[data.state == answer_state]
                # iloc works by getting or set the value(s) of the specified indexes
                t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
                t.write(answer_state)

                # states_to_learn.csv

    except Exception as e: 
        print(e)

    #answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name? ")
    ## This prints the output
    #print(answer_state)

    #turtle.mainloop()

    # alternative to turtle.mainloop() which will keep screen open, but it should not exit on click
    #screen.exitonclick()

    

if __name__ == "__main__":
    main()