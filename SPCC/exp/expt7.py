print("If\n\tA->abc|epsilon\n\tB->pqr\nthen,\n\tNumber of unique non-terminals on LHS=2\n\tnon-terminal number 1: A\n\tnon-terminal number 2: B\n\tRHS for non-terminal 1: abc|epsilon\n\tRHS for non-terminal 2: pqr")
print("-"*55)
num=int(input("Enter the number of unique non-terminals on LHS: "))
nt_list=[]
production_list=[]
first_list=[]
follow_list=[]
for i in range(num):
    nt=input(f"Enter non-terminal number {i+1}: ")
    production=input(f"Enter RHS for non-terminal number {i+1}: ")
    nt_list.append(nt)
    production_list.append(production)
    first_list.append([])
    follow_list.append([])
follow_list[0].append('$')

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

print("-"*55)
for i in range(num):
    print(f"{nt_list[i]}\tFIRST: {first_list[i]}\tFOLLOW: {follow_list[i]}")
