class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        nums = []

        # Flatten the grid
        for row in grid:
            for num in row:
                nums.append(num)

        # Check if conversion is possible
        for num in nums:
            if (num - nums[0]) % x != 0:
                return -1

        # Sort to find median
        nums.sort()
        median = nums[len(nums) // 2]

        # Calculate operations
        operations = 0

        for num in nums:
            operations += abs(num - median) // x

        return operations