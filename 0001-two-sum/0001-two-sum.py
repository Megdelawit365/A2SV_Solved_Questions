class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        for k,v in indices.items():
            num = target - k
            if num in indices:
                if len(indices[num]) > 1 and indices[num][0] != indices[num][1]:
                    return [indices[num][0], indices[num][1]]
                elif v[0] != indices[num][0]:
                    return [v[0],indices[num][0]]
        return []