
email=input('Enter your email:')
password=input('Enter your password:')




def checker_email():
    checker=input('Enter your email to check:')
    
    
    if checker== email:
            print('Correct')
            return True
    else:
            
            return False


def checker_password():
    checker=input('Enter your password to check :')
    
    
    if checker== password:
            print('Correct')
            return True
    else:
            print('Not same')
            return False


def create_account():
    file2=open('account.txt','w')
    file2.write(f'Account: email:{email}/Password:{password}\n ')
    file2.close()



while True:
    
    
    if checker_email() :
        
        print('Login to your account, now enter your password')

    if checker_password():
        
        print('Ok!')
        create_account()
        print('Account created and saved!')
        break
    else:
        print('Not same')
        break
    
file = open("account.txt", "r")
lines = file.readlines()
file.close()
print(lines)         

print(f'your email is {email}')

