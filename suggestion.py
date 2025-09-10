snack = input("What is your favorite snack? ").lower() # Convert input to lowercase
print(f"You ordered : {snack}")
if snack == "tea" or snack == "sutta":
    print("You are a person of good taste")
else:
    print("NOT FOUND")