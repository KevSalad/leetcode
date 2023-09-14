class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Last Index in nums1
        last = (m + n) - 1
    
        # Merge in Reverse
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                # Essentially moving this right
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                # nums1[m - 1] < num2[n - 1]
                nums1[last] = nums2[n - 1]
                n -= 1
            # move last pointer iterator left
            last -= 1
        
        # Finish iterating through the second array, even once there is no more nums1 to compare to
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1