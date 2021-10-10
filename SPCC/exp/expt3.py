with open("source03.txt","r") as fi:
    content=fi.readlines()

words=[]
for line in content:
    words.append(line.strip().split(" "))
MNT=[]
ALA={}
MDT=[]
MNTC=0
MDTC=0
ALAC=0
global_tracker={}
num=25

for i in range(len(words)):
    if (words[i][0]=="MACRO"):
        j=1
        arg_list=[]
        while (words[i+j][0]!="MEND"):
            if (j==1):
                MNTC+=1
                MDTC+=1
                MNT.append((MNTC,words[i+j][0],MDTC))
                formatted_line=words[i+j][0]+" "
                for word in words[i+j]:
                    if ("&" in word):
                        ALAC+=1
                        ALA[word]=ALAC
                        formatted_line+="#"+str(ALA[word])+" , "
                        arg_list.append(word)
                global_tracker[words[i+j][0]]=arg_list
                formatted_line=formatted_line[:len(formatted_line)-3]
                MDT.append([MDTC,formatted_line])
            else:
                formatted_line=""
                for word in words[i+j]:
                    if (word not in arg_list):
                        formatted_line+=word+" "
                    else:
                        formatted_line+="#"+str(ALA[word])
                MDTC+=1
                MDT.append([MDTC,formatted_line])
            j+=1
        MDTC+=1
        MDT.append([MDTC,"MEND"])

#Pass 1
print("Pass 1")        
print("\nMNT")
print("-"*num)
print("Index\tName\tMDT Index")
for values in MNT:
    print(f"{values[0]}\t{values[1]}\t{values[2]}")

print("\nALA")
print("-"*num)
print("Index\tArguments")
for key,value in ALA.items():
    print(f"{value}\t{key}")

print("\nMDT")
print("-"*num)
print("Index\tDefinitions")
for values in MDT:
    print(f"{values[0]}\t{values[1]}")

#print(global_tracker)
gen_strings=[]
for macro_name,arguments in global_tracker.items():
    formatted_line=macro_name+" "
    for arg in arguments:
        formatted_line+=arg+" , "
    formatted_line=formatted_line[:len(formatted_line)-3]
    gen_strings.append(formatted_line.split(" "))
#print(gen_strings)

mapper={}
for x in gen_strings:
    for word in words:
        if (word[0]==x[0] and word!=x):
            for i in range(len(word)):
                if (word[i]!=x[i]):
                    mapper[ALA[x[i]]]=word[i]

#print(mapper)
for i in range(len(MDT)):
    _,m_content=MDT[i]
    for key,value in mapper.items():
        if ("#"+str(key) in m_content):
            m_content=m_content.replace("#"+str(key),mapper[key])
    MDT[i][1]=m_content

#print(MDT)
#Pass 2
print("\nPass 2")        
print("\nMNT")
print("-"*num)
print("Index\tName\tMDT Index")
for values in MNT:
    print(f"{values[0]}\t{values[1]}\t{values[2]}")

print("\nALA")
print("-"*num)
print("Index\tArguments")
for key,value in mapper.items():
    print(f"{key}\t{value}")

print("\nMDT")
print("-"*num)
print("Index\tDefinitions")
for values in MDT:
    print(f"{values[0]}\t{values[1]}")
