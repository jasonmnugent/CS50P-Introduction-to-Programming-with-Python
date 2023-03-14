def main(text):
    """
    Replace :) with 🙂 and :( with 🙁 in a given string.

    Parameters:
    text (str): The input text to be converted.

    Returns:
    str: The converted text with :) replaced with 🙂 and :( replaced with 🙁.
    """

    # Replace :) with 🙂 and replace :( with 🙁
    text = input("Say something with a happy or sad face: ")
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")

    # Return the converted text
    return text

# Call the main (convert) function with a string argument and print it
result = main("Hello :) World :( !")
print(result)