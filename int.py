print("Let's see how well you know me")
quit = False

print("\nNow lets try it using while True and break instead of variable")
while True:
    name = input("What is my name?: ")
    if(name == "Khaliah"):
        print("Yes thats me")
    age = input ("What is my age?: ")
    if(age == 16):
        print("Correct")

else:
    print("Your wrong")
    print("I'm done")
    break
