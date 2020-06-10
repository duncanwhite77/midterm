"""
Exam #1 / Problem set #1.
Your job is to complete the definitions of each function so that it achieves its indicated behavior.
Do not run this file directly... rather, run the file named main.py if you want to try out the code in these functions.
"""

def say_hello():
  """
  Asks the user to enter their name and prints out a greeting message.
  The printed output must follow exactly the format, "Hello, Sheila!\n", where 'Sheila' is replaced with whatever name the user enters.
  Remember that the print() function by default adds a line break to the end of each printed string.

  Requirements:
  - The first letter of the user's name must be capitalized in the output, even if the user entered it all lowercase.
  """
  # write your solution below this line.
  name = input('Enter your name: ')
  message = 'Hello, {}!'.format(name.capitalize())
  print(message)
  


def get_age():
  """
  Asks the user to enter their age and returns their response.

  Requirements:
  - If the age is valid (i.e. the user entered an integer), return the age as an int.
  - If the age is invalid (i.e. the user did not enter an integer), return False.

  :returns: The user's age, as an integer, if valid.  False otherwise.
  """
  # write your solution below this line.
  age = input("How old are you?: ")
  if age >= 0:
    return age
  else:
    return False



def to_dog_years():
  """
  Asks the user to enter their age and name, in that order, and then prints the user's age in dog years.

  The formula for calculating dog years: 
    1 human year = 7 dog years.

  Requirements:
  - The output must be in the exact format, "Hello, Sheila!\nYour dog age is 140!\n", where 'Sheila' and '140' are replaced with the data the user entered.
  - The part that asks for the user's age must be performed using the get_age() function defined above. 
  - The part that asks for the user's name and prints, "Hello, Sheila!\n", must be performed using the say_hello() function defined above.
  """
  # write your solution below this line.
  human_years = get_age()
  dog_years = human_years * 7

  say_hello() + print("\nYour dog age is {}!\n".format(dog_years))