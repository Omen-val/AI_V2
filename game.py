def game():
    import random

    num = random.randint(0, 20000)
    tries = 0
    found = False

    while not found:
        try:
            gues = int(input("Your Guess: "))
            tries +=1
            if gues == num:
                found = True
                print(f"You found the number after {num} after {tries} tries")

            elif gues > num:
                print(f"The number is less than {gues}")

            else:
                print(f"The number is greater that {gues}")
        except Exception as e:
            print("Please Enter a number!")