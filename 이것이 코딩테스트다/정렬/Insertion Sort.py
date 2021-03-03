from typing import List

nums = [14, 7, 2, 6, 9, 1, 2, 5]


"""삽입 정렬
시간 복잡도: O(N^2)
정렬되어있는 경우 매우 빠르게 동작한다.

보통의 경우에는 퀵 정렬보다 느리지만
정렬이 거의 되어있는 상황에서는 퀵정렬보다 강력하다.
"""
def insertion_sort(nums: List[int]):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break

insertion_sort(nums)

print(nums)
