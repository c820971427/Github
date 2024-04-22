import self as self


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            len1, len2 = len(nums1), len(nums2)

            left, right, half_len = 0, len1, (len1 + len2 + 1) // 2
            mid1 = (left + right) // 2
            mid2 = half_len - mid1

            while left < right:
                if mid1 < len1 and nums2[mid2 - 1] > nums1[mid1]:
                    left = mid1 + 1
                else:
                    right = mid1
                mid1 = (left + right) // 2
                mid2 = half_len - mid1
                if mid1 == 0:
                    max_of_left = nums2[mid2 - 1]
                elif mid2 == 0:
                    max_of_left = nums1[mid1 - 1]
                else:
                    max_of_left = max(nums1[mid1 - 1], nums2[mid2 - 1])

                if (len1 + len2) % 2 == 1:
                    return max_of_left

                if mid1 == len1:
                    min_of_right = nums2[mid2]
                elif mid2 == len2:
                    min_of_right = nums1[mid1]
                else:
                    min_of_right = min(nums1[mid1], nums2[mid2])

                return (max_of_left + min_of_right) / 2


# # 不考虑时间时间复杂度
# class Solution:
#     def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
#         list_len = len(nums1) + len(nums2)
#         united_list = nums1 + nums2
#         united_list.sort()
#         if list_len % 2:
#             return united_list[int((list_len - 1) / 2)]
#         else:
#             return (united_list[list_len / 2] + united_list[list_len / 2 - 1]) / 2


nums1 = [1, 3]
nums2 = [2]
C = Solution
print(C.findMedianSortedArrays(self, nums1, nums2))
