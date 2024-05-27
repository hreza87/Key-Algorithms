"""
#Binary Gap Problem

def gap(number):
  number=number
  if isinstance(number,int) and (number >=0 and number<=2147483647):
    print(number)
  number=bin(number)
  
  str=number[2:]
  list=[]
  for i in range(len(str)):
    list.append(str[i])
  print(list)
  
  count=0
  current=0
  max2=[]
  for i in range(len(list)):
    if list[i]=="1":
      current=count
      max2.append(current)
      count=0
    elif list[i]=="0":
      count=count+1
  
  return(max(max2))


print(gap(1041))

"""

"""
#Ceaser Cipher -One Letter
char=input("enter a letter")
jumps=int(input("How many jumps would you like to make ?"))
char2=[]
for i in range(len(char)):
  char2.append(ord(char[i]))
  char2[i]=(char2[i]-97)# this point algorithm works fine
  number=char2[i]+jumps
  if number>25:
    char2[i]=number%26
    char2[i]=chr(97+char2[i])
  else:
    char2[i]=chr(97+number)
newword=""
for i in range(len(char2)):
  newword=newword+(char2[i])
print(newword)
"""

"""
#Classic Knoughts and Crosses Game-String Based


board=[["","",""],["","",""],["","",""]]
playera=True

while True:
  if playera==True:
    columna=int(input("Player A enter column:"))
    rowa=int(input("Player A enter row:"))
    if board[rowa][columna]=="":
      board[rowa][columna]="x"
      print(board[0])
      print(board[1])
      print(board[2])
      playera=False
    else:
      print("position already taken, try another")
    if (board[0][0]=="x" and board[0][1]=="x" and board[0][2]=="x") or (board[1][0]=="x" and board[1][1]=="x"and board[1][2]=="x") or (board[2][0]=="x" and board[2][1]=="x"and board[2][2]=="x"):
      print("player a has won")
    elif (board[0][0]=="x" and board[1][0]=="x" and board[2][0]=="x") or (board[0][1]=="x" and board[1][1]=="x" and board[2][1]=="x") or (board[0][2]=="x" and board[1][2]=="x" and board[2][2]=="x"):
      print("player a has won")
    elif (board[0][0]=="x" and board[1][1]=="x" and board[2][2]=="x") or (board[0][2]=="x" and board[1][1]=="x" and board[2][0]=="x"):
      print("player a has won")
  else:
    columnb=int(input("Player B enter column:"))
    rowb=int(input("Player B enter row:"))
    if board[rowb][columnb]=="":
      board[rowb][columnb]="o"
      print(board[0])
      print(board[1])
      print(board[2])
      playera=True
    else:
      print("position already taken, try another")
    if (board[0][0]=="o" and board[0][1]=="o" and board[0][2]=="o") or (board[1][0]=="o" and board[1][1]=="o"and board[1][2]=="o") or (board[2][0]=="o" and board[2][1]=="o"and board[2][2]=="o"):
      print("player b has won")
    elif (board[0][0]=="o" and board[1][0]=="o" and board[2][0]=="o") or (board[0][1]=="o" and board[1][1]=="o" and board[2][1]=="o") or (board[0][2]=="o" and board[1][2]=="o" and board[2][2]=="o"):
      print("player b has won")
    elif (board[0][0]=="o" and board[1][1]=="o" and board[2][2]=="o") or (board[0][2]=="o" and board[1][1]=="o" and board[2][0]=="o"):
      print("player b has won")

"""
"""
#Max Machines for no overlap jobs 

start = [1,8,3,9,6]
finish = [7,9,6,14,7]
machines = []

for i in range(len(start)):
    min_time = start[i]
    max_time = finish[i]
    machines.append([min_time, max_time])

print("Timelines:", machines)

overlapslist = []

for i in range(len(machines)):
    mainstart = machines[i][0]
    mainfinish = machines[i][1]
    print("Main Timeline:", mainstart, mainfinish)
    overlaps = 0
    for j in range(len(machines)):
        if i != j:
            comparestart = machines[j][0]
            comparefinish = machines[j][1]
            print("Comparable Timeline:", comparestart, comparefinish)
            if mainstart < comparefinish and comparestart < mainfinish:
                overlaps = overlaps + 1
    overlapslist.append(overlaps)

print("Number of overlaps for each timeline:", overlapslist)

machines=max(overlapslist)+1
print(machines)

"""
"""
#Roman Numeral Calculator
literal=input("enter the roman literals")
total=0
roman=list(literal)
print(roman)
for i in range(len(roman)):
  if roman[i]=="m":
    roman[i]=1000
  elif roman[i]=="d":
    roman[i]=500
  elif roman[i]=="c":
    roman[i]=100
  elif roman[i]=="l":
    roman[i]=50
  elif roman[i]=="x":
    roman[i]=10
  elif roman[i]=="v":
    roman[i]=5
  elif roman[i]=="i":
    roman[i]=1

roman2=[]
for i in range(1,len(roman)):
    if roman[i]==roman[i-1]:
      roman2.append(roman[i-1])  
    elif roman[i]<roman[i-1]:
      roman2.append(roman[i-1])
    elif roman[i]>roman[i-1]:
      roman2.append(-roman[i-1])
    #elif i==len(roman):
      #roman2.append(roman[i])

roman2.append(roman[len(roman)-1])
      
      
print(roman)
print(roman2)
total=0
for i in range(len(roman2)):
  total=total+roman2[i]
print(total)

"""

"""
#Stack Command Calculator 
def solution(S):
  command=S  
  my_list=command.split()
  stack=[]
  for i in range(len(my_list)):
      if type(my_list[i]) == int:
          my_list[i] = str(my_list[i])  
      elif type(my_list[i]) == str:
          if my_list[i].isdigit():
              my_list[i] = int(my_list[i])  
          elif "." in my_list[i]:
              my_list[i] = float(my_list[i])  
      stack.append(my_list[i])
  print(stack)
  stack2=[]
  for i in range(len(stack)):
    if type(stack[i]) == int:
      stack2.append(stack[i])
      print(stack2)
    elif stack[i]=='-':
      stack2.append(stack2[-1]-stack2[-2])
      stack2.pop(-2)
      stack2.pop(-2)
      print(stack2)
    elif stack[i]=='+':
      number=stack2[-1] + stack2[-2]
      stack2.append(number)
      stack2.pop(-2)
      stack2.pop(-2)
      print(stack2)
    elif stack[i]=="DUP":
      stack2.append(stack2[-1])
      print(stack2)
    elif stack[i]=="POP":
      stack2.pop(-1)
      print(stack2)
S=input("enter an operation to carry out")
print(solution(S))
"""

