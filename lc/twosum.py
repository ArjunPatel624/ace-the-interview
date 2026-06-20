from typing import List

class Solution:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    --> Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    --> Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    --> Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
    
    Only one valid answer exists.
 
    Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        My logic:
        I check every possible pair of different indices. For each index i,
        I compare nums[i] with every number after it. Starting j at i + 1
        makes sure I do not use the same element twice.

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
    def twoSumEnhanced(self, nums: List[int], target: int) -> List[int]:
        """
        My logic:
        I first store each number and its index in a dictionary. This lets me
        quickly check whether the number I need to reach the target exists.

        For each number nums[i], I calculate the difference target - nums[i].
        If that difference exists in the dictionary, then I found the second
        number needed to make the target. I also check that the stored index is
        not the same as i, so I do not use the same element twice.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        indices = {}  # value -> index
        
        for i, n in enumerate(nums):
            diff = target - n
            # Check if the needed number is already in our dictionary
            if diff in indices:
                return [indices[diff], i]
            # If not found, add the current number and its index to the dictionary
            indices[n] = i
        return []
        
# Main method to test the solution(s)
def main():
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))  # [0,1]
    print(solution.twoSum([3,2,4], 6))       # [1,2]
    print(solution.twoSum([3,3], 6))         # [0,1]
    print('-' * 20)
    print(solution.twoSumEnhanced([2,7,11,15], 9))  # [0,1]
    print(solution.twoSumEnhanced([3,2,4], 6))       # [1,2]
    print(solution.twoSumEnhanced([3,3], 6))         # [0,1]

if __name__ == "__main__":
    main()