mod = 11

class Hashtag():
    def __init__(self, hashtag, tweet):
        self.hashtag = hashtag
        self.tweet = tweet
        self.number = 0

def readData():
    dataFile = open('hashtagList.csv', 'r')
    objectList=[]
    for line in dataFile:
        thisline = line.split(",")
        hashtag = thisline[0]
        tweet = thisline[1]
        objectList.append(Hashtag(hashtag, tweet))
    dataFile.close()
    return objectList


def hashascii():
    objectList = readData()
    for x in objectList:
        number = 0
        for charecter in x.hashtag:
            number = number + ord(charecter)
        number = number%mod
        x.number = number
        print(number)
    return objectList
  
hashascii()

def listOfLists():
    objectList = hashascii()
    twitterList = []
    for i in range(mod):
         val =  i
         i = []
         for x in objectList:
             if x.number == val:
                #print(x.hashtag)
                i.append(x)
         twitterList.append(i)
    #print(len(twitterList))
    return twitterList
        



twitterList = listOfLists()

def findTweet(hashtag):
    holdingList=[]
    number = 0
    for charecter in hashtag:
        number = number + ord(charecter)
    number = number%mod
    for x in twitterList[number]:
        if x.hashtag == hashtag:
            holdingList.append(x)
    return holdingList
    
        
def writeTweet(newhashtag, newtweet):
    new = Hashtag(newhashtag, newtweet)
    number = 0
    for charecter in new.hashtag:
        number =number + ord(charecter)
    number = number % mod
    new.number=number
    twitterList[number].append(new)
    
    


    
def test():
    twitterList=listOfLists()
    val=0
    for x in twitterList:
        print(val)
        val=val+1
        for item in x:
            print(item.hashtag,' ', item.tweet)
    


def test2():
    holdingList=findTweet("blessed")
    for item in holdingList:
        print(item.tweet)


def test3():
    writeTweet("blessed","There is so much good in the world")
    

test3()