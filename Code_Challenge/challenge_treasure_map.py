


row1=["$","$","$"]
row2=["$","$","$"]
row3=["$","$","$"]

map=[row1,row2,row3]
# print(map)
print(f"{row1}\n{row2}\n{row3}")

position=input("Enter the position in in this map: ")
column_num=int(position[0])
row_num=int(position[1])
# print(column_num,row_num)
map[row_num-1][column_num-1]="@"
print(f"{row1}\n{row2}\n{row3}")
