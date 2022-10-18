
#N-Queens problem
N = 4
def issafe(arr,rows,colums):
	for i in range(colums): # check horizontally
		if arr[rows][i] == True:
			return False
	for i,j in zip(range(rows,-1,-1),range(colums,-1,-1)):
		if arr[i][j] == True: # checks upper diagonal
			return False
	for i,j in zip(range(rows,N),(colums,-1,-1)):
		if arr[i][j] == True:        # checks lower diagonal
			return False
	return True

def solveutil(arr,colums):
	if colums >=N:
		return True
	for i in range(N):
		if issafe(arr,i,colums):
			arr[i][colums] =1
			if solveutil(arr,colums+1) == True:
				return True
			arr[i][colums] = 0           #           ###########Backtracking###########

	return False

def print2(arr):
	for i in range(N):
		for j in range(N):
			print(arr[i][j] ,end =" ")
def answer():
	arr =[[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0] ]#we are changing the rows so no need to check vertically just check diagonally and horizonatlly
	if solveutil(arr,0):
		return "solution exists"
	else:
		return "solution doesn't exist"
#	print(arr)
	return True
  
#answer()
#lcs
a = "atha"
b = "partha"
i = len(a)
j = len(b)
def lcs(a,b,i,j):
	if i == 0 or j == 0:
		return 
	if a[i-1] == b[j-1]:
		return lcs(a,b,i-1,j-1)
	else:
		return 1+lcs(a,b,i-1,j) or lcs(a,b,i,j-1)
#print(lcs(a,b,i,j))



#find first and last element of the array 
a = [1,2,3,4,4,4,4,4,4,4,5,8,9]
def bsans(a,target):
	start,x,y = 0,0,0
	end = len(a)-1
	while start<end:
		mid = (start+end)//2
		if a[mid] == target:
			x =	bsr(mid,end)
			y =	bsl(start,mid)
	return y-x
def bsr(start,end):
	target = 4
	mid = (start + end)//2
	if a[mid] == target and a[mid+1]!=target:
		return mid
	else:
		pass

def bsl(start,end):
	pass
a = 0
def binary(x):
	ans =""
	while x>0:
		if x%2 == 0:
			ans += "0"
		else:
			ans += "1"
		x = x//2
	return ans[::-1]
while (a<20):
	if a % 10 == 0:
		print(a,end ='')
	else:
		print(binary(a))
	a += 4
print(int("110000",2))
#binary search
def bs(arr,l,r,mid,target):
	if arr[mid] == target:
		return mid
	if arr[mid] < target:
		return bs(arr, mid+1,r,(l+r)//2,target)
	else:
		return bs(arr,l,mid-1,(l+r)//2,target)
arr = [1,2,3,8,56,1025,4587,6985,56987]
target = 6985
l,r = 0,len(arr)-1
print(bs(arr,l,r,(l+r)//2,target))
class Node:
	def __init__(self,data):
		self.next = None
		self.data = data
def middle(node):
	fast = node.next.next
	slow = node.next
	while fast.next:
		return slow.data
for i in range(20):
	print("*",end = " ")
	for j in range(20):
		if j<i:
			print("*",end = " ")
		else:
			print(" ",end = " ")
	print()
