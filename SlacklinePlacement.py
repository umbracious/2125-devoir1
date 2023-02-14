#Satyam Chowdhury 20214226
#Carlos Eduardo

#Sources: https://realpython.com/python-csv/#parsing-csv-files-with-pythons-built-in-csv-library -> csv reader
#         https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/ -> check for intersection

import csv
import math

points=[]

class Node:

    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x},{self.y}"

class Edge:

    def __init__(self, n1:Node, n2:Node) -> None:
        self.p1 = p1
        self.p2 = p2

#csv parsing
with open('data_devoir1\instance_jarry.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line = 0
    for row in csv_reader:
        if line > 0:
            points.append(Node(float(row[8]),float(row[9])))
        line+=1

#calculate distance
def distance(p1:Node, p2:Node) -> float:

    distX = abs(a.x - b.x)
    distY = abs(a.y - b.y)

    #pythagore
    return math.sqrt(distX**2+distY**2)

#check if two edges are intersecting:
def intersect(edge1:Edge, edge2:Edge) -> bool:
   return True

# whats left to do:

# -finish intersect method
# -create a list of valid edges (5<=dist<=30)
# -write a greedy algortithm that chooses the longest edges in order as long as they dont intersect
# -if there is enough time, try a different algorithm to see which gets a better result (expand from both nodes of the largest edge)