#Eleanor Davis - eleanor.davis@centre.edu - Lab 14: Program Design & More File I/O

#def a function that will read my file
def read_file(filename):
    '''
    Purpose:
        read file
    Parameters:
        filename [str]
    Returns:
        l_names [list of strs] names in file
        l_prs [list of int] prs of each athlete
    '''
    #open my file
    fileopen = open(filename)

    #read the lines of my file
    l_lines = fileopen.readlines()

    #close the file
    fileopen.close()

    #create two empty lists for my names and prs
    l_names = []
    l_prs = []

    #clean up my lines a bit 
    for item in l_lines:
        stripped_item = item.strip() #'Pierce,3'
        l_new = stripped_item.split(',') # ['Pierce', '3']

        #append the names and the prs (ints) into their respective lists
        l_names.append(l_new[0])
        l_prs.append(int(l_new[1]))

    #return nice lists of names and prs for the athletes
    return l_names, l_prs

#define a function to (over)write my file
def write_file(s_filename, l_names, l_prs):
    '''
    Purpose:
        (over)write the file with the changes made from other functions
    Parameters:
        s_filename: [str] a string of the entire file contents
        l_names: [list] a list of the names from the file
        l_prs: [list] a list of the prs from the file
    Returns:
        none
    '''
    #open my file in write mode
    fo = open(s_filename, 'w')

    #format how I want to write my names and prs to my file
    for i in range(len(l_names)):
        fo.write(f'{l_names[i]},{l_prs[i]}\n')

    #close my file
    fo.close()

#define a function to insert a new athlete
def insert_athlete(name, pr):
    '''
    Purpose:
        insert an athlete's name and pr into the file
    Parameters:
        name: [str] the athlete's name (from user input)
        pr: [int] the athlete's pr (from user input)
    Returns:
        l_names: [list] an updated list of athletes' names 
        l_prs: [list] an updated list of athlete's prs
    '''
    #give my filename and read the file in order to have l_names and l_prs
    filename = "lab_14_220_yes.txt"
    l_names, l_prs = read_file(filename)

    #if the name is not already in the file, append the name to l_names and pr to l_prs
    if name not in l_names:
        l_names.append(name)
        l_prs.append(pr)

    #if the name is in the l_names already, tell the user the athlete is already in file
    else:
        print("This athlete is already in the file.")
    
    return l_names, l_prs

#define a function to delete an athlete
def delete_athlete(name):
    '''
    Purpose:
        delete both an athlete and their corresponding pr from the lists
        l_names and l_prs
    Parameters:
        name: [str] athlete name from user input
    Returns:
        l_names: [list] an updated list of athletes' names 
        l_prs: [list] an updated list of athlete's prs
    '''
    #give my filename and read the file in order to have l_names and l_prs
    filename = "lab_14_220_yes.txt"
    l_names, l_prs = read_file(filename)

    #assign my index to the index of name in l_names
    index = l_names.index(name)

    #delete the [index] in both l_names and l_prs
    del l_names[index]
    del l_prs[index]
    
    return l_names, l_prs


#define a funciton to update an athlete's pr
def update_athlete(name, pr):
    '''
    Purpose:
        given an athlete's name and a new pr, the function will do a few things
            1. double check and see if the athlete is in the roster
            2. check if the new pr is actually larger than their old pr
                    if the new > old, then the pr is updated
                    if new is not > old, then it tells the user they can't update this pr
    Parameters:
        name: [str] athlete name from user input
        pr: [int] athlete pr given from user
    Return:
        l_names: [list] an updated list of athletes' names 
        l_prs: [list] an updated list of athlete's prs                  
    '''
    #give my filename and read the file in order to have l_names and l_prs
    filename = "lab_14_220_yes.txt"
    l_names, l_prs = read_file(filename)

    #if the name is in l_names
    if name in l_names:
        
        #assign my index to the index of name in l_names
        index = l_names.index(name)

        #if the new pr is greater than the pr in l_prs
        if pr > l_prs[index]:
            #assign the pr in l_prs to equal the new pr
            l_prs[index] = pr

        #if the new pr is less than or equal to the old pr, tell the user
            #the athlete cannot be updated
        else:
            print("I can't update this PR")

    #if the name is not in the file, tell the user this
    else:
        print('This athlete is not in the file')

    return l_names, l_prs
            

