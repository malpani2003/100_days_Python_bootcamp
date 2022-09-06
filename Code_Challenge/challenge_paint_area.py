from math import ceil

def paint_cal(lenght,height,cover_area):
    can_require=(lenght*height)/cover_area
    return can_require
h=int(input("Enter height of wall "))
l=int(input("Enter length of wall "))
coverage=5
buy_can=ceil(paint_cal(l,h,coverage)) 
print(buy_can)
