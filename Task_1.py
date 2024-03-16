# Codsoft Internship 
# Task-1  write a code for To_Do_List.. 
class To_do_list:
    # Built_ in_ function
    def __init__(self) :
        self.tasks=[]#Create Empty task
    # create function to add tasks
    def add_task(self,tasks): 
        task=input("Enter task:")# have a input from user
        self.tasks.append(task)# add the task in tasks using append method
        return f'added..' 
    # create a function to remove tasks  
    def Remove_task(self,tasks):
        if tasks==0:#check the tasks is Empty 
            print("Tasks is Empty") #print task is empty
        else:
            self.tasks.pop() # remove the tasks
        return f'removed'
    def Display(self,tasks): # function to display the tasks
        for i in self.tasks: # looping to print the tasks line by line
            print('-',i)
        return f'This will Increase Your productivity'
if __name__=="__main__": #main function
    s=To_do_list() # constructor 
    tasks=[] # an Empty list
    while True:
        print("1.Add Task")
        print("2.Remove Task")
        print("3.Display")
        print("4.Exit")
        option=int(input("Enter your option:"))  # have option from user
        
        if option == 1: # option for add task
            addtask=s.add_task(tasks)
            print(addtask)
        elif option==2: # option for remove tasks
            removetask=s.Remove_task(tasks)
            print(removetask)
        elif option == 3: #option  for display tasks
            list_out=s.Display(tasks) 
            print(list_out)
        elif option == 4: 
            print("Exiting")
            #break the loop 
            break
        else:
            # user enter any invalid input this messsage will appear
            print("Enter valid option") 
        