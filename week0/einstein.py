# Prompt the user for mass in kilograms (as an integer)
mass = int(input("Enter mass in kilograms: "))

# Calculate the equivalent number of Joules
c = 300000000 # speed of light in meters per second
energy = mass * c**2

# Print the result
print("The equivalent energy is:", energy, "Joules")