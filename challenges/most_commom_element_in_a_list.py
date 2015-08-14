"""
Your task is to find the most popular holiday destination from a list of
destinations searched for by users.
 
You are given as standard input the integer size of the list, followed by
the names of the destinations themselves.
 
The input has the following format:
 
on the first line, the count of items in the list
on the subsequent lines, the name of each destination searched for, one per
line (each destination is a single word with no spaces, destinations can be
searched for and appear more than once)
 
The input is correct. There is at least one destination in the input.
 
Write a program that reads the input from stdin and then outputs out the name
of the most searched for destination i.e. the destination that appears most
in the list.  One destination is guaranteed to be the outright winner in the
input.
 
Examples: 
 
Input:                      Input:
6                           5
Barcelona                   Singapore
Edinburgh                   Bangkok
Barcelona                   Singapore
Miami                       Bangkok
Miami                       Singapore
Barcelona
 
Output:                     Output:
Barcelona                   Singapore
"""

input1 = ["Barcelona", "Edinburgh", "Barcelona", "Miami", "Miami", "Barcelona"]
output1 = "Barcelona"
input2 = ["Singapore", "Bangkok", "Singapore", "Bangkok", "Singapore"]
output2 = "Singapore"

# Decorator to check eficience in time
def st_time(func):
    """ st decorator to calculate the total time of a func """
    from time import time
    def st_func(*args, **keyArgs):
        t1 = time()
        r = func(*args, **keyArgs)
        t2 = time()
        print "Function=%s, Time=%s", (func.__name__, t2 - t1)
        return r

    return st_func

# Get most commom element in a list using python libs
@st_time
def get_most_commom_element_in_a_list_using_python_libs(list):
    from collections import Counter
    return Counter(list).most_common(1)[0][0]

print get_most_commom_element_in_a_list_using_python_libs(input1)
print ""
print get_most_commom_element_in_a_list_using_python_libs(input2)
print ""

# Get most commom element in a list from scratch
def binary_search(A, n, x, search_first):
    low, high, result = 0, n - 1, -1
    while low <= high:
        mid = (low + high) / 2
        if A[mid] == x:
            result = mid
            if search_first:
                high = mid - 1
            else:
                low = mid + 1
        elif x < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return result

def find_count(A, n, x):
    first = binary_search(A, n, x, True)
    last =  binary_search(A, n, x, False)
    return last - first + 1

@st_time
def get_most_commom_element_in_a_list_from_scratch(list):
    return sorted([[find_count(list, len(list), element), element]
                    for element in set(list)])[-1][1]

print get_most_commom_element_in_a_list_from_scratch(input1)
print ""
print get_most_commom_element_in_a_list_from_scratch(input2)
