import random
import time

responses = [
             "Yes", "most definitely!",
             "The chances are high!", "Not likely!", 
             "May the odds be ever in your favor.",
             "You got no shot, kid.", "Try it out and see!", 
             "Worth giving a shot", "99.9% success rate",
             "Congratulations, yes!", "Dumb Question", 
             "Ask again later", "Better not tell you now",
             "Cannot predict now", "Grab a drink and ask again later", 
             "Don't count on it"
            ]

choice = 'yes'
while (choice == "yes"):
  ques = input("Enter your Question: \n>>")
  for x in range(0, 8):
    print("Thinking" + "." * x, end="\r")
    time.sleep(0.5)

  print("Answer: ", random.choice(responses))
  choice = input("Do you want to continue? Type yes to continue\n>> ")
  if(choice != 'yes'):
    break