with open("source.txt","r") as fi, open("destination.txt","w") as fo:
    fo.write(fi.read().replace("'"," "))

with open("destination.txt","r") as fileref:
    lines=fileref.readlines()

each_line=[]
for line in lines:
    each_line.append(line.strip().split(" "))
#print(each_line)
each_line[0][0]="MARCO"

rx_words=["L","A","ST"]

symbol_table={}
location_counter=[0]
base_table={}

for line in each_line:
    if (len(line)<4):
        diff=4-len(line)
    for _ in range(diff):
        line.append("blank")

for i in range(len(each_line)):
    if (each_line[i][1]=="START"):
        symbol_table[each_line[i][0]]=location_counter[-1]
        location_counter.append(int(each_line[i][2]))
    elif (each_line[i][0]=="END"):
        break
    elif (each_line[i][0]=="USING" and each_line[i][1]=="*"):
        base_table[each_line[i][3]]=location_counter[-1]
        location_counter.append(location_counter[-1])
    elif (each_line[i][0] in rx_words):
        location_counter.append(location_counter[-1]+4)
        symbol_table[each_line[i][3]]=None
    elif (each_line[i][0] in symbol_table):
        symbol_table[each_line[i][0]]=location_counter[-1]
        if (each_line[i][1]=="DS"):
            num1=int(each_line[i][2][0])
            type_word=each_line[i][2][1]
            if (type_word=="F"):
                num2=4
            location_counter.append(location_counter[-1]+num1*num2)
        elif (each_line[i][1]=="DC"):
            location_counter.append(location_counter[-1]+4)
    else:
        continue

print("BASE TABLE")
print("-"*20)
print("Base register\tValue")
for key,value in base_table.items():
    print(f"{int(key)}\t\t{value}")

print("\nSYMBOL TABLE")
print("-"*20)
print("Symbol\tValue")
for key,value in symbol_table.items():
    print(f"{key}\t{value}")

print("\nLOCATION COUNTER")
print(location_counter)

#Pass 1
print("\n------------------------\nPass 1:")
for line in each_line:
    if (line==each_line[0] or line==each_line[1] or line[0]=="END"):
        continue
    elif (line[0] in symbol_table and line[1]=="DC"):
        print("DC "+line[3])
    elif (line[0] in symbol_table and line[1]=="DS"):
        print("DS "+line[2])
    else:
        for word in line:
            if (word in symbol_table):
                print("_",end=" ")
            elif (word=="blank"):
                continue
            else:
                print(word,end=" ")
        print(f"({base_table['15']},{15})")

#Pass 2
print("\n------------------------\nPass 2:")
for line in each_line:
    if (line==each_line[0] or line==each_line[1] or line[0]=="END"):
        continue
    elif (line[0] in symbol_table and line[1]=="DC"):
        print("DC "+line[3])
    elif (line[0] in symbol_table and line[1]=="DS"):
        print("DS "+line[2])
    else:
        for word in line:
            if (word in symbol_table):
                print(symbol_table[word],end=" ")
            elif (word=="blank"):
                continue
            else:
                print(word,end=" ")
        print(f"({base_table['15']},{15})")



