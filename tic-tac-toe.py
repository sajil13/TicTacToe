import time
moves = {}


def track(plr,pos):
    if pos in moves:
        print("Illegal Move")
    else:
        if (pos == "7" or pos == "Q" or pos == "q"):
            pos = "00"
        elif (pos == "8" or pos == "W" or pos == "w"):
            pos = "01"
        elif (pos == "9" or pos == "E" or pos == "e"):
            pos = "02"
        elif (pos == "4" or pos == "A" or pos == "a"):
            pos = "10"
        elif (pos == "5" or pos == "S" or pos == "s"):
            pos = "11"
        elif (pos == "6" or pos == "D" or pos == "d"):
            pos = "12"
        elif (pos == "1" or pos == "Z" or pos == "z"):
            pos = "20"
        elif (pos == "2" or pos == "X" or pos == "x"):
            pos = "21"
        elif (pos == "3" or pos == "C" or pos == "c"):
            pos = "22"
    moves[pos] = plr


def show():
    print("""
         %s | %s | %s
        -----------
         %s | %s | %s
        -----------
         %s | %s | %s\n"""%(moves["00"],moves["01"],moves["02"],moves["10"],moves["11"],moves["12"],moves["20"],moves["21"],moves["22"]))

    
def result(plr):
    res = []
    res1 = []
    res3 = []
    res4 = []
    
    k = 2;
    for i in range(3):
        
        
        res3.append(str(i)+str(i))
        
        l = 0
        res4.append(str(k)+str(i))
        k-=1
        l+=1
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        for j in range(3):
            
            res.append(str(i)+str(j))
            res1.append(str(j)+str(i))
            
            
    if (plr == moves[res[0]] and plr == moves[res[1]] and plr == moves[res[2]]) or (plr == moves[res[3]] and plr == moves[res[4]] and plr == moves[res[5]]) or (plr == moves[res[6]] and plr == moves[res[7]] and plr == moves[res[8]]):
        count1 +=1
        
    if (plr == moves[res1[0]] and plr == moves[res1[1]] and plr == moves[res1[2]]) or (plr == moves[res1[3]] and plr == moves[res1[4]] and plr == moves[res1[5]]) or (plr == moves[res1[6]] and plr == moves[res1[7]] and plr == moves[res1[8]]):
        count2 +=1
        

    if (plr == moves[res3[0]] and plr == moves[res3[1]] and plr == moves[res3[2]]):
        count3 +=1
        

    if (plr == moves[res4[0]] and plr == moves[res4[1]] and plr == moves[res4[2]]):
        count4 +=1
        

    else:
        pass
    if count1 == 1 or count2 == 1 or count3 == 1 or count4 == 1:
        print(plr + " WINS!")
        quit() 
    else:
        pass
    

print("For Those who have a dedicated num pad on the key board use this")
print('''
          7 | 8 | 9
         -----------
          4 | 5 | 6
         -----------
          1 | 2 | 3''')

print("For Those who dont have a dedicated num pad use this")
print('''
          Q | W | E
         -----------
          A | S | D
         -----------
          Z | X | C\n''')

input("Press ENTER to start")
print("\n")

print("Loading",end="");time.sleep(0.5);print(".",end="");time.sleep(0.5);print(".",end="");time.sleep(0.5);print(".");time.sleep(0.5);
print("\n")


for i in range(3):
    for j in range(3):
        posi = str(i)+str(j)
        moves[posi] = " "
for i in range(1,10):
    if i%2 == 0:
        print("O's Turn")
        position = input("Input where you want to make your move NOTE: Follow the map mensioned above ")
        print("\n")
        
        track("O",position)
        show()
        result("O")
    else:
        print("X's Turn") #pun intended
        position = input("Input where you want to make your move NOTE: Follow the map mensioned above ")
        print("\n")
        track("X",position)
        show()
        result("X")

    
    

    
    


