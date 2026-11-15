from typing import List


n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here


def flatten(lists: List[List[int]]) -> List[int]:
    results = []
    for i in lists:
        for p in i:
            results.append(p)
    return results


print(flatten(n))
