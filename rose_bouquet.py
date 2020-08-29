# Given an array of roses. roses[i] means rose i will bloom on day roses[i]. Also given an int k, which is the minimum number of adjacent bloom roses required for a bouquet, and an int n, which is the number of bouquets we need. Return the earliest day that we can get n bouquets of roses.
#
# Example:
# Input: roses = [1, 2, 4, 9, 3, 4, 1], k = 2, n = 2
# Output: 4
# Explanation:
# day 1: [b, n, n, n, n, n, b]
# The first and the last rose bloom.
#
# day 2: [b, b, n, n, n, n, b]
# The second rose blooms. Here the first two bloom roses make a bouquet.
#
# day 3: [b, b, n, n, b, n, b]
#
# day 4: [b, b, b, n, b, b, b]
# Here the last three bloom roses make a bouquet, meeting the required n = 2 bouquets of bloom roses. So return day 4.

#DOES NOT WORK
#HALF WRITTEN
#-ADITYA
def mindays(roses, n, k):
    bloomed = ['n'] * len(roses)
    days = max(roses)
    for i in range(days):
        for j in range(len(roses)):
            if i == roses[j]:
                bloomed[j] = 'b'
                for l in range(k):
                    if bloomed[j+l] == 'b':
                        break


roses = [1, 2, 4, 9, 3, 4, 1]
n = 2
k = 2
mindays(roses, n, k)