import pytest

from solution import Solution


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize("list, target, expected", [
    ([2], 5, None),
    ([2, 2], -10**9, None),
    ([2, 2], 10**9, None),
    ([2, 10**9], 3, None),
    ([-10**9, 1], 3, None)
])
def test_negative_solution(list, target, expected, sol) -> None:
    assert sol.twoSum(list, target) is expected


@pytest.mark.parametrize("list, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([3, 1, 3], 6, [0, 2]),
    ([3, 1, 2, 3], 6, [0, 3]),
    ([3, 1, 2, 3], 5, [0, 2]),
    ([3, 1, 2, 3], 3, [1, 2]),
    ([1, 1, 2, 3], 5, [2, 3])
])
def test_positive_solution(list, target, expected, sol) -> None:
    assert sol.twoSum(list, target) == expected


@pytest.mark.parametrize("lnums1, m, nums2, n, expected", [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1])
])
def test_positive_merge(lnums1: list[int], m: int, nums2: list[int], n: int, expected, sol) -> None:
    assert sol.merge(lnums1, m, nums2, n) == expected


@pytest.mark.parametrize("nums1, nums2, expected", [
    ([1, 3], [2], 2.00000),
    ([1, 2], [3, 4], 2.50000)
])
def test_findMedianSortedArrays(nums1: list[int], nums2: list[int], expected, sol) -> None:
    assert sol.findMedianSortedArrays(nums1, nums2) == expected


@pytest.mark.parametrize("allowed, words, expected", [
    ("ab", ["ad", "bd", "aaab", "baa", "badab"], 2),
    ("abc", ["a","b","c","ab","ac","bc","abc"], 7),
    ("cad", ["cc","acd","b","ba","bac","bad","ac","d"], 4)
])
def test_countConsistentStrings(allowed: str, words: list[str], expected: int, sol: Solution) -> None:
    assert sol.countConsistentStrings(allowed, words) == expected

@pytest.mark.parametrize("s, expected", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3)
])
def test_lengthOfLongestSubstring(s: str, expected, sol) -> None:
    assert sol.lengthOfLongestSubstring(s) == expected
