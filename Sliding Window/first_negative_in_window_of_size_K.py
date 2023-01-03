#ques link- https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1


def printFirstNegativeInteger( A, N, K):
    # code here
    i, j = 0,0
    res = []
    ans = []
    while j < N:
        if A[j] < 0:
           res.append(A[j]) 
        if j - i + 1 < K:
            j += 1
        elif j - i + 1 == K:
            if not res:
                ans.append(0)
            else:
                ans.append(res[0])
                if A[i] == res[0]:
                    res.pop(0)
            i += 1
            j += 1
    return ans