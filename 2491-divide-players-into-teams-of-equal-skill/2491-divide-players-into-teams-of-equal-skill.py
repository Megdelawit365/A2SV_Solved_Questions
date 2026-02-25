class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()
        if len(skill) == 2:
            return skill[0] * skill[1]
        left,right = 0,len(skill)-1
        total = 0
        teams = []
        while left<right:
            skills = skill[left] + skill[right]
            if total == 0:
                total = skills
            elif skills != total:
                return -1
            teams.append([skill[left],skill[right]])
            left += 1
            right -= 1
        ans = 0
        for t in teams:
            ans += t[0]*t[1]
        return ans
        
