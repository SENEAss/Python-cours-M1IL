marks = []

while True:
    user_input = input("Enter a positif number : ")
    try:
        user_input = int(user_input)
    except ValueError:
            print("This is not a number", user_input)
    else:
        if user_input > 0:
            marks.append(user_input) 
        else:
            break

# The average
try:
    average = sum(marks)/len(marks)
except ZeroDivisionError:
    print("You can do this my man /0")
else:
    print("the marks are : ", marks)
    print(f'And the average is : {average:.2f}')
    
         