def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    if len(matrix[0]) == 0:
        return False

    i = 0
    starting_point = matrix[i][0]
    if starting_point == target:
        return True

    while starting_point < target and i < len(matrix):
        starting_point = matrix[i][0]
        if starting_point == target:
            return True
        if starting_point < target:
            i += 1
        elif starting_point > target:
            break

    if len(matrix[0]) == 1:
        return False

    # do a binary search of the index that may have
    # the element
    first = 0
    last = len(matrix[i - 1]) - 1
    if matrix[i-1][last] == target:
        return True

    while first < last:
        mid = first + (last - first) // 2
        if matrix[i-1][mid] > target:
            last = mid
        elif matrix[i-1][mid] < target:
            first = mid + 1
        elif matrix[i-1][mid] == target:
            return True

    return False


def main() -> None:
    print(searchMatrix(matrix=[[1,  3]], target=3))


if __name__ == '__main__':
    main()

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
