#Codsoft Internship
#Task - 3 Password Generator
#import random package to perform random operation
import random 
#import string package to perform string operation
import string

#function to perform generate password pass one parameter size_pass
def Password(size_pass): 
    #sentence contains ascii letters(&,%,#,/...),digits(1,2,3...)and punctuation(.,;'etc)
    sentences=string.ascii_letters+string.digits+string.punctuation
    #random keyword take the values randomly from sentences 
    password=''.join(random.choice(sentences)for password in range(size_pass))
    #return the password
    return password
#main function
if __name__ == "__main__": 
    #get a length of the password from user
    size_pass=int(input("Enter the length of the password you want :"))
    #check whether the user input in positive value(1,2,3,4,5..) or negative value(-1,-2,-3,-4...)
    if size_pass<0:
        print("size should be in positive integer...")
    else:
        #function password(sixe_pass) is stored in strong_pass
        strong_Pass=Password(size_pass)
        # print the strong _pass
        print("Generated  password is : ",strong_Pass)

  
    

