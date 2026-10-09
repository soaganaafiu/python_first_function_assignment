

numberOne = int(input("Enter first number: "))
numberTwo = int(input("Enter first number: "))



def maximumNumber(numberOne, numberTwo):

    largest = numberOne;

    if (numberTwo > largest):
        largest = numberTwo;

    return largest;



def isEven(numberOne):

    if (numberOne % 2 == 0):

        return True 

    return False




def primeNumber(numberOne):

    if(numberOne < 2):

        return False


    for count in range (2, numberOne):

        if (numberOne % count == 0):

            return False


        return True




def subraction(numberOne, numberTwo):
    if (numberOne > numberTwo):
        return numberOne - numberTwo

    return numberTwo - numberOne



def division(numberOne, numberTwo):
    if(numberTwo == 0):

        return 0.0

    return numberOne / numberTwo





def squareOf(numberOne):

    return numberOne * numberOne






def factorialOf(numberOne):

    multiply = 1;

    for count in range(1,numberOne):

        multiply = multiply * count

    return multiply





def factorOf(numberOne):

    add = 0

    for count in range (1, numberOne):

        if(numberOne % count == 0):

            add = add + 1

            return add;
       





def isPerfectSquare(numberOne):

    for count in range (1, numberOne):

        if(count * count == numberOne):

            return True

        return False





def isPalindrome(numberOne):

    reversed = 0

    while numberOne > 0:

        digit = numberOne % 10

        reversed = reversed * 10 + digit

        numberOne = numberOne / 10



    if (reversed == numberOne):

        return True;

    return False;





 



largestNumber = maximumNumber(numberOne, numberTwo)
print("Largest: ", largestNumber)

answer = isEven(numberOne)
print("This is Even: ", answer)


primeCheck = primeNumber(numberOne)
print("This is a Prime Number: ", primeCheck)


subtract = subraction(numberOne, numberTwo)
print("This is the subtraction of two number: ", subtract)



divide = division(numberOne, numberTwo)
print("This is division: ", divide)


factorial = factorialOf(numberOne)
print("The factorial of number one is: " , factorial)


factor = factorOf(numberOne)
print("The factor of number one is: " , factor)


square = isPerfectSquare(numberOne)
print("Is this a perfect square: " ,square)


palindrome = isPalindrome(numberOne)
print("Is this a palindrome: " , palindrome )
