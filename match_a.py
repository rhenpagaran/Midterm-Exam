#Rhina G. Pagaran
#Midterm Exam

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
