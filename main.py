print("Welcome to the Love Calculator! \n")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1 + name2

lower_name = name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

first_number = t + r + u + e
second_number = l + o + v + e

love_percent = str(first_number) + str(second_number)
love_percent = int(love_percent)

if love_percent < 10 or love_percent > 90:
    print(f"Your score is {love_percent}, you go together like coke and mentos.")

elif love_percent >= 40 and love_percent <= 50:
    print(f"Your score is {love_percent}, you are alright together.")

elif love_percent > 100:
    love_percent = str(love_percent[0] + love_percent[1]) + str(love_percent [2] + love_percent[3])
    print(f"Your score is roundified to {love_percent}.")

else:
    print(f"Your score is {love_percent}.")
