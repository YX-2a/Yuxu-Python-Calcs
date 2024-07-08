def GCD (num1, num2):
    if num2 == 0 or num1 == 0:
        return 0
    elif  num2 ==  num1:
        return num1
    elif num1 > num2:
        
        return GCD(num1-num2, num2)
    elif num1 < num2:
        
        return GCD(num1, num2 - num1)
