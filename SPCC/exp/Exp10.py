import random
t=int(input("Enter number of production : "))
print("Enter productions : ")
d={}
R0=""
R1=""
left={}
count=0
code_generated=[]
register_descriptor=[]
address_descriptor=[]
statements=[]
for i in range(t):
    s=input()
    statements.append(s)
    q=list(s.split("="))
    d[str(q[0])]=str(q[1])
for each in d.keys():
    l=[]
   
    c=list(tuple(d[each]))
    if len(R0)==0:
        l.append("MOV")
        l.append(c[0])
        l.append(",")
        l.append("R0")
        if c[1] =="+":
            l.append("ADD")
        if c[1] =="-":
            l.append("SUB")
        l.append(c[2])
        l.append(",")
        l.append("R0")
        R0=each
    elif len(R1)==0:
        l.append("MOV")
        l.append(c[0])
        l.append(",")
        l.append("R1")
        if c[1] =="+":
            l.append("ADD")
        if c[1] =="-":
            l.append("SUB")
        l.append(c[2])
        l.append(",")
        l.append("R1")
        R1=each
    elif c[0]==R0:
        if c[1]=="+":
            l.append("ADD")
        if c[1]=="-":
            l.append("SUB")
        l.append("R1")
        l.append(",")
        l.append("R0")
        R0=each
    code_generated.append(l)
    q=["R0","contains",R0,",","R1","contains",R1 if R1!="" else "_"]
    register_descriptor.append(q)
    q1=[R0, "in", "R0",",",R1 if R1!="" else "_","in","R1"]
    address_descriptor.append(q1)

l=["MOV","R0",",","d"]
code_generated.append(l)

print("Statements Code Generated Register descriptor address descriptor")
for i in range(4):
    print(statements[i]," | ",*code_generated[i]," | ",*register_descriptor[i]," | ",*address_descriptor[i])
final=code_generated[-1][0]+" "+code_generated[-1][1]+" "+code_generated[-1][2]+" "+code_generated[-1][3]
print("\t ",final,end=" ")
print("\t\t\t\t\t    ",end="")
print(*address_descriptor[-1][:3],end=" ")
print("and memory")
#print(address_descriptor)
