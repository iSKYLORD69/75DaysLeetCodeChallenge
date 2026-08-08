class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        # last[j] = position in word1 where word2[j]
        # can be matched when matching from the right
        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        # If word2 cannot even be matched exactly,
        # we can still potentially use one mismatch.
        
        ans = []
        used_mismatch = False
        j = 0

        for i in range(n):

            if j == m:
                break

            # Exact match: always take it because
            # we want the smallest possible index.
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use our one allowed mismatch
            elif not used_mismatch:

                # Can the remaining characters be matched exactly?
                if j == m - 1 or i < last[j + 1]:
                    ans.append(i)
                    used_mismatch = True
                    j += 1

        if j == m:
            return ans

        return []