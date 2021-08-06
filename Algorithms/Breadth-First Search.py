from collections import deque

def isSeller(name):
    return name[-1]=='m'

def search(name):
    search_quene =deque()
    search_quene += graph[name]
    searched = []
    while search_quene:
        person = search_quene.popleft()
        if person not in searched:
            if isSeller(person):
                print(person,"is mango seller!")
                return True
            else:
                search_quene += graph[person]
                searched.append(person)
    return False

graph = {}
graph["you"]   = ["alice", "bob", "claire"]
graph["bob"]   = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"]= ["thom", "jonny"]
graph["anuj"]  = []
graph["peggy"] = []
graph["thom"]  = []
graph["jonny"] = []

search("you")