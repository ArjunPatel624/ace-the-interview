import time

class Solution:
    """
    Given a string s, find the length of the longest substring without repeating characters.

    A substring is a contiguous sequence of characters within the string.

    --> Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with length 3. Other valid answers include "bca" and "cab".

    --> Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", since all characters are identical.

    --> Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with length 3.
    Note: "pwke" is not valid because it is a subsequence, not a substring.

    Return the length of the longest substring without duplicate characters.
    
    Time Complexity: O(n^2)
    Space Complexity: O(k)
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        I iterate through the string and, for each starting index, use a hashmap
        to store characters seen in the current substring along with their indices.
        I expand forward until I find a repeated character in the hashmap, which
        indicates the substring is no longer valid. I then update the maximum length
        based on the size of the current valid substring.
        """
        char_map = dict()
        maxlen = 0
        for i in range(len(s)):
            char_map.clear() 
            char_map[s[i]] = i 
            for j in range(i+1, len(s)):
                next_char = s[j]
                if next_char in char_map:
                    break
                else:
                    char_map[next_char] = j
            maxlen = max(maxlen, len(char_map))
        return maxlen
    
# Can we do better? The above solution does a lot of work by clearing the hashmap and re-adding characters for each starting index.

    def lengthOfLongestSubstringEnhanced(self, s: str) -> int:
        """
        My logic:
        I use a sliding window approach with a set. I expand the right pointer,
        and if a duplicate is found, I shrink the window from the left until
        it becomes valid again. I keep track of the maximum window size.

        Time Complexity: O(n)
        Space Complexity: O(k)
        """
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    
def main():
    solution = Solution()
    test_cases = ["abcabcbb", "bbbbb", "pwwkew", "", "au", "dvdf"]
    for s in test_cases:
        print(f"Input: s = \"{s}\"")
        start = time.time()
        result1 = solution.lengthOfLongestSubstring(s)
        time1 = time.time() - start
        start = time.time()
        result2 = solution.lengthOfLongestSubstringEnhanced(s)
        time2 = time.time() - start
        print(f"Brute Force Output: {result1} | Time: {time1:.6f}s")
        print(f"Enhanced Output:    {result2} | Time: {time2:.6f}s")
        
if __name__ == "__main__":
    main()