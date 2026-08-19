def number_guessing_game():

    import random           #library
    
    print("Welcome to number guess game")
    print("guess the number between 1-100")
    
    secret_no = random.randint(1,100)
    
    for i in range(1,8):
        try:                                                             #expcetional handling
            user_input = int(input("enter the number"))
            if user_input < 1 or user_input > 100:                        #nested if statement
                print("Invalid number !! enter number between 1-100 ")
            elif user_input > secret_no:
                print ("Your Number is greater than SN")
            elif user_input < secret_no:
                print("Your Number is lesser than SN")
            else:
                print("You have guess the crt number")
                break
        except ValueError:
            print("Your wrong !! , pls try the number between 1-100 ")
    
    if secret_no == user_input:
        print(f"You have guess the {secret_no} in {i} attempts")
    else:
        print("Sorry! , your trails is exceeded")