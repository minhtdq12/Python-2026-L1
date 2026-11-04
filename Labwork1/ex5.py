color_list = ['black', 'yellow', 'orange', 'red', 'pink', 'blue']
user_fav_color = input("What is your favorite color? ")

if user_fav_color in color_list:
    idx = color_list.index(user_fav_color)
    print(f"Your color is at  index {idx} in my list")
else:
    print("sorry, I could not find your color")

