import random
t=int(input("Enter no of production : "))
print("Enter productions : ")
d={}
done={}
left={}
count=1
for i in range(t):
q=list(input().split("="))
d[str(q[0])]=str(q[1])
left[q[0]]="T"+str(count)
count+=1
if q[0] not in done.keys():
done[q[0]]=q[0]
# for each in q[1]:
# if each not in ["+","-","*","/"]:
# if each.islower and each in left.keys():
# done[each]=left[each]
print(d)
print(done)
quadruples=[]
result=[]
argument=[]
triples_argument=[]
operator=[]
location=[1,2,3,4]
count=0
operator.append("")
for each in d.keys():
k=[]
args=[]

print(left[each],"=",end="")
s=left[each]+"="
result.append(left[each])
for each1 in d[each]:
if each1 in left.keys():
print(each1,end="")
s+=each1
k.append(each1)
args.append(left[each1][1])
count+=1
else:
if each1 in ["+","-","*","/"]:
operator.append(each1)
else:
k.append(each1)
args.append(each1)
print(each1,end="")
s+=each1
argument.append(k)
quadruples.append(s)
triples_argument.append(args)
print()
# print(quadruples)
# print(result)
# print(operator)
# print(argument)
print("**************Quadruples***************")
print("operator ar1 ar2 result")
for i in range(len(result)):
print(operator[i],*argument[i],result[i],sep=" ")
print("**************triples***************")
print(triples_argument,len(triples_argument))
print("location ar1 ar2 result")
for i in range(len(result)):
print(location[i],operator[i],*triples_argument[i],sep=" ")
print("**************indirect triples***************")
print("location ar1 ar2 result")
n=random.randint(100,300)
for i in range(len(result)):
print(n+i,location[i],operator[i],*triples_argument[i],sep=" ")