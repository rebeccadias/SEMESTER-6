import pandas as pd

n_d=80
print('REBECCA DIAS TE CMPN A 19/182027')

print("If\n\tA->abc|epsilon\n\tB->pqr\nthen,\n\tNumber of unique non-terminals on LHS=2\n\tnon-terminal number 1: A\n\tnon-terminal number 2: B\n\tRHS for non-terminal 1: abc|epsilon\n\tRHS for non-terminal 2: pqr")
print("-"*n_d)
num=int(input("Enter the number of unique non-terminals on LHS: "))
nt_list=[]
production_list=[]
first_list=[]
follow_list=[]
all_ch=set()

for i in range(num):
    nt=input(f"Enter non-terminal number {i+1}: ")
    production=input(f"Enter RHS for non-terminal number {i+1}: ")
    all_ch.add(nt)
    nt_list.append(nt)
    production_list.append(production)
    first_list.append([])
    follow_list.append([])
follow_list[0].append('$')

r=1
later_use=[]
for i in range(len(nt_list)):
    if ("|" not in production_list[i]):
        later_use.append([nt_list[i],production_list[i],r])
        r+=1
    else:
        for p in production_list[i].split("|"):
            later_use.append([nt_list[i],p,r])
            r+=1

for production in production_list:
    if ("|" in production):
        for prod in production.split("|"):
            for ch in prod:
                all_ch.add(ch)
    else:
        for ch in production:
            all_ch.add(ch)
all_ch.add("$")

def nt_present(f_list,production,index,j):
    for first_value in first_list[index]:
        if (first_value=="epsilon"):
            if (j==len(production)-1):
                f_list.append("epsilon") 
            elif (production[j+1] in nt_list):
                nt_present(f_list,production,nt_list.index(production[j+1]),j+1)
            elif (production[j+1] not in nt_list):
                f_list.append(production[j+1])
        else:
            f_list.append(first_value)
    return 
                

for i in reversed(range(num)):
    nt=nt_list[i]
    productions=production_list[i]
    t_productions=productions.split("|")
    j=0
    for production in t_productions:
        if (production=="epsilon"):
            first_list[i].append(production)
            continue
        elif (production[j] not in nt_list):
            first_list[i].append(production[j])
        else:
            index=nt_list.index(production[j])
            nt_present(first_list[i],production,index,j)
                        
def follow_nt_present(p_idx,f_list,production,j):
    nt_index=nt_list.index(production[j])
    
    for first in first_list[nt_index]:
        if (first=="epsilon"):
            if (j==len(production)-1):
                for follow in follow_list[p_idx]:
                    f_list.append(follow)
            elif (production[j+1] not in nt_list):
                f_list.append(production[j+1])
            else:
                follow_nt_present(p_idx,f_list,production,j+1)
        else:
            f_list.append(first)
    return 

for prod_idx,productions in enumerate(production_list):
    for production in productions.split("|"):
            if (production=="epsilon"):
                continue
            else:
                for j in range(len(production)):
                    if (production[j] in nt_list):
                        nt_index=nt_list.index(production[j])
                        if (j==len(production)-1):
                            if (nt_index==prod_idx):
                                continue
                            for follow_value in follow_list[prod_idx]:
                                follow_list[nt_index].append(follow_value)
                        elif (production[j+1] not in nt_list):
                            follow_list[nt_index].append(production[j+1])
                        else:
                            follow_nt_present(prod_idx,follow_list[nt_index],production,j+1)

print("-"*n_d)
for i in range(num):
    print(f"{nt_list[i]}\tFIRST: {first_list[i]}\tFOLLOW: {follow_list[i]}")
print("-"*n_d)
for idx,production in enumerate(production_list):
    if("|" in production):
        production_list[idx]=production.split("|")
    if (type(production_list[idx])==list):
        for ele_idx in range(len(production_list[idx])):
            production_list[idx][ele_idx]="."+production_list[idx][ele_idx]
    else:
        production_list[idx]="."+production_list[idx]

production_list=["."+nt_list[0]]+production_list
nt_list=[nt_list[0]+"'"]+nt_list

#print("All non-terminals:",nt_list)
#print("All productions:",production_list)

state_list=[[[nt_list[0],nt_list[1]],[production_list[0],production_list[1]]]]
for p in state_list[0][1]:
    if (p[1] in nt_list and p[1] not in state_list[0][0]):
        nt_idx=nt_list.index(p[1])
        if (type(production_list[nt_idx])==list):
            num_repeat=len(production_list[nt_idx])
            for _ in range(num_repeat):
                state_list[0][0].append(nt_list[nt_idx])
            for production in production_list[nt_idx]:
                state_list[0][1].append(production)

#print("Initial state list:",state_list)
cpy_state_list=[]
for state in state_list:
    cpy_s=[[],[]]
    for nts in state[0]:
        cpy_s[0].append(nts)
    for prods in state[1]:
        cpy_s[1].append(prods)
    cpy_state_list.append(cpy_s)
    
