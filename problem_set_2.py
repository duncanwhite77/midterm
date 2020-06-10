"""
Exam #1 / Problem set #2.
Your job is to complete the definition of the function so that it achieves its indicated behavior.

Do not run this file directly.
Run the file named main.py if you want to try out the code in these functions.
"""

def take_order():
  """
  Imagine this function is a grilled cheese-making robot.  It takes customers' orders 
  by asking a series of questions and then prints them a grilled cheese based on their order.

  The required flow - inputs must be requested in this order:
  - Ask the user what kind of bread they would like.  Acceptable responses are 'rye' and 'pumpernickel'.
  - Ask the user whether they would like a spread on the bread.  Acceptable responses are 'yes', 'yeah', 'no', and 'nope'.
  - If the user wants a spread, ask whether they want butter or margarine.  Acceptable responses are 'butter' and 'margarine'.
  - If the user wants margarine, ask whether they want real cheese or vegan cheese.  Acceptable responses are 'real' and 'vegan'.
  - If the user wants real cheese, ask what type.  Acceptable responses are 'cheddar' and 'swiss'.
  - Ask the user whether they want a tomato slice.  Acceptable responses are 'yes', 'yeah', 'no', and 'nope'.

  Output requirements:
    - The printed output of the function must meet exactly the following requirements.

    - For a grilled cheese with vegan cheese, the output must follow the format in the following examples.
      Replace 'rye' with the appropriate bread type and spread that the user entered:
        "You ordered a vegan grilled cheese on rye." (i.e. with no tomato)
        "You ordered a vegan grilled cheese on rye, with a slice of tomato." (i.e. with tomato)

    - For a grilled cheese with real cheese, the output must follow the format in the following examples.
      Replace 'cheddar', 'rye' and 'margarine' with the appropriate cheese type, bread type and spread that the user entered:
        "You ordered a grilled cheese with cheddar on rye." (i.e. with no butter or margarine)
        "You ordered a grilled cheese with cheddar on rye, with a slice of tomato."  (i.e. with no butter or margarine, but with tomato)
        "You ordered a grilled cheese with cheddar on rye, spread with margarine." (i.e. with a spread of butter or margarine)
        "You ordered a grilled cheese with cheddar on rye, spread with margarine, with a slice of tomato." (i.e. with a spread of butter or margarine and tomato)
  """
  bread = input("What type of bread... (pumpernickle / rye): ")
  spread = input("Would you like a spread... (yes / yeah / no / nope): ")
  cheese = input("Would you like cheese, if so what type?: ")

  if spread == "yes" or "yeah":
    input("Would you like butter or margarine?")
    

    print("You ordered a grilled cheese with {} on {}.".format(cheese,bread)
    print("You ordered a grilled cheese with {} on {}.")
    print("You ordered a grilled cheese with {} on {}.")
    print("You ordered a grilled cheese with {} on {}.")
    