#define a function to look up an athlete
def lookup_athlete(name):
    '''
    Purpose:
        Lookup an athlete from the file given their name. If the athlete
        is not in the database, it tells the user this
    Parameters:
        name: [str] athlete name given from
    Return:
        none
    '''
    #give my filename and read the file in order to have l_names and l_prs
    filename = "lab_14_220_yes.txt"
    l_names, l_prs = read_file(filename)

    #if the name is in l_names
    if name in l_names:
        
        #assign my index to the index of name in l_names
        index = l_names.index(name)

        #tell the user what the pr is of the name they inputed
        print("Their PR is", l_prs[index])

    #if the name is not in l_names
    else:
        #tell the user the name is not in the file
        print("This athlete is not in the file")
    
#define main function
def main():
    '''
    Purpose:
        Asks what action the user wants to do, then based on their answer
        the program preforms their preferred function. 
    Parameters:
        none
    Return:
        none
    '''
    #give file name
    filename = "lab_14_220_yes.txt"

    #welcome the user
    print("Welcome!")

    #give the user the actions of the program
    print("1. Insert an athlete into file")
    print("2. Update an athlete's PR")
    print("3. Delete an athlete from the file")
    print("4. Lookup an athlete's PR")
    print("5. Quit the program")

    #ask the user what action they want to perform
    s_task = input("What action would you like to do?: ")

    #while the user hasn't asked to quit the program
    while s_task != '5':

        #if the user asked to complete action 1
        if s_task == '1': #insert athlete

            #ask user for name and pr of the athlete they want to insert
            name = input("Input athlete name: ")
            pr = int(input("Input athlete PR: "))

            #update l_names and l_prs with the inserted athlete
            l_names, l_prs = insert_athlete(name, pr)

            #write l_names and l_prs to the file
            write_ath = write_file(filename, l_names, l_prs)

            #give the user the actions of the program
            print("1. Insert an athlete into file")
            print("2. Update an athlete's PR")
            print("3. Delete an athlete from the file")
            print("4. Lookup an athlete's PR")
            print("5. Quit the program")
            
            #ask the user what action they want to perform
            s_task = input("What action would you like to do?: ")

        #if the user asked to complete action 2   
        elif s_task == '2': #update athlete

            #ask user for name and pr of the athlete they want to update
            name = input("Input athlete name: ")
            pr = int(input("Input athlete PR: "))
            
            #update l_names and l_prs with the updated athlete
            l_names, l_prs = update_athlete(name, pr)

            #write l_names and l_prs to the file
            write_ath = write_file(filename, l_names, l_prs)

            #give the user the actions of the program
            print("1. Insert an athlete into file")
            print("2. Update an athlete's PR")
            print("3. Delete an athlete from the file")
            print("4. Lookup an athlete's PR")
            print("5. Quit the program")
            
            #ask the user what action they want to perform
            s_task = input("What action would you like to do?: ")

        #if the user asked to complete action 3   
        elif s_task == '3': #delete athlete

            #ask user for name of the athlete they want to delete
            name = input("Input athlete name: ")

            #update l_names and l_prs with the deleted athlete
            l_names, l_prs = delete_athlete(name)
            
            #write l_names and l_prs to the file
            write_ath = write_file(filename, l_names, l_prs)

            #give the user the actions of the program
            print("1. Insert an athlete into file")
            print("2. Update an athlete's PR")
            print("3. Delete an athlete from the file")
            print("4. Lookup an athlete's PR")
            print("5. Quit the program")
    
            #ask the user what action they want to preform
            s_task = input("What action would you like to do?: ")

        #if the user wants to perform action 4
        elif s_task == '4': #lookup athlete
            
            #ask user for name of the athlete they want to lookup
            name = input("Input athlete name: ")

            #call function lookup_athlete(name) 
            lookup_athlete(name)

            #give the user the actions of the program
            print("1. Insert an athlete into file")
            print("2. Update an athlete's PR")
            print("3. Delete an athlete from the file")
            print("4. Lookup an athlete's PR")
            print("5. Quit the program")
            
            #ask the user what action they want to preform
            s_task = input("What action would you like to do?: ")

        #if the user inputed an invalid input
        else:

            #tell user to input options 1-5
            print("Please enter input for options 1 through 5.")

            #give the user the actions of the program
            print("1. Insert an athlete into file")
            print("2. Update an athlete's PR")
            print("3. Delete an athlete from the file")
            print("4. Lookup an athlete's PR")
            print("5. Quit the program")
            
            #ask the user what action they want to preform
            s_task = input("What action would you like to do?: ")

#call my main function
main()
