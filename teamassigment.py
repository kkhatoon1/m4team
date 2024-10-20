options = (
  "1. Go to school",
  "2. Play video games",
  "3. Make Breakfast",
  "4. Go to the gym",
  "5. Take care of sibling",
  "0. Exit")

def output_options():
  print ("What option will you be choosing:")
  for option in options:
    print (option)

def main():
  while True:
    output_options()

    answer = input("Choose and enter the number of your choice:")

    if answer == "1":
     print ("You are going to school")
    elif answer == "2":
      print("Nice! you are going to playing video games")
    elif answer == "3":
      print("Your hungry lets make breakfast")
    elif answer == "4":
      print("Lets go to the gym")
    elif answer == "5":
      print("Lets go take care of your sibling")
    elif answer == "0"
       print("you are leaving bye!)
       break
    else:
      print("Invalid input try again please")

if _name_ == "_main_"
   main()
