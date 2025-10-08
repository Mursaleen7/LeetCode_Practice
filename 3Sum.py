class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        answer = []
        fixed = 0

        while fixed < len(nums):
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                fixed += 1
                continue

            left = fixed + 1
            right = len(nums) - 1

            while left < right:
                total = nums[fixed] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    answer.append([nums[fixed], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

            fixed += 1

        return answer
