# Write an algorithm that takes an array and 
# moves all of the zeros to the end, preserving the 
# order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
def move_zeros(lst):
    dicti=({})
    if len(lst)>1:
        for i in range(len(lst)-1):
            dicti={i: lst[i] for i in range(len(lst))}
        for k in list(dicti.keys()):
            if dicti[k]==0:
                del dicti[k]
    
        lstv=list(dicti.values())
    
        diffe=len(lst)-len(lstv)
        for i in range(diffe):
            lstv.append(0)
            
    return lstv if dicti else lst