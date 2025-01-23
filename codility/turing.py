def solution(arr):
    """Return a set of 3 digits from the array whose sum equals zero."""
    size = len(arr)
    if size < 3:
        return []

    fi, si, ti = 0, 1, 2

    while True:
        if arr[fi] + arr[si] + arr[ti] == 0:
            return [arr[fi], arr[si], arr[ti]]

        if ti < size - 1:
            ti += 1
        elif si < size - 2:
            si += 1
        elif fi < size - 3:
            fi += 1
        else:
            break

    return []
