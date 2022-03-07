# Havel hakim's theorem : it is used to check the given sequence is graph or not

# function return the true value if given sequence is graph
from audioop import reverse


def Havel_Hakim(l):
    l.sort(reverse=True) # to make sure it is descending order
    a=l[0]
    while(a!=-1):
        l.pop(0) # removing first element of the sequence
        try:
            for i in range(a+1):
                l[i]-=1
        except:
            return([-1])
        l.sort(reverse=True) # sort the list in descending order
    return l 

def main():
    l=input("Enter the sequence with space separated ::: ")
    l=l.split()
    for i in range(len(l)):
        # convert each item to int type
        l[i] = int(l[i])
    m=Havel_Hakim(l)
    if(-1 in l):
        print("Graph is not possible")
    else:
        print("Graph is possible for given sequence")
if __name__ == "__main__":
    main()