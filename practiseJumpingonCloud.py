length=len(c)
    count =i= 0
    #0 0 1 0 1 0 and 0100010 
    while (i!=length):
        j = i +1
        if (c[j] is 1):
            i=j+1
            count+=1
        else:
            if (j!=length):
                j+=1
                if (c[j] is not 1):
                    i=j
                    count+=1
                else :
                    i=j-1
                    count+=1
            
            
    return count  