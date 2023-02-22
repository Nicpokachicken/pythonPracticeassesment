# You will construct a program that presents the quiz to the user, checks the answer and gives some kind of feedback.
# Your program will ask the user for their age, as this productivity tool will only be suitable for ages 12-16.
# Your program will output a suitable advice.

print ("Hello, this is a productivity tool!")
age = int(input("What is your age? "))
if age >= 12 and age <= 16:
    print("you can use this tool :)")
else:
    print("you are not old/to old to use this tool")
    quit()

focus = input("what is it you want to accomplish? Wake up earlier, Not going on my phone in the morning, Sleep better. ")

if focus == "Wake up earlier":
    print("okay to wake up earlier you need to set alarms earlier. Okay your welcome come back soon, bye.")

if focus == "Not going on my phone in the morning":
    print("Dont have a phone or put it away in a cupboard to charge not near your bed. "
          "Okay your welcome come back soon, bye.")

if focus == "Sleep better":
    print("reading before bed helps to get a better/deeper sleep. Okay your welcome come back soon, bye. ")
#if focus = "wake up earlier":
