import pandas
import turtle
import tkinter.messagebox

data = pandas.read_csv('50_states.csv')

turtle.Screen().title('US States Game')
screen = turtle.Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
screen.setup(725, 491)
turtle.shape(image)

state_name = turtle.Turtle()
state_name.hideturtle()
state_name.penup()

state_lists = data.state.to_list()

tkinter.messagebox.showinfo(title="US States Game!", message="Try to Guess ALL 50 US STATES")

state_count = len(state_lists)
score = 0
while state_count > score:
    if score == 0:
        state_input = turtle.textinput(title='Guess a State', prompt='Type a State Name: ').title()
    else:
        state_input = turtle.textinput(title=f'Score: {score}/ {len(state_lists)}',
                                       prompt='Type another State Name: ').title()

    if state_input in state_lists:
        score += 1
        state_coord = data[data.state == state_input]
        x = state_coord.x.item()
        y = state_coord.y.item()

        state_name.setx(x)
        state_name.sety(y)

        state_name.write(arg=state_input, move=False, align='left', font=('Arial', 10, 'bold'))

if score == 50:
    tkinter.messagebox.showinfo(title="Congratulations", message="You've guessed all the State.")

turtle.mainloop()
