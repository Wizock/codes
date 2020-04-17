import random
import time

def run():
	
    g = 5
    n = random.randint(1, 30)
    x = input("Enter a number and take a guess :")
    while g > 1 :

        if x == n:
            print("good job you got it in "+g+" tries")

        if int(x) > n:
            g -= 1
            print("try a little lower")
            x = input("Enter a number and take a guess")

        if int(x) < n:
            g -= 1
            print("try a little higher")
            x = input("Enter a number and take a guess")

	if int g == 0:
	    print("unlucky , you are out of lives")
	    y = print("would you like to play again? ")

	    if y == "y" or "yes":
	        print("oh okay lets start again")
	        time.sleep(5)
	        run()
	        
	    if y == "n" or "no":
	        print("oh...")
	        time.sleep(3)
	        print("um...")
	        time.sleep(4)
	        print("well....")
	        time.sleep(3)
	        print("um")
	        time.sleep(4)
	        print("I guess ill see you later?...")
	        time.sleep(3)
	        print("good bye?")
                     
run()
