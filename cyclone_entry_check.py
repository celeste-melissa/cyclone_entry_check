# Write code below 💖

# New entry system for "The Cyclone" must check user height and the amount of credits they have

# Get the user's height in feet
height = float(input("What is your height in feet? "))


# Converts the users height from feet to centimeters
def height_conversion(user_height):
  if 0 < user_height <= 12:
    return user_height * 30.48
  else:
    return 0

# Convert height and validate
converted_height = float(height_conversion(height))

if converted_height == 0:
    print("Invalid input. Please enter height in feet (e.g., 5.5).")
else:
    print("Height:", round(converted_height, 2), "cm")

#  Get the number of credits
credits = int(input("How many credit do you have? "))
print("Credits:", credits)

# Check users eligibility to ride
if converted_height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif credits >= 10 or converted_height < 137:
  print("You are not tall enough to ride.")
elif converted_height >= 137 or credits < 10:
  print("You don't have enough credits.")
else:
  print("You have not met either requirement.")
