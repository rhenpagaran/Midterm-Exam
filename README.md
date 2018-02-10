# Midterm-Exam
#Rhina G. Pagaran

def match_a():
    print ("Function match_a() \n")

    rgp1 = input ("Enter 1st input:")
    rgp2 = input ("Enter 2nd input:")
    rgp3 = input ("Enter 3rd input:")

    rgp22 = []
    rgp33 = []
    rgp11 = []

    
    for i in rgp1:
        if len(i) != 1:      #exclude character
            if i == i[::-1]: #Palindrome checker
                rgp11.append(i)

    for i in rgp2:
        if len(i) != 1:      #exclude character
            if i == i[::-1]: #Palindrome checker
                rgp22.append(i)

    for i in rgp3:
        if len(i) != 1:      #exclude character
            if i == i[::-1]: #Palindrome checker
                rgp33.append(i)

    print "1st output: ",len(rgp11)
    print "2nd output: ",len(rgp22)
    print "3rd output: ",len(rgp33)

match_a()
print ("\n\n")


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

