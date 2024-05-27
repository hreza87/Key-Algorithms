
"""
#Insertion Sort Algorithm 
list=[5,2,1,6]
def insertionsort(list):
  for i in range(1,len(list)):
    j=i
    print("For loop runs pointing towards index",i,"which is",list[i])
    print(list)
    proceed=input("press enter to proceed to inner while loop")
    while list[j]<list[j-1] and j>0:
      print("The inner loop executes when list is as follows:",list)
      print("j is",j," list[j-1]:",list[j-1]," list[j]:",list[j])
      temp=list[j-1]
      list[j-1]=list[j]
      list[j]=temp
      j=j-1
      print("the inner loop ran and list is as follows",list)
      proceed=input("press enter to proceed the inner loop")
    proceed=input("press enter to proceed back to the for loop")
      

insertionsort(list)
print(list)

"""
"""
#Bubble Sort Algorithm 
list=[6,4,2,10,5,1]
sorted=False
print(list)
while sorted==False:# The while loop will keep running until array is sorted.
  sorted=True #assumes the for loop will not need to sort any of the items out so stops the while loop.
  for i in range(len(list)-1):# the for loop will check through the list once and swap elements around .
    if list[i]>list[i+1]:# swaps the elements using three way swap.
      temp=list[i]
      list[i]=list[i+1]
      list[i+1]=temp
      print(list)
      sorted=False # resets the while loop as there was a need to swap the items. 
    else:
      print(list)
  print("for loop ended, finished all comparisons")
print("while loop is going to end here.")

"""

"""
#Binary Search 
list=[1,2,3,4,5,6,7]
searchitem=5 # is the item to look for 

found=False# list has not found the item yet
left=0 # starting point of the list 
right=len(list)-1# end point of the list 

while found==False and left<=right: # repeats halving the list until list is no more and item is found.
  midpoint=(left+right)//2
  print(list[left:right+1])
  if list[midpoint]==searchitem:
    found=True
    print("item found at position",midpoint)
  elif searchitem>list[midpoint]:
    left=midpoint+1 
  elif searchitem<list[midpoint]:
    right=midpoint-1
    
"""



