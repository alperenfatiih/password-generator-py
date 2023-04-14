import random
lenghtInput= int(input("Password Length: "))
passwordInput= int(input("How Many Passwords: "))
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "&<>{}@$/=""}"
i=0
print("your password is : ")
while i < passwordInput :

        i=i+1
        if i == passwordInput+1:
            break
        use_for = lower_case + upper_case + numbers + symbols
        length_for_pass = lenghtInput
        password = "".join(random.sample(use_for,length_for_pass))
        print(password)       
                    
               