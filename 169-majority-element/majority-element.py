class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicts = {}

        for num in nums:
            if num in dicts:
                dicts[num] += 1
            else:
                dicts[num] = 1

        key = max(dicts, key = dicts.get)

        return key 

        