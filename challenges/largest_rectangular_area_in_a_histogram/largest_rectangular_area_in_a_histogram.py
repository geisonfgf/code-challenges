"""
Largest Rectangular Area in a Histogram

Sample Input
5
1 2 3 4 5

Sample Output
9
        0
      0 0
    1 1 1
  0 1 1 1
0 0 1 1 1
"""

import sys

def get_max_area(buildings, number_of_buildings):
    stack, top, max_area, area_with_top, i = [], 0, 0, 0, 0

    while i < number_of_buildings:
        if stack is None or len(stack) == 0 or buildings[stack[-1]] <= buildings[i]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            area_with_top = buildings[top] * ((i - stack[-1] - 1) if stack else i)
            if max_area < area_with_top:
                max_area = area_with_top

    while stack:
        top = stack.pop()
        area_with_top = buildings[top] * ((i - stack[-1] - 1) if stack else i)
        if max_area < area_with_top:
            max_area = area_with_top

    return max_area

print get_max_area(map(int, raw_input().split(" ")), int(input()))