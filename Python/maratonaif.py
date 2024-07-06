#1874
#temp=input()
#tempspl=temp.split(" ")
#a=int(tempspl[0])
#b=int(tempspl[1])
#c=int(tempspl[2])

#if(a>b and b<=c):
#    print(":)")

#elif(a<b and b>=c):
#    print(":(")

#elif(a<b and b<c):
#    ab=a-b
#    bc=b-c

#    if(ab<bc):
#        print(":(")

#    elif(ab>=bc):
#        print(":)")

#elif(a>b and b>c):
#    ab=a-b
#    bc=b-c

#    if(ab>bc):
#        print(":)")

#    elif(ab<=bc):
#        print(":(")

#elif(a==b):
#    if(b<c):
#        print(":)")
    
#    elif(b>c):
#        print(":(")

#2756
#print("       A")
#print("      B B")
#print("     C   C")
#print("    D     D")
#Print("   E       E")
#print("    D     D")
#print("     C   C")
#print("      B B")
#print("       A")

#1759
n=int(input())
i=1
while(i<=n):
    if (i<n):
        print("Ho ", end="")
    else:
        print("Ho!", end="")
    i+=1

