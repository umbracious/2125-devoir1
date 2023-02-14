#Satyam Chowdhury 20214226
#Carlos Eduardo

#Sources: 1- https://realpython.com/python-csv/#parsing-csv-files-with-pythons-built-in-csv-library -> csv reader
#         2- https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/ -> check for intersection

import csv
import math

points=[]

class Node:

    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"

class Edge:

    def __init__(self, n1:Node, n2:Node):
        self.n1 = n1
        self.n2 = n2

#csv parsing adapted from source 1
with open('data_devoir1\instance_jarry.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line = 0
    for row in csv_reader:
        if line > 0:
            points.append(Node(float(row[8]),float(row[9])))
        line+=1

#calculate distance
def distance(p1:Node, p2:Node):

    distX = abs(a.x - b.x)
    distY = abs(a.y - b.y)

    #pythagore
    return math.sqrt(distX**2+distY**2)

########## following methods were taken from source 2 ##########

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


# whats left to do:

# -create a list of valid edges (5<=dist<=30)
# -write a greedy algortithm that chooses the longest edges in order as long as they dont intersect
# -if there is enough time, try a different algorithm to see which gets a better result (expand from both nodes of the largest edge)