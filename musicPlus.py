

PREF_FILE = "musicrecPlus.txt"

def loadUsers(fileName):
    ''' Reads in a file of stored users' preferences
        stored in the file 'fileName'.
        Returns a dictionary containing a mapping
        of user names to a list preferred artists
    '''
    file = open(fileName, 'r')
    userDict = {}
    for line in file:
        # Read and parse a single line
        [userName, bands] = line.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        userDict[userName] = bandList
    file.close()
    return userDict

def getPreferences(userName, userMap):
    ''' Returns a list of the uesr's preferred artists.

        If the system already knows about the user,
        it gets the preferences out of the userMap
        dictionary and then asks the user if she has
        additional preferences.  If the user is new,
        it simply asks the user for her preferences. '''
    newPref = ""
    if userName in userMap:
        prefs = userMap[userName]
        print("I see that you have used the system before.")
        print("Your music preferences include:")
        for artist in prefs:
            print(artist)
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = raw_input("to complete your preferences: ")
    else:
        prefs = []
        print("I see that you are a new user.")
        print("Please enter the name of an artist or band")
        newPref = raw_input("that you like: " )
        
    while newPref != "":
        prefs.append(newPref.strip().title())
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = raw_input("to complete your preferences: ")
        
    # Always keep the lists in sorted order for ease of
    # comparison
    prefs.sort()
    return prefs

def getRecommendations(currUser, prefs, userMap):
    ''' Gets recommendations for a user (currUser) based
        on the users in userMap (a dictionary)
        and the user's preferences in pref (a list).
        Returns a list of recommended artists.  '''
    bestUser = findBestUser(currUser, prefs, userMap)
    recommendations = drop(prefs, userMap[bestUser])
    return recommendations

def findBestUser(currUser, prefs, userMap):
    ''' Find the user whose tastes are closest to the current
        user.  Return the best user's name (a string) '''
    users = userMap.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        score = numMatches(prefs, userMap[user])
        if score > bestScore and currUser != user:
            bestScore = score
            bestUser = user
    return bestUser

def drop(list1, list2):
    ''' Return a new list that contains only the elements in
        list2 that were NOT in list1. '''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    
    return list3

def numMatches( list1, list2 ):
    ''' return the number of elements that match between
        two sorted lists '''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def saveUserPreferences(userName, prefs, userMap, fileName):
    ''' Writes all of the user preferences to the file.
        Returns nothing. '''
    userMap[userName] = prefs
    file = open(fileName, "w")
    for user in userMap:
        toSave = str(user) + ":" + ",".join(userMap[user]) + \
                    "\n"
        file.write(toSave)
    file.close()

def mostPopular(userMap):
    artists = {}
    for x in userMap:
        for y in userMap[x]:
            if y in artists:
                artists[y] += 1
            else:
                artists[y] = 1

    mostPopular = ['', 0]
    for x in artists:
        if artists[x] > mostPopular[1]:
            mostPopular = [x, artists[x]]
        elif artists[x] == mostPopular[1]:
            return "Sorry, there are multiple popular artists."
    return "The most popular artist is:", mostPopular[0]

def mostPopularNum(userMap):
    artists = {}
    for x in userMap:
        for y in userMap[x]:
            if y in artists:
                artists[y] += 1
            else:
                artists[y] = 1

    mostPopular = ['', 0]
    for x in artists:
        if artists[x] > mostPopular[1]:
            mostPopular = [x, artists[x]]
        elif artists[x] == mostPopular[1]:
            return "Sorry, there are multiple popular artists."
    return "Users who like the most popular artist:", mostPopular[1]

def mostLikes(userMap):
    mostLikes = ['', 0]
    for x in userMap:
        if len(userMap[x]) > mostLikes[1]:
            if x[-1] != '$':
                mostLikes = [x, len(userMap[x])]
                print mostLikes
    return "The user with the most likes is:", mostLikes[0], "with", mostLikes[1], \
           "total likes. Their artists are:", userMap[mostLikes[0]]

def main():
    ''' The main recommendation function '''
    userMap = loadUsers(PREF_FILE)
    print("Welcome to the music recommender system!")

    userName = raw_input("Please enter your name: ")
    print "Welcome,", userName

    selection = ''
    prefs = []
    while(selection != 'q'):
        print "\nEnter a letter to choose an option:"
        selection = raw_input("e - enter preferences \
                          \nr - get recommendations \
                          \np - show most popular artists \
                          \nh - how popular is the most popular \
                          \nm - which user has the most likes \
                          \nq - save and quit\n")
        if selection == 'e':
            prefs = getPreferences(userName, userMap)
            saveUserPreferences(userName, prefs, userMap, PREF_FILE)

        elif selection == 'r':
            if len(userMap) > 1 and prefs != []:
                recs = getRecommendations(userName, prefs, userMap)

                # Print the user's recommendations
                if len(recs) == 0:
                    print("I'm sorry but I have no recommendations")
                    print("for you right now.")
                else:
                    print userName, ",based on the users I currently"
                    print("know about, I believe you might like:")
                for artist in recs:
                    print(artist)

                    print("I hope you enjoy them! I will save your")
                    print("preferred artists and have new")
                    print("recommendations for you in the future.")
            else:
                print "Sorry, you are either the only user in the system, or you have not entered any preferences."

        elif selection == 'p':
            print mostPopular(userMap)

        elif selection == 'h':
            print mostPopularNum(userMap)

        elif selection == 'm':
            print mostLikes(userMap)

        elif selection == 'q':
            print "Thank you for using the music recommender system."
            saveUserPreferences(userName, prefs, userMap, PREF_FILE)

        else:
            print "Error: Please input a valid selection."
    
if __name__ == "__main__": main()
