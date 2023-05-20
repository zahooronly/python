row1 = ['👻', '👻', '👻']
row2 = ['👻', '👻', '👻']
row3 = ['👻', '👻', '👻']
# row3 = ['👻', '👻', '🥸']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you wanna put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])
selectedRow = map[horizontal-1]
selectedRow[vertical-1] = "🥸'"
# print(map[vertical-1])
print(f"{row1}\n{row2}\n{row3}")
