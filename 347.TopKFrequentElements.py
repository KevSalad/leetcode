# Given an integer array nums and an integer k, 
# return the k most frequent elements. You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Hash Map, count occurences of each value
        count = {}
        # Array that will be the same size as nums and hold our index's [1, 2, 3]
        freq = [[] for i in range(len(nums) + 1)]

        # Increase the count for that current index
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # Returns key value pair in our dictionary
        for n, c in count.items():
            # At index count, we will append our # in that location 
            freq[c].append(n)

        # Our Top K Frequents Elements 
        res = []
        # freq - 1 starts at the end, all the way to 0, and decrements -1
        for i in range(len(freq) - 1, 0, -1 ):
            for n in freq[i]: 
                res.append(n)
                # Once we have our K elements, we can return the array
                if len(res) == k:
                    return res