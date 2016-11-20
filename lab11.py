import os
S=raw_input("what is the name of your file?")
fileSize=os.path.getsize(S)
handle=open(S, 'r')
data=handle.read()
total=len(data)

def main():
    if__name__=="__main__"

p=1.0/total
d={}
for char in data:
    if char not in d:
        d[char] = 1
    else:
        d[char] +=1
items=d.items()
print items
numOfUnique=len(d.keys())
dataLength="Distinct characters: %s" % numOfUnique
print dataLength
OrigBytes="Total bytes %s" % fileSize
print OrigBytes

handle.close()
