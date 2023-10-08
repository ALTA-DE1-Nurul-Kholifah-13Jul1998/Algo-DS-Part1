def max_sequence(arr):
    if not arr:
        return 0
    start = arr[0]
    end = arr[0]
    for i in arr[1:]: #start index 1 atau elemen k2
        start = max(i, start+i) #mengambil nilai max i/(start+i)
        end = max(end, start)

    return end

if __name__ == "__main__":
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_sequence([-2, -5, 6, -2, -3, 1, 5, -6]))    # 7
    print(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]))    # 7
    print(max_sequence([-2, -5, 6, -2, -3, 1, 6, -6]))    # 8
    print(max_sequence([-2, -5, 6, 2, -3, 1, 6, -6]))     # 12