## ----- fetch methods name from a file ----- ##

# def get_method_name(path):
    # if path is None:
        # return "no path found"
    # file_texts = "";
    # file_splits = []
    # res = ""
    # f = open(path, "r")
    # for x in f:
        # file_texts += x
    # file_splits = file_texts.split("public void ")
    # for i in file_splits:
        # p = i.split("() throws ")
        # res += p[0] + "\n"
    # print(res)
    
    
# get_method_name(r"C:\Users\kiprajap.ORADEV\Desktop\x.java")


# import pymongo
# from pymongo import MongoClient

# cluster = MongoClient("mongodb+srv://kiran:Abc123!!@cluster0.8xxxn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# print(cluster)

# from collections import defaultdict
# import pdb
# def two_sum(nums, target):
    # D = defaultdict(lambda:-1)
    # for i in range(len(nums)):
        # if D[target-nums[i]] != -1:
            # return [D[target-nums[i]], i]
        # else:
            # D[nums[i]] = i
            
    # return []
    
    
# print(two_sum([2,7,11,15], 9))


# def myAtoi(s):
    # i = 0
    # while i < len(s):
        # if s[i] == "-":
            # i += 1
            # pass
        # elif not s[i].isnumeric():
            # if i < len(s):
                # s = s[:i] + s[i+1:]
            # else:
                # s = s[:i] 
        # else:
            # i += 1
    # return int(s)
    
    
# print(myAtoi("4193 with words"))


def water_level(height):
    low = 0
    high = len(height)-1
    max_area = float("-inf")
    while low < high:
        cur_area = min(height[low], height[high]) * (high-low)
        
        max_area = max(max_area, cur_area)
        if height[low] <= height[high]:
            low += 1
        else:
            high -= 1
    return max_area


# print(water_level([1,8,6,2,5,4,8,3,7]))
# print(water_level([2,3,4,5,18,17,6]))

def findDiagonalOrder(matrix):
    diagonal_order = []
    n = len(matrix)
    m = len(matrix[0])
    i = 0
    j = 0
    while len(diagonal_order) < n * m:
        while i >= 0 and j < m:  # we go upwards
            diagonal_order.append(matrix[i][j])
            i -= 1
            j += 1
        if j == m:
            i += 2
            j = m - 1
        else:
            i = 0
        # while i < n and j >= 0:  # we go downwards
            # diagonal_order.append(matrix[i][j])
            # i += 1
            # j -= 1
        # if i == n:
            # j += 2
            # i = n - 1
        # else:
            # j = 0
    return diagonal_order


# print(findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))



## ------------ get longest unique string 
A = "skmnskdepo"

def LUSUBS(A):
    if len(A) == 1:
        return 1
    cur = A[0]
    max_len = 0
    for i in range(1, len(A)):
        if cur[-1] == A[i]:
            cur = A[i]
        elif A[i] in cur:
            cur = cur[cur.index(A[i]):i+1] + A[i]
        else:
            cur += A[i]
        max_len = max(max_len, len(cur))
    return max_len



print("startedd................")
print(LUSUBS("skmnskdeso"))
print("ended ...................")












