seat_type=input("Enter the desired seat type : ").lower()
match seat_type:
    case "sleeper":
        print("You have chosen Sleeper class")
    case "ac":  
        print("You have chosen AC class")
    case "first class":
        print("You have chosen First class")
    case _:
        print("Invalid seat type")