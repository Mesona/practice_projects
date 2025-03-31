
def initial_graph():
  return {
    'A': {'B':1, 'C':4, 'D':2, 'E':10},
    'B': {'A':9, 'E':15},
    'C': {'A':4, 'F':15},
    'D': {'A':10, 'F':7},
    'E': {'B':3, 'J':7},
    'F': {'C':11, 'D':14, 'K':3, 'G':9},
    'G': {'F':12, 'I':4},
    'H': {'J':13},
    'I': {'G':6, 'J':7},
    'J': {'H':2, 'I':4},
    'K': {'F':6}
  }

class Dijkstra:
  def __init__(self, graph=initial_graph(), source="A", destination="H"):
    self.graph = graph
    self.source = source
    self.destination = destination

    self.path = {}
    self.neighbors = {}
    self.queue = []


    print("Initial graph:", self.graph)

  def nodeSetup(self):
    for node in self.graph:
      self.path[node] = float("inf")
      self.neighbors[node] = None
      self.queue.append(node)

    self.path[self.source] = 0

  def dijkstra(self):
    print("NEIGHBORS BEFORE:", self.neighbors)
    while self.queue:
      currentNode = self.queue[0]
      for n in range(1, len(self.queue)):
        nextNode = self.queue[n]
        if self.path[nextNode] < self.path[currentNode]:
          currentNode = nextNode

      self.queue.remove(currentNode)

      for i in self.graph[currentNode]:
        alternatePath = self.graph[currentNode][i] + self.path[currentNode]
        if alternatePath < self.path[i]:
          self.path[i] = alternatePath
          self.neighbors[i] = currentNode

    print("NEIGHBORS AFTER:", self.neighbors)

  def solve(self):
    print("The shortest path between " + self.destination + " and " + self.source)
    print(self.destination, end = "<-")
    while True:
      self.destination = self.neighbors[self.destination]
      if self.destination is None:
        print("")
        break

      print(self.destination, end = "<-")

  def run(self):
    self.nodeSetup()
    self.dijkstra()
    self.solve()
