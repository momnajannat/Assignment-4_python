# question1
# add function 
def add(x, y):
    return x + y

# subtracts function
def subtract(x, y):
    return x - y

#  multiplication function
def multiply(x, y):
    return x * y

#  division function
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # user input on run time
    choice = input("press 1. for add , 2. for substract, 3. for multiplication, 3.divsion")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
       
        next_calculation = input("Enter your choice  if you want: ")
        if next_calculation == "no":
          break
    
    else:
        print("Dont Enter Correctly")

        #question 2
        list = ["momna", 21, 4, "jannat"] 
for x in list: 
    if type(x) == int: 
        print(x)

#question3
key1=int(input("Enter the key (int) to be added:"))
value1=input("Enter the value for the key to be added:")
d={}
d.update({key1:value1})
print("Updated dictionary is:")
print(d)

#question4
dictionary_momna = {'dict1':200,'dict2':300,'dict3':-50}
print(sum(dictionary_momna.values()))

#question5
def duplicate(l1):
    n=len(l1)
    dup=[]
    for i in range(n):
        k = i + 1
        for j in range(k,n):
            if l1[i] == li[j] and l1[i] not in dup:
                dup.append(l1[i])
    return dup

l1=[ 10, 20, 50, -50, -60, 50, 80, -50, -60, 90]
print("Duplicate items in list are: ",duplicate(l1))



#question6:
def duplicate(l1):
    n=len(l1)
    dup=[]
    for i in range(n):
        k = i + 1
        for j in range(k,n):
            if l1[i] == l1[j] and l1[i] not in dup:
                dup.append(l1[i])
    return dup


l1=[ 10, 20, 50, -50, -60, 50, 80, -50, -60, 90]
print("Duplicate items in list are: ",duplicate(l1))