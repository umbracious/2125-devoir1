#Satyam Chowdhury 20214226
#Carlos Eduardo

#Using a greedy algorithm takes coordinates of nodes (trees) and returns a list of slacks (edges in the format [tree1, tree2])
#None of these edges should overlap, and the edges are between 5-30m long.
#The algorithm should ideally attempt to maximize the total amount of distance covered by the slacks

#Sources: 1- https://realpython.com/python-csv/#parsing-csv-files-with-pythons-built-in-csv-library -> csv reader
#         2- https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/ -> check for intersection

import csv
import math
import numpy as np
import sys

#node class to represent trees
class Node:

    def __init__(self, x:float, y:float, n:int):
        self.x = x
        self.y = y
        self.n = n

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

#edge class to represent slacks
class Edge:

    def __init__(self, n1:Node, n2:Node):
        self.n1 = n1
        self.n2 = n2
        self.dist = distance(self.n1,self.n2)

    def __str__(self):
        return f"x1: {self.n1.x}, y1: {self.n1.y}, x2: {self.n2.x}, y2: {self.n2.y}, distance: {self.dist}"

#calculate distance between two nodes
def distance(n1:Node, n2:Node):

    distX = abs(n1.x - n2.x)
    distY = abs(n1.y - n2.y)

    #pythagore
    return math.sqrt(distX**2+distY**2)

########## following methods were taken from source 2 ##########

#checks if point q lies between points p and r
def onSegment(p, q, r):
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and 
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False
  
def orientation(p, q, r):
    # to find the orientation of an ordered triplet (p,q,r)
    # function returns the following values:
    # 0 : Collinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise
      
    # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/ 
    # for details of below formula. 
      
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if (val > 0):
          
        # Clockwise orientation
        return 1
    elif (val < 0):
          
        # Counterclockwise orientation
        return 2
    else:
          
        # Collinear orientation
        return 0
  
#returns True if edge1 and edge2 intersect, False if not
def intersect(edge1:Edge, edge2:Edge):
    # Find the 4 orientations required for 
    # the general and special cases
    p1 = edge1.n1
    q1 = edge1.n2

    p2 = edge2.n1
    q2 = edge2.n2

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
  
    # General case
    if ((o1 != o2) and (o3 != o4)):
        return True
  
    # Special Cases
  
    # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
    if ((o1 == 0) and onSegment(p1, p2, q1)):
        return True
  
    # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
    if ((o2 == 0) and onSegment(p1, q2, q1)):
        return True
  
    # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
    if ((o3 == 0) and onSegment(p2, p1, q2)):
        return True
  
    # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
    if ((o4 == 0) and onSegment(p2, q1, q2)):
        return True

##############################################################

def main():
    nodes=[] #array of all nodes
    edges=[] #array of all valid edges
    final=[] #array of all final edges
    total=0

    #csv parsing adapted from source 1
    with open(f'data_devoir1\{sys.argv[1]}') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line = 0
        for row in csv_reader:
            if line > 0 and float(row[14])>=25:
                nodes.append(Node(float(row[8]),float(row[9]),(line-1)))
            line+=1

    #find all valid edges
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            n1 = nodes[i]
            n2 = nodes[j]

            dist = distance(n1,n2)

            if dist>=5 and dist<=30:
                edges.append(Edge(n1, n2))

    #sort edges in order of distance
    edges.sort(key=lambda edge: edge.dist)
    np.asarray(edges)

    #current largest edge
    curr = edges.pop()
    final.append([curr.n1.n, curr.n2.n])
    total+=curr.dist

    #each iteration, select largest edge and remove overlapping edges
    while len(edges)>0:
        for edge in edges:
            if intersect(edge, curr):
                edges.remove(edge)
        curr = edges.pop()
        final.append([curr.n1.n, curr.n2.n])
        total+=curr.dist
    
    print(final)
    print(total)
    return final


if __name__ == "__main__":
    main()

# TODO:
# -determine complexity of algorithm
# -implement time measurement
# -potentially make the algorithm more efficient, runtime is a little long now
# -if there is enough time, try a different algorithm to see which gets a better result (expand from both nodes of the largest edge)

# possible better algorithms:
# - for each edge, add the distance covered by every single one of the edges it overlaps with and choose edge that returns the shortest distance. repeat until no edges left
# - choose the largest edge. every iteration, list every edge connecting to a node on the graph. add the largest of these edges to the graph