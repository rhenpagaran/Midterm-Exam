#Rhina G. Pagaran
#Midterm Exam

def front_x():
    print ("Function front_x()\n")

    rgp1 = input ("Enter 1st input:")
    rgp2 = input ("Enter 2nd input:")
    rgp3 = input ("Enter 3rd input:")

    rgp11 = []
    rgp111 = []
    rgp22 = []
    rgp222 = []
    rgp33 =[]
    rgp333 = []

    for i in rgp1:
        if i.startswith('x'): #new list of strings that starts with 'x' from others
            rgp11.append(i)
        else:
            rgp111.append(i) #new list of other strings
            
    print "1st output: ",sorted(rgp11) + sorted(rgp111) #to alphabetically arranged


    for i in rgp2:
        if i.startswith('x'): #new list of strings that starts with 'x' from others
            rgp22.append(i)
        else:
            rgp222.append(i) #new list of other strings
            
    print "2nd output: ",sorted(rgp22) + sorted(rgp222) #to alphabetically arranged


    for i in rgp3:
        if i.startswith('x'): #new list of strings that starts with 'x' from others
            rgp33.append(i)
        else:
            rgp333.append(i) #new list of other strings
            
    print "3rd output: ",sorted(rgp33) + sorted(rgp333) #to alphabetically arranged

    
front_x()
