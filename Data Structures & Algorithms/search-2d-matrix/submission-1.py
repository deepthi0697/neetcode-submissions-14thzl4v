class Solution:
    def binarySearch(self, arr, target):
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) //2
            if target > arr[mid]:
                l = mid +1
            elif target < arr[mid]:
                r = mid - 1
            elif target == arr[mid]:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            last_ele = matrix[i][len(matrix[i]) - 1]
            first_ele = matrix[i][0]
            if target <= last_ele and target >= first_ele:
                return self.binarySearch(matrix[i], target)

        return False
        