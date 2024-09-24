def lab2Question1(word):
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise
    
    if word == word[::-1]:
        return True
    else:
        return False
    

def lab2Question2(number_val):
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number
    
    num1 = 0
    num2 = 1
    
    while num2 <= number_val:
        print(num1)
        new_num = num1 + num2
        num1 = num2   
        num2 = new_num
        
        if num2 > number_val:
            break
        return num1


def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.
    
    str1 = str()
    str2 = str()

    strcount = str1.count(str2)
    
    return strcount


def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list
    
    sum_list = []   
    
    if len(list1) == len(list2):
        list3 = zip(list1, list2)
        zip_list = list(list3)
        
        for i in range(0,len(zip_list)):
            sum_list.append(list1[i] + list2[i])
        return sum_list
    else:
        return []


def lab2Question5():
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 
    
    password = input("Enter password")
    isValidPassword(password)

    while True:
        if isValidPassword(password) == False:
            password = input("Re-enter password")
            isValidPassword(password)

        else:
            break
            return password


def isValidPassword(password):
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    
    password = ()
    
    if len(password) < 8:
        length = False
        print("Must be at least 8 characters")
            
    if not any(char.isupper() for char in password):
        print("Must contain at least 1 upper case letter")
        upper = False
            
    if not any(char.islower() for char in password):
        print("Must contain at least 1 lower case letter")
        lower = False
            
    if not any(char.isdigit() for char in password):
        print("Must contain at least 1 number")
        digit = False

    if length or upper or lower or digit == False:
        print("False")
