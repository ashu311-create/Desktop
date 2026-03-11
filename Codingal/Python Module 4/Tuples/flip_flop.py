def pallind(r):
    e=len(r)-1
    s=0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True
r=(1,2,3,3,2,1)
if (pallind(r)):
    print("This is a Flip-Flop")
else:
    print("This is not a Flip-Flop")