class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)):
            result.append(-1)
            for j in range(len(nums2)-1):
                if nums1[i] == nums2[j]:
                    for k in range(j+1, len(nums2)):
                        print(nums1[i], k, nums2[k])
                        if nums1[i] < nums2[k]:
                            result[i] = nums2[k]
                            break
                    print("\n")
        return result