class Solution(object):
    def search(self, nums, target):
        l = 0
        h = len(nums)-1
        
        while l<h:
            mid = l+((h-l)//2)

            if nums[mid] == target:
                return mid
            
            # If the lower half is sorted check if the target is in that half
            if nums[l] <= nums[mid]:
                # If target in sorted lower half decrease high
                if target < nums[mid] and target >= nums[l]:
                    h = mid-1
                # Else increase low
                else:
                    l = mid + 1
            
            # Else the upper half must be sorted
            else:
                if target > nums[mid] and target <= nums[h]:
                    l = mid+1
                else:
                    h = mid-1
        
        if nums and target == nums[l]:
            return l
        return -1
                    