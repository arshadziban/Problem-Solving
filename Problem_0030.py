def celebrate_eid(name):

    greeting = f"Eid Mubarak, {name}! May this blessed day bring peace, happiness, and prosperity to all. 💖✨"
    return greeting

user_name = input("Please enter your name: ")
message = celebrate_eid(user_name)
print(message)