transitions=[]
def create_states(state_list,new_state_list):
    temp_state_list=[]
    for state in state_list:
        temp_list=[[],[]]
        for nts in state[0]:
            temp_list[0].append(nts)
        for prods in state[1]:
            temp_list[1].append(prods)
    temp_state_list.append(temp_list)
    for state_idx,_ in enumerate(state_list):
        for p_idx,p in enumerate(state_list[state_idx][1]):
            new_state=[[],[]]
            dot_idx=p.index(".")
            if (dot_idx+1==len(p)):
                continue
            else:
                if (dot_idx+2==len(p)):
                    sg=p[:dot_idx]+p[dot_idx+1]+p[dot_idx]
                else:
                    sg=p[:dot_idx]+p[dot_idx+1]+p[dot_idx]+p[dot_idx+2:]
                if (p[dot_idx+1] in nt_list):
                    new_state[0].append(state_list[state_idx][0][p_idx])
                    new_state[1].append(sg)
                    if (dot_idx+2!=len(p) and sg[dot_idx+2] in nt_list):
                        nt_idx=nt_list.index(p[dot_idx+1])
                        if (type(production_list[nt_idx])==list):
                            num_repeat=len(production_list[nt_idx])
                            for _ in range(num_repeat):
                                new_state[0].append(nt_list[nt_idx])
                            for production in production_list[nt_idx]:
                                new_state[1].append(production)
                        else:
                            new_state[0].append(nt_list[nt_idx])
                            new_state[1].append(production_list[nt_idx])
                else:
                    new_state[0].append(state_list[state_idx][0][p_idx])
                    new_state[1].append(sg)
                    if (dot_idx+2!=len(p) and sg[dot_idx+2] in nt_list):
                        nt_idx=nt_list.index(sg[dot_idx+2])
                        if (type(production_list[nt_idx])==list):
                            num_repeat=len(production_list[nt_idx])
                            for _ in range(num_repeat):
                                new_state[0].append(nt_list[nt_idx])
                            for production in production_list[nt_idx]:
                                new_state[1].append(production)
                        else:
                            new_state[0].append(nt_list[nt_idx])
                            new_state[1].append(production_list[nt_idx])
                    
            #temp_state_list.append(state_list[state_idx])
            state_list[state_idx][1][p_idx]=p[dot_idx+1]+p[dot_idx]+p[dot_idx+2:]
            if (new_state not in new_state_list):
                new_state_list.append(new_state)
            transitions.append([state_idx,p[dot_idx+1],new_state_list.index(new_state)+1])
    final_list=temp_state_list+new_state_list
    return final_list,transitions,new_state_list

semi_final_list_1,transitions_1,new_state_list=create_states(state_list,[])
cpy_semi_final_list_1=[]
for state in semi_final_list_1:
    cpy_list=[[],[]]
    for nts in state[0]:
        cpy_list[0].append(nts)
    for prods in state[1]:
        cpy_list[1].append(prods)
    cpy_semi_final_list_1.append(cpy_list)

semi_final_list_2,transitions_2,final_new_state_list=create_states(cpy_semi_final_list_1,new_state_list)
final_list=[]
for l1 in semi_final_list_1:
    if (l1 not in final_list):
        final_list.append(l1)
for l2 in semi_final_list_2:
    if (l2 not in final_list):
        final_list.append(l2)
final_transitions=[]
for t1 in transitions_1:
    if (t1 not in final_transitions):
        final_transitions.append(t1)
for t2 in transitions_2:
    if (t2 not in final_transitions):
        final_transitions.append(t2)
print("Final states:")
for fi,f in enumerate(final_list):
    print(fi,"\tNon-terminals:",f[0],"\tProductions:",f[1])
print("-"*n_d)
print("How to read final transitions?\t[From state number,when received this character,went to this state number]")
print("-"*n_d)
print("Final transitions:")
print(final_transitions)
state_nt=[]
for state_idx,state in enumerate(final_list):
    for p_id,p in enumerate(state[1]):
        if (p[-1]=="."):
            state_nt.append([final_list[state_idx][0][p_id],state_idx,p])

#print("States reduce at:",state_nt)
all_ch_list=list(all_ch)
final_new_state_list=cpy_state_list+final_new_state_list

display_list=[]
for _ in range(len(final_new_state_list)):
    l=[]
    for _ in range(len(all_ch_list)):
        l.append("-")
    display_list.append(l)

df=pd.DataFrame(display_list,columns=all_ch_list)

for t in final_transitions:
    if (t[1] in nt_list):
        df.at[t[0],t[1]]=t[2]
    else:
        df.at[t[0],t[1]]="S"+str(t[2])

#print(df)
#print(state_nt)
#print(later_use)
final=[]
for sn in state_nt:
    for l in later_use:
        if (l[0]==sn[0] and l[1]==sn[2].replace(".","")):
            final.append([l[0],sn[1],l[2]])
#print(final)
#[nt,reduced_at,number]

#print(follow_list)

for i in range(len(final)):
    nt_idx=nt_list.index(final[i][0])-1
    for f in follow_list[nt_idx]:
        df.at[final[i][1],f]="r"+str(final[i][2])
df.at[state_nt[0][1],"$"]="Accept"
print("-"*n_d)
print("Final table below")
print("-"*n_d)
print(df)