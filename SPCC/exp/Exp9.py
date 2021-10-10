def quadruples(e ,l):
    a = 0
    if l==3:
        a = 1
        arg2.append(' ')
    else:
        a = 2
    for i in range(a,l):
        if e[i].isalpha():
            if i == 2:
                arg1.append(e[i])
            else:
                arg2.append(e[i])
        elif e[i] in operator:
            op.append(e[i])
    result.append(e[0])
    location[e[0]] = j
    return
print('REBECCA DIAS TE CMPN A 19/182027')
n = int(input('Enter the number of expressions: '))
exp = []
print(f'Enter the {n} expressions in 3 address code:')
for i in range(n):
    exp.append(input())

operator = ['+','-','*','/','^','=']
op = []
arg1 = []
arg2 = []
result = []
j = 0
location = {}
for e in exp:
    quadruples(e,len(e))
    j = j + 1
print('\n__________Quadruples__________\nop\targ1\targ2\tresult\n')
for i in range(n):
    print(op[i],'\t',arg1[i],'\t',arg2[i],'\t',result[i],'\n') 
print('\n____________Triples____________\nlocation\top\targ1\targ2\n')
for i in range(n):
    if arg1[i] in location and arg2[i] in location:
        print(i,'\t\t',op[i],'\t',location[arg1[i]],'\t',location[arg2[i]])
    elif arg1[i] in location:
        print(i,'\t\t',op[i],'\t',location[arg1[i]],'\t',arg2[i])
    elif arg2[i] in location:
        print(i,'\t\t',op[i],'\t',arg1[i],'\t',location[arg2[i]])
    else:
        print(i,'\t\t',op[i],'\t',arg1[i],'\t',arg2[i])
print('\n_________Indirect Triples_________\nlocation\top\targ1\targ2\n')
j = 1001
for i in range(n):
    if arg1[i] in location and arg2[i] in location:
        print(j,'\t\t',op[i],'\t',location[arg1[i]],'\t',location[arg2[i]])
    elif arg1[i] in location:
        print(j,'\t\t',op[i],'\t',location[arg1[i]],'\t',arg2[i])
    elif arg2[i] in location:
        print(j,'\t\t',op[i],'\t',arg1[i],'\t',location[arg2[i]])
    else:
        print(j,'\t\t',op[i],'\t',arg1[i],'\t',arg2[i])
    j = j + 1