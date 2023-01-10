def findMedianSortedArrays(nums1, nums2):

    n1 = len(nums1)
    n2 = len(nums2)

    middle = int(n1 + n2) / 2

    if ((n1 + n2) % 2 != 0):
        return kth(nums1, nums2, 0, n1 - 1, 0, n2 - 1, (n1 + n2) // 2)
    else:
        m1 = kth(nums1, nums2, 0, n1 - 1, 0, n2 - 1, (n1 + n2) // 2)
        m2 = kth(nums1, nums2, 0, n1 - 1, 0, n2 - 1, (n1 + n2) // 2 - 1)
        return (m1 + m2) / 2

def kth(l1, l2, start1, end1, start2, end2, k):
    if start1 > end1:
        return l2[k-start1]
    if start2 > end2:
        return l1[k-start2]
    
    m1 = (start1 + end1) // 2
    m2 = (start2 + end2) // 2
    mv1 = l1[m1]
    mv2 = l2[m2]

    if (m1 + m2) < k:
        if mv1 > mv2:
            return kth(l1, l2, start1, end1, m2 + 1, end2, k)
        else:
            return kth(l1, l2, mv1 + 1, end1, start2, end2, k)
    else:
        if mv1 > mv2:
            return kth(l1, l2, mv1 - 1, end1, start2, end2, k)
        else:
            return kth(l1, l2, start1, end1, mv2 - 1, end2, k)

nums1 = [1, 3]
nums2 = [2]

print(findMedianSortedArrays(nums1, nums2))