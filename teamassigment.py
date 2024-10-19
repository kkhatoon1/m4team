options = (
  "1. Go to school",
  "2. Play video games",
  "3. Make Breakfast",
  "4. Go to the gym",
  "5. Take care of sibling",
  "6. Exit")

def output_options():
  print ("What option will you be choosing:")
  for option in options:
    print (option)

def main():
  while True:
    output_options()

    option = input("Choose and enter the number of your choice:")

if option == "1":
   print ("You are going to school")
elif option == "2":
    print("Nice! you are going to playing video games")
elif option == "3":
    print("Your hungry lets make breakfast")
elif option == "4":
    print("Lets go to the gym")
elif option == "5":
    print("Lets go take care of your sibling")
  
