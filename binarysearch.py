# Binary Search Practice
# Leet Code Problem : 
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

# 1.) Summary of problem:

This problem is a sorting problem basically. Many examples floating around use analogies such as a phonebook, or dictionary to 
give an example of what this problem asks us to do. 
Instead of flipping through every page, you can split the book in half, see if the name is in the top or bottom half, then flip through 
that half again. You keep doing this until you find the name or reach the end. This is basically how this algorithm works, but for 
finding a number in a sorted list.

The "O(log n)" part means that the more numbers you have, the fewer times you need to split the list in half to find the target. So, even
with a million numbers, you might only need to split the list 20 times (around O(log 1,000,000) = 20). That's way faster than checking each 
of those million numbers one by one.
  
# 2.) Test cases

# 3.) Psuedocode solution
