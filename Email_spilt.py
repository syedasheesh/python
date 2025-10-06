# Slice Email
# Collect eamil from use 
# Split the email using the @, the first part as 

#hello@codewithsyed.com

def main():
    print('Welcome to the email Slicer')
    print('')
    
    email_input = input('Input you email address: ')
    (username, domain) = email_input.split('@')
    (domain, extension) = domain.split('.')
    
    print('Username : ', username)
    print('Domain : ', domain)
    print('Extension : ', extension)
while True:
    main()
