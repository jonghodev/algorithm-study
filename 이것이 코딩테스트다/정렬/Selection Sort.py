from typing import List

nums = [5, 7, 2, 6, 9, 1, 2, 5]

"""선택 정렬
시간 복잡도: O(N^2)
버블정렬은 안쪽 for 문에서 데이터 교환이 일어나는 반면
선택정렬은 바깥 for 문에서 데이터 교환이 이루어진다.
따라서 교환 횟수는 더 적다고 볼 수 있다.

하지만 버블정렬은 최선의 경우 데이터 이동횟수가 없고
데이터는 실제로 항상 최악의 경우로 배치되지 않는다.
"""
def selection_sort(nums: List[int]):
    for i in range(len(nums)):
        min_idx = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]


selection_sort(nums)

print(nums)
