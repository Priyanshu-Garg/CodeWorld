#This program Encripts and Decripts any message
def secret_code():
    k=1
    while k==1: #This condition is for the program to run endlessly
        
        l='ABCDEFGHIJKLMNOPQRSTUVWXYZab1cd2ef3gh4ij5kl6mn7op8qr9st0uvwxyz!@#$%^&*()' #This is the ultimate list of key
        a=0 #this is used for index tracking later in the program

        x=input('Enter 1 if you want to Encrypt and Enter 2 if you want to Decrypt') #'x' variable takes the input for encription or decryption
    
        if x=='1':
            Real_message=input('Enter the message')
            Fake_message=''
            for i in Real_message:
                a=0
                for j in l: #loop for the list values
                    a+=1
                    if i==j: #loop for the word values
                        Fake_message+=l[a+4] # all the letters are shifted 5 places in front using the list key.
                        
            
            print('The encrypted message is',Fake_message)
                
        
    
    
        elif x=='2': #Decryption
            Real_message=''
            Fake_message=input('Enter the message')
            for i in Fake_message:
                a=0
                for j in l: #loop for the list values
                    a+=1
                    if i==j: #loop for the word values
                        Real_message+=l[a-6] # all the letters are shifted 5 places before using the list key.
            print('The decripted message is',Real_message)
            
            
        else: #this condition is if the user enter any other value other than 0 and 1.
            print('The program has restarted')
        
secret_code() #the function is called

#Here the list key 'l' is used as the ultimate key for encrypting and decrypting

                
