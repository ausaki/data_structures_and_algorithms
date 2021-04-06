# title: count-pairs-with-xor-in-a-range
# detail: https://leetcode.com/submissions/detail/470428838/
# datetime: Sun Mar 21 12:02:22 2021
# runtime: 9544 ms
# memory: 25.1 MB

class TrieNode:
 
    # Function to initialize
    # a Trie Node
    def __init__(self):        
        self.child = [None, None]
        self.cnt = 0
        
def insertTrie(root, N):
      
    # Traverse binary representation of X.
    for i in range(31, -1, -1):
              
        # Stores ith bit of N
        x = bool( (N) & (1 << i))
          
        # Check if an element already
        # present in Trie having ith bit x.
        if(root.child[x] == None):
              
            # Create a new node of Trie.
            root.child[x] = TrieNode()
                  
        # Update count of elements
        # whose ith bit is x
        root.child[x].cnt += 1
          
        # Update root.
        root= root.child[x] 
        
# Function to count elements
# in Trie whose XOR with N
# less than K
def cntSmaller(root, N, K):
      
    # Stores count of elements
    # whose XOR with N exceeding K
    cntPairs = 0
      
    # Traverse binary representation
    # of N and K in Trie
    for i in range(31, -1, -1):       
        if(root == None):
            break
                                     
        # Stores ith bit of N                         
        x = bool(N & (1 << i))
          
        # Stores ith bit of K
        y = K & (1 << i)
          
        # If the ith bit of K is 1
        if (y != 0):
             
            # If an element already
            # present in Trie having
            # ith bit (1 - x)
            if (root.child[x]):
 
                # Update cntPairs
                cntPairs += root.child[ x].cnt
 
            # Update root.
            root = root.child[1 - x]
          
        # If the ith bit of K is 0
        else:
              
            # Update root.
            root = root.child[x]
    return cntPairs
  

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        n = len(nums)
        root = TrieNode()
        a, b = 0, 0
        for i in range(n):
            a += cntSmaller(root, nums[i], high + 1)
            b += cntSmaller(root, nums[i], low)
            # Insert arr[i] into Trie.
            insertTrie(root, nums[i])    
        return a - b