print("Welcome to the ride!")
height = int(input("What is your height in cm?: "))
bill = 0


if height > 120:
    print("You can ride.")
    age = int(input("What is your age?: "))
    if age < 12:
        bill = 5
        print(f"Your bill is: ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Your bill is: ${bill}")
    elif 45 <= age <= 55:
        bill = 0
        print("Free ride on us.")
    else:
        bill = 12
        print(f"Your bill is: ${bill}")
    photo = input("Do you want a photo for $3? y or n. ").lower()
    if photo == "y":
        bill += 3
    print(f"Your final bill is: ${bill}")
else:
    print("Sorry, you are too short to ride.")