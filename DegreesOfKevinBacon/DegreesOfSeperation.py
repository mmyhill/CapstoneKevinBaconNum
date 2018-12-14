#nconst	primaryName	birthYear	deathYear	primaryProfession	knownForTitles
#tconst	ordering nconst	category	job	characters
import re
import random
class GraphNode:#acts as both movie and actor class
    def __init__(self, const, ifMovie):
        self.ifMovie = ifMovie
        self.const = const
        self.connect = []#where all connections will be stored
        self.isChecked = False

    #it is possilbe for node class to be both movies and people because all data is
    #stored and boolean distinguishes movies from people
    def getConst(self):
        return self.const

    def addConnection(self, toConnect):
        self.connect.append(toConnect)

    def isMovie(self):
        return self.isMovie

    def getConnections(self):
        return self.connect

    def flipCheck(self):
        self.isChecked = not self.isChecked

    def isChecked(self):
        return self.isChecked

class BiPartite:
    def __init__(self):
        self.peoples = []
        self.movies = []

    def addNew(self, line):#line will be regex returned line with all info
        #actors start with n, titles with tt
        if(line[0] == 't'): #is movie
            #will see if movie is already in data base when using method
            newNode = GraphNode(line[0 : line.find(" ")], True)
            self.movie.append(newNode)#adds t const

        else:#is actor
            newNode = GraphNode(line[0 : line.find(" ")], False)
            self.peoples.append(newNode)#adds t const

    def connect(self, personLine, personNode):#to be called after everything has been added
        inMovies = re.findall(" tt0*(\d+)$,?")#need to test this
        for movie in inMovies:
            personNode.addConnection(self.movies[movie])
            self.movies[movie].addConnection(personNode)#need to have connection running both ways

    def calculateNumber(actor):#is node
        #assumes searching for Kevin bacon
        KB = self.peoples[102]
        if(not actor == KB):
            return self.BFS(actor, KB)
        else:
            return 0

    def calculateNumber(actorToFind, actorIn):#is node
        #assumes searching for Kevin bacon
        if(not actorToFind == actorIn):
            return self.BFS(actorIn, actorToFind)
        else:
            return 0

    def BFS(self, personIn, personToFind):
        toReset = []#filled with nodes that have already been visited
        shortestPath = 1 #shortest path automatically through one movie if not same person
        canStillLook = True #there are still movies to look for connections in

        moviesToLookIn = personToFind.getConnections()
        #plan for breadth first search:
        while(len(moviesToLookIn) > 0):
            nextPeoples = []
            for movie in moviesToLookIn:
                    movie.flipCheck()
                    toReset.append(movie)
                    for person in movie.getConnections():
                        nextPeoples.append(person)

            moviesToLookIn = []

            for person in nextPeoples:
                if(person.getConst() == personIn.getConst()):
                    return shortestPath #break, node has been found and shortest paths checked first
                else:
                    #clears queue
                    shortestPath += 1
                    for movie in person.getConnections():
                        if(not movie.isChecked()):
                            moviesToLookIn.append(movie)

        #make sure to check if person being searched for is not same person being searched from

        #reset movie nodes for next search
        for node in toReset:
            node.flipCheck()

    def calcAverageBaconNum(self, choseAccuracy):#higher accuracy takes far more time, let user chose
        #chose accuracy will be the number of people used in average
        if(choseAccuracy > len(self.peoples)):
            print("Error: specified accuracy exceeds size of database")
        sum = 0;
        toReset = []#list of people to set as not checked for future methods
        for x in range(choseAccuracy):
            #find random person to check
            use = self.peoples[random.randInt(0, len(self.peoples) - 1)]
            while(use.isChecked()):
                use = self.peoples[random.randInt(0, len(self.peoples) - 1)]
            sum += self.calculateNumber(use)
        avgNum = (sum * 1.0)/choseAccuracy

        for node in toReset:
            node.flipCheck()

        print("Average Bacon Number: " + avgNum + "\n")

    def calcAverageHollywoodNum(self, choseAccuracy):#higher accuracy takes far more time, let user chose
        #chose accuracy will be the number of people used in average
        if(choseAccuracy > len(self.peoples)):
            print("Error: specified accuracy exceeds size of database")
        sum = 0;
        toReset = []#list of people to set as not checked for future methods
        for x in range(choseAccuracy):
            #find random person to check
            use = self.peoples[random.randInt(0, len(self.peoples) - 1)]
            while(use.isChecked()):
                use = self.peoples[random.randInt(0, len(self.peoples) - 1)]
            toReset.append(use)
            if(len(toReset) < 2):
                use2 = self.peoples[random.randInt(0, len(self.peoples) - 1)]
                while(use2.isChecked()):
                    use2 = self.peoples[random.randInt(0, len(self.peoples) - 1)]
                toReset.append(use2)
            else:
                use2 = toReset
            sum += self.calculateNumber(use, use2)
            
        avgNum = (sum * 1.0)/choseAccuracy

        for node in toReset:
            node.flipCheck()

        print("Average Bacon Number: " + avgNum + "\n")




            #add all connections on current level to queue
            #see if item being searched for is in queue
            #if not, go one level deeper
            #keep looping until connection found or no where to look






        # if(nodeToFind.isMovie() != nodeIn.isMovie())#not same type, no point in looking in this level
        #     for elem in nodeIn.getConnections():
        #         toReturn += self.BFS(elem, nodeToFind)
def main():
    graph = BiPartite()
    dADDa = open("title.principals.tsv", "r").read().split('\n')
    daDDa += open("name.basics.tsv", "r").read().split('\n')
    for item in dADDA:
        graph.addNew(dADDA)
    graph.connect()
    print(graph.calculateNumber("nm0000018	Kirk Douglas	1916	\N	actor,producer,soundtrack	tt0049456,tt0080736,tt0054331,tt0052365"))


main()
