'''
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key
def inordertraversal(root):
    if root:
        inordertraversal(root.left)
        print(root.data)
        inordertraversal(root.right)
# Driver code
#
root = Node(1)
#I made the gap
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
inordertraversal(root)

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def levelordertraversal(root):
    
    if root is  None:
        return
    q=[]
    q.append(root)
    while(len(q)>0):
        print(q[0].data)
        node=q.pop(0)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print ("Level Order Traversal of binary tree is -")
levelordertraversal(root)

print("                                 cyclic Sort                                    ")
Array=[1,2,3,5,8,4,9,6,7,0]
for i in range(len(Array)):
    Array.clear()
    Array.append(i)
    print(Array, end=' ')

print("           ")
print( 



)
print('                               ######boundary traversal#######                   ')
class node:
    def __init__(self,data):
        self.data=data
        self.left=left
        self.right=right
def leaves(root):
    if root:
        leaves(root.left)
        if root.left is None and root.right is None:
            print(root.data)
        leaves(root.right)
def boundaryleft(root):
    if root:
        if root.left:
            print(root.data)
            boundaryleft(root.left)
        elif(root.right):
            print(root.right)
            boundaryleft(root.right)
def boundaryright(root):
    if root:
        if root.right:
            boundaryright(root.right)
            print(root.data)
        elif(root.left):
            boundaryright(root.data)
            print(root.data)
def printboundarytraversal(root):
    if root:
        print(root.data)
        boundaryleft(root.left)
        leaves(root.left)
        leaves(root.right)
        boundaryright(root.right)
root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
printboundarytraversal(root)

print("                       %%%%%$$$###&&&vertical order traversal&&&&######              ")
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def getverticalorder(root,hd,m):
    if root is None:
        return

    try:
        m[hd].append(root.data)
    except:
        m[hd]=[root.data]
    getverticalorder(root.left,hd-1,m)
    getverticalorder(root.right,hd+1,m)
def printverticalorder(root):
    m=dict()
    hd=0
    getverticalorder(root,hd,m)
    for index,val in enumerate(sorted(m)):
        for i in m[val]:
            print(i)
        print
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
print ("Vertical order traversal is")
printverticalorder(root)

print('                      $$$$$$$$$$$$$top view##############                               ')
class newNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def fillmap(root,d,l,m):
    if root is None:
        return
    if d not in m:
        m[d]=[root.key,l]
    elif (m[d][1] > l):
        m[d]=[root.key,l]
    fillmap(root.left,d-1,l+1,m)
    fillmap(root.right,d+1,l+1,m)
def topview(root):
    m={}
    fillmap(root,0,0,m)
    for i in sorted(m.keys()):
         print(m[i][0], end=" ")
        
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.right = newNode(4)
root.left.right.right = newNode(5)
root.left.right.right.right = newNode(6)
print("Following are nodes in top view of Binary Tree")
topview(root)
''' 
from queue import deque
 
def topView(root):
    dic = {}
 
    # variable which is going to store
    # the minimum positional value.
    mi = float('inf')
 
    if not root:
        return 1
 
    q = deque([(root, 0)])
 
    while q:
        cur = q.popleft()
        if cur[1] not in dic:
            dic[cur[1]] = cur[0].data
            mi = min(mi, cur[1])
        if cur[0].left:
            q.append((cur[0].left, cur[1] - 1))
        if cur[0].right:
            q.append((cur[0].right, cur[1] + 1))
 
    # Starting from the leftmost node and
    # just incrementing it until
    # the rightmost node stored in the dic.
    while mi in dic:
        print(dic[mi], end=' ')
        mi += 1
 
 
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
 
# Driver Code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(9)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(13)
    print("Top view of Binary Tree (from left to right) is as follows:")
    topView(root)  
