string=input("Please enter a word or a sentence:")
char=input("Please enter the charecter you want to see repeated:")
i=0
count=0
while(i<len(string)):
    if (string[i]==char):
        count=count+1
    i=i+1
print("The total number of times",char,"has occoured is",count)