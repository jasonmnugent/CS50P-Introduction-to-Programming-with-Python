def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# creating a function, similar to how "input()" is a function
def dollars_to_float(amount):
    """
    Convert a dollar amount formatted as $##.## to a float.

    Parameters:
    amount (str): The dollar amount formatted as $##.##.

    Returns:
    float: The dollar amount as a float.
    """
    return float(amount.replace("$", ""))


def percent_to_float(percent):
    """
    Convert a percentage formatted as ##% to a float.

    Parameters:
    percent (str): The percentage formatted as ##%.

    Returns:
    float: The percentage as a float.
    """
    return float(percent.replace("%", "")) / 100

# Convert a dollar amount to a float
result1 = dollars_to_float("$50.00")

# Convert a percentage to a float
result2 = percent_to_float("15%")

# Print the results
print(result1) # 50.0
print(result2) # 0.15

# call the function
main()