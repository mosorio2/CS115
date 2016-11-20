def numMatchesFast(userPref,storedData):
    userPref.sort()
    storedData.sort()
    matches=0
    i=0
    j=0
    assert(i<=len(userPref) and j<=len(storedData))
    while i < len(usePref) and j< len(storedData):
        assert(i<=len(userPref) and j<=len(storedData))
        if userPref[i]==storedData[j]:
            matches +=1
            i+=1
            j+=1
        elif userPref[i]>storedData[j]:
            j+=1
        else:
            i+=1
    assert(i<=len(userPref) and j<=len(storedData))
    return matches
            
