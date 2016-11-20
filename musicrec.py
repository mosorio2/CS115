import time
import sys
from collections import Counter
import re

def menu():
    print "  Enter a letter to choose an option:"
    print "    'e' - Enter Preferences"
    print "    'r' - Get recommendations"
    print "    'p' - Show most popular artists"
    print "    'h' - How popular is the most popular"
    print "    'm' - Which user has the most likes"
    print "    'q' - Save and Quit"
    print ''
    s = raw_input()
    return s

handle = open('musicrecPlus.txt', 'r')
data = handle.read()
total = len(data)

def main():
    if__name__=="__main__"



#p = 1.0/total
d = {}
for char in data:
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1
#items = d.items() #creates a list of tuples from the dictionary
#print items
#numOfUnique = len(d.keys())
#dataLength = "Distinct characters: %s " % numOfUnique
#print dataLength
#OrigBytes = "Total bytes: %s" % fileSize
#print OrigBytes

handle.close()



def writeFile():
    """Opens and writes chosen file"""
    FILE = open(FILE_NAME, 'w')
    for i in D:
        s = i+":"+D[i]
        FILE.write(s)
        FILE.write('\n')
    FILE.close()

def getName():
    """Gets name of user"""
    name = raw_input("Enter your name ")
    return (name.strip()).title()
def getMusic():
    """Gets name of band or artist from user"""
    name = raw_input("Eenter the name of an artist or band you like ")
    return (name.strip()).title()
D = []    


PREF_FILE = "musicrecPlus.txt"

with open('musicrecPlus.txt') as f:
    passage = f.read()

words = re.findall(r'\w+', passage)
word_counter = Counter(words)
count_list = word_counter.items()
wordCo = sorted(count_list, key = lambda x: x[1])


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
    newPref = ''
    if userName in userMap:
        prefs = userMap[userName]
        print("I see that you have used the system before.")
        print("Your music preferences include:")
        for artist in prefs:
            print(artist)
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = raw_input("to see your recommendations or press 'm' to see the best user: ")
        prefs.append(newPref.strip().title())
        saveUserPreferences(userName, prefs, userMap, PREF_FILE)
        if newPref == 'm':
            return findBestUser(userName, prefs, userMap)
        if newPref == 'q':
            menu()
        if newPref == 'r':
            print getRecommendations(userName, prefs, userMap)
    else:
        prefs = []
        prefs.append(newPref.strip().title())
        print("I see that you are a new user.")
        print("Please enter the name of an artist or band")
        newPref = raw_input("that you like: " )
        saveUserPreferences(userName, prefs, userMap, PREF_FILE)
        if newPref == 'q':
            menu()
        
    while newPref != "":
        prefs.append(newPref.strip().title())
        
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = raw_input('to see your recoomendations: ')
        saveUserPreferences(userName, prefs, userMap, PREF_FILE)
        if newPref == 'q':
            break
        if newPref == 'r':
            print getRecommendations(userName, prefs, userMap)
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
        score = numMatchesFast(prefs, userMap[user])
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

def numMatchesFast(userPref, storedData):
    """matches the number from user prefrence and stored data quickly"""
    userPref.sort()
    storedData.sort()
    count = 0
    i = 0
    j = 0
    assert (i <= len(userPref) and j <= len(storedData))
    while i < len(userPref) and j < len(storedData):
       assert (i <= len(userPref) and j <= len(storedData))
       # count <= min(i,j)
       # count is the number of matches between userPref[0:i] and sortedData[0:j]
       if userPref[i] == storedData[j]:
           count +=1
           i += 1
           j += 1
       elif userPref[i] > storedData[j]:
           j += 1
       else:
           i +=1
    assert (i <= len(userPref) and j <= len(storedData))       
    return count

def swap(lst, a, b):
    """swaps a and b in a list"""
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp
def selectionSort(lst):
    """finds the min index in a list and swaps in that list"""
    for i in range(len(lst)-1):
        minIndex = i
        for j in range(i +1,len(lst)):
            if lst[j] < lst[minIndex]:
                minIndex = j
        if minIndex != i:
            swap(lst,i,minIndex)

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

def readPrefs(Fname):
    """reads the prefrences from the users in the file and prints that user"""
    PREF_FILE = open(Fname, 'r')
    for line in PREF_FILE:
        [user,artists] = line.split(':')
        user = user.strip()
        artists = artists.strip(',')
        for i in range(len(artists)):
            artists[i] = artists[i].strip()
        print user
    PREF_FILE.close()

def main():
    ''' The main recommendation function '''
    userMap = loadUsers(PREF_FILE)
    while(1):
        print("Welcome to the music recommender system!")
        c = menu()
        if c == 'p':
            while(1):
                print mostPopArt()
                break
        if c == 'h':
            while(1):
                print howPop()
                break
        if c == 'e':
            while(1):
                userName = getName()
                if userName == '':
                    print ('This is not a valid user name')
                    break
                if userName == "Q":
                    print("Saving and exiting")
                    saveUserPreferences(userName, prefs, userMap, PREF_FILE)
                    break
        
        
                print ("Welcome,", userName)

                prefs = getPreferences(userName, userMap)
                recs = getRecommendations(userName, prefs, userMap)
                #saveUserPreferences(userName, prefs, userMap, fileName)
        if c =='q':
            print('saving and exiting')
            #saveUserPreferences(userName, prefs, userMap, PREF_FILE)
            break

        # Print the user's recommendations
        if c == 'r':
            if len(recs) == 0:
                print("I'm sorry but I have no recommendations")
                print("for you right now.")
            else:
                print(userName, "based on the users I currently")
                print("know about, I believe you might like:")
                for artist in recs:
                    print(artist)

                print("I hope you enjoy them! I will save your")
                print("preferred artists and have new")
                print(" recommendations for you in the future")
            
        
                #saveUserPreferences(userName, prefs, userMap, PREF_FILE)
        saveUserPreferences(userName, prefs, userMap, PREF_FILE)

def mostPopArt():
    """shows the most popular artist from the given information"""
    print("The most popular artist is %s") % wordCo[-1][0]

def howPop():
    """shows how many users like the most popular artist"""
    print('The amount of user who like the most popular artist is %s') % wordCo[-1][1]



if __name__ == "__main__": main()
