

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        count = {}
        max_len = 0

        for right in range(len(fruits)):
            fruit = fruits[right]

            count[fruit] = count.get(fruit, 0) + 1

           
