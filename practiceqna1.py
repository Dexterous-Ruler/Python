#question1
print("Hello, World! Welcome to Python.")

#question2
print("Twinkle, twinkle, little star,\nHow I wonder what you are!")

#question3
your_name = input("What is your name? ")
your_age =  int(input("What is your age? "))
your_height = float(input("What is your height in meters? "))

you_are_a_student = True

print(f"Your name is {your_name}, you are {your_age} years old , your height is {your_height} meters and it is {you_are_a_student} that you are a student.")   

#question4
num="45"
num_int=int(num)
num_int+=10
print(num_int)

#question5
a=input("Enter your favorite food: ")
print(f"Your favorite food is {a}. wow! I also like {a}.")

#question6
a= int(input("Enter a number: "))
b=int(input("Enter another number: "))
sum=a+b
print(f"The sum of {a} and {b} is {sum}.")  
diff=a-b
print(f"The difference between {a} and {b} is {diff}.")
product=a*b
print(f"The product of {a} and {b} is {product}.")
quotient=a/b
print(f"The quotient of {a} divided by {b} is {quotient}.")

#question7
print("Hello \"Python\" world!\nThis is a new line.\nAnd this is a tab ->\t<- after tab.")

#question8
a= int(input("Enter a number: "))
print(a**2)
print(a**3)

#question9
name="tanishq"
age=20
height=160.6
is_student=True
print("the name of the student is"+name+".She is"+str(age)+"years old.She is"+str(height)+"cm tall.It is"+str(is_student)+"that she is a student.")