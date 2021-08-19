#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Hfloat 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#Hfloat 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
total = int(input("what is the total price : "))
people = int(input("how many people you wannna split the bill with : "))
tip = int(input("what is the tip percentage you'll like to give 10 , 12 , 15? : "))
tip_percentage = float(tip / 100)
tip = float(total + float(total * tip/100))
tip_per_person = tip /people
print(f"each person has to give" , tip_per_person)