class Solution:
    def shiftGrid(self, grid, k):

        m = len(grid)
        n = len(grid[0])

        # Flatten
        arr = []
        for row in grid:
            arr.extend(row)

        # Reduce unnecessary rotations
        k %= len(arr)

        # Rotate right
        arr = arr[-k:] + arr[:-k]

        # Build the grid again
        ans = []
        index = 0

        for i in range(m):
            ans.append(arr[index:index + n])
            index += n

        return ans