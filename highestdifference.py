import numpy as np
def buy_and_sell(A):
    # max_profit = 0
    # for i in range(len(A)-1):
    #     for j in range(i+1, len(A)):
    #         if A[j] - A[i] > max_profit:
    #             max_profit = A[j] - A[i]
    #             print(max_profit)
    # return max_profit
    # min = A[0]
    # max_profit = 0
    # for i in A:
    #     if i < min:
    #         min = i
    #     elif i > min:
    #         max_profit = i - min
    # print(max_profit)  
    s = np.sort(A)
    return s[-1]-s[0]
    # print(s)
            
           
                
                # TODO: write code...
                
a = [22, 44, 22, 11, 45, 53, 23, 64, 66]
print(buy_and_sell(a))