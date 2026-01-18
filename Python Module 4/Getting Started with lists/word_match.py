def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(words)> 1 and word[0] == word[-1]:
            ctr+=1
            lst.append
    print ("List of words with the first and last charecter as the same\n",lst)
    return ctr
count=match_words(['abc','cfc', 'xyz','aba','1221'])
print ("Number of words having the same\n",count)