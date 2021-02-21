# def two_sum_brute_force(A, target):
#     for i in range(len(A)-1):
#         for j in range(i+1 len(A)):
#             if A[i] + A[j] == target:
#                 print(A[i], A[j])
#                 return True
#     return False

def two_sum_best(A, target):
    i = 0
    j = len(A) - 1
    while i <= j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return False
        
x = [-2, 1, 2, 4, 7, 11]
target = 11

two_sum_best(x, target)