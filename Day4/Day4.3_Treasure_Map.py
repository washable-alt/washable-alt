first_row = ["⬜", "⬜", "⬜"]
second_row = ["⬛", "⬛", "⬛"]
third_row = ["🟥", "🟥", "🟥"]
map = [first_row, second_row, third_row]
print(f"{first_row}\n{second_row}\n{third_row}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]

#assign the treasure based on the row and horizontal value input
selected_row[horizontal - 1] = "X"

#Another way to do it would be using map[vertical - 1][horizontal - 1] = 'X'

print(f"{first_row}\n{second_row}\n{third_row}")