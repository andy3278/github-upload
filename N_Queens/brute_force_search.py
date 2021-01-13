import itertools as it 

def is_solution(perm):
    for (i1,i2) in it.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False
    return True

#print(is_solution([1,3,0,2]))
#print(is_solution([3,1,0,2]))

for perm in it.permutations(range(4)):
    if is_solution(perm):
        print(perm)
        exit()