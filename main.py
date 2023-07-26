import turtle
import pandas
screen = turtle.Screen()
title = screen.title("US-STATES-GAME")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# to get x and y co-ordinates of the state
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []
score = 0
while len(guessed_state) < 50:
    answer_state = turtle.textinput(title=f"SCORE:{score}/50", prompt="what's the next state")
    state = answer_state.title()
    if state == 'Exit' :
        break
    if state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == state]

        t.goto(int(state_data.x), int(state_data.y))
        t.write(state)
        all_states.remove(state)

        guessed_state.append(state)

        score += 1

states_to_learn = all_states.copy()
states_to_learn_data = pandas.DataFrame(states_to_learn)
states_to_learn_data.to_csv("states_to_learn.csv")




















































# with open("weather_data.csv") as data_file:
#     data=data_file.readlines()
#     print(data)
# import csv
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperature=[]
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# #CREATING DATA FRAME
# data = pandas.read_csv('weather_data.csv')
# #TO GET THE DETAILS OF THE ROW
# monday=data[data.day == "Monday"]
# print((monday.temp * 1.8) + 32 )
#CREATING DATAFRAME FROM SCRATCH
# data_dictionary={
#     "name":['dhoni','kohli','rohit'],
#     "highest_score_in_odi":[183,183,264]
# }
# data=pandas.DataFrame(data_dictionary)
# data.to_csv("new_data.csv")



