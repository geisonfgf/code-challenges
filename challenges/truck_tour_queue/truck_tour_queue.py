"""
Problem Statement

Suppose there is a circle. There are N petrol pumps on that circle. Petrol
pumps are numbered 0 to (N−1) (both inclusive). You have two pieces of
information corresponding to each of the petrol pump: (1) the amount of
petrol that particular petrol pump will give, and (2) the distance from
that petrol pump to the next petrol pump.

Initially, you have a tank of infinite capacity carrying no petrol. You can
start the tour at any of the petrol pumps. Calculate the first point from
where the truck will be able to complete the circle. Consider that the truck
will stop at each of the petrol pumps. The truck will move one kilometer for
each litre of the petrol.

Input Format

The first line will contain the value of N.
The next N lines will contain a pair of integers each, i.e. the amount of
petrol that petrol pump will give and the distance between that petrol pump
and the next petrol pump.

Constraints:
1<=N<=105
1<=amount of petrol, distance<=109

Output Format

An integer which will be the smallest index of the petrol pump from which
we can start the tour.

Sample Input
3
1 5
10 3
3 4

Sample Output
1

Explanation
We can start the tour from the second petrol pump and visit all.

EX.: gas-station1 - gas-station2 - gas-station2
          -4             7              1
"""

def get_starting_point_of_tour(arr, n):
    start, end = 0, 1
    current_petrol = arr[start][0] - arr[start][1]
    while end != start or current_petrol < 0:
        while current_petrol < 0 and start != end:
            current_petrol -= arr[start][0] - arr[start][1]
            start = (start + 1) % n
            if start == 0:
                return -1
        current_petrol += arr[end][0] - arr[end][1]
        end = (end + 1) % n
    return start

arr, N = [], int(input())
for i in xrange(N):
    arr.append(map(int, raw_input().split(" ")))

print get_starting_point_of_tour(arr, N)