from collections import Counter

class Solution:

    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        list_allowed = set(allowed)
        words_copy = words
        are_allowed = 0

        for word in words_copy:
            set_of_words = set(word)
            print(list_allowed)
            union = set_of_words | list_allowed
            if (union - list_allowed == set()):
                are_allowed += 1
        return are_allowed

    def lengthOfLongestSubstring(self, s: str) -> int:
        my_list = list(s)
        counters = Counter(my_list)
        repeating_chars = [item for item,
                           count in counters.items() if count > 1]
        words = []

        for c in repeating_chars:
            starting_index = 0
            for index, char in enumerate(my_list):
                if (c == char and index > 0):
                    words.append(my_list[starting_index: index])
                    starting_index = index
        if (len(words) > 1):
            return max(len(sublist) for sublist in words)

        return 0

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged: list[int] = nums1+nums2
        return sum(merged)/len(merged)

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
        if len(nums1) != (m+n):
            raise Exception("The length does not match")
        if len(nums2) != n:
            raise Exception("Condition not met")
        if not 0 <= m <= 200 and 0 <= n <= 200:
            raise Exception("Condition not met")
        if not 1 <= (m + n) <= 200:
            raise Exception("Condition not met")

        new_list: list[int] = nums1[:m]+nums2
        return sorted(new_list)

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) < 2 or len(nums) > 10**4:
            return None
        if not self.__checkNumber(target):
            return None
        if len(nums) == 2:
            if (self.__sum(nums[0], nums[1]) == target):
                return [0, 1]
            else:
                return None

        for index, value in enumerate(nums):
            if not self.__checkNumber(value):
                return None
            if index+1 == len(nums)-1:
                if self.__sum(value, nums[index+1]) == target:
                    return [index, index + 1]

            for i in range(index+1, len(nums)):
                if self.__sum(value, nums[i]) == target:
                    return [index, i]

    def __checkNumber(self, number: int) -> bool:
        if -10**9 > number or number > 10**9:
            return False
        return True

    def __sum(self, val1: int, val2: int) -> int:
        return val1 + val2
