def merge(arr1, arr2):
    m, n = len(arr1), len(arr2)

    
    def nextGap(gap):
        return 0 if gap <= 1 else (gap // 2) + (gap % 2)

    gap = nextGap(m + n)

    while gap > 0:
        i = 0
        
        while i + gap < m:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1

      
        j = gap - m if gap > m else 0
        while i < m and j < n:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

    
        if j < n:
            k = 0
            while j + k + gap < n:
                if arr2[j + k] > arr2[j + k + gap]:
                    arr2[j + k], arr2[j + k + gap] = arr2[j + k + gap], arr2[j + k]
                k += 1

        gap = nextGap(gap)



arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merge(arr1, arr2)

print("arr1 =", arr1)
print("arr2 =", arr2)
