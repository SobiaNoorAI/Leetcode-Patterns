class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left= 0
        right= left+1
    
        # run loop to check all elements
        for right in range(len(nums)):
            # if no unique element then continue searching
            if nums[right]==nums[left]:
                right+=1
            
            # if unique element is fouond then swap
            else:
                left+=1

                nums[left]= nums[right]
        # return unique elements   
        return left+1
            
        