# Problem: Rotate array right by k steps
# Input: [1,2,3,4,5,6,7], k=3 → Output: [5,6,7,1,2,3,4]

def rotate_right(nums, k):
    """O(n) time, O(1) space"""
    k %= len(nums)  # Handle k > len(nums)

    # Reverse whole, then reverse parts
    nums.reverse()  # [7,6,5,4,3,2,1]
    nums[:k] = reversed(nums[:k])  # First k elements
    nums[k:] = reversed(nums[k:])  # Rest
    return nums


def rotate_right_short(nums, k):
    """Return new rotated list, original unchanged"""
    k %= len(nums)
    return nums[-k:] + nums[:-k]

# Usage:
original = [1, 2, 3, 4, 5, 6, 7]
rotated = rotate_right_short(original, 3)
print("Original:", original)  # [1, 2, 3, 4, 5, 6, 7] ← unchanged
print("Rotated:", rotated)    # [5, 6, 7, 1, 2, 3, 4]