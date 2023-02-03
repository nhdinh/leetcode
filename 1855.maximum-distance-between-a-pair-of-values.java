// 1855. Maximum Distance Between a Pair of Values

class Solution {
    public int maxDistance(int[] nums1, int[] nums2) {
        int i = 0, j = 0;
        int n = nums1.length;
        int m = nums2.length;
        int max = 0;
        while (i < n && j < m) {
            if (nums1[i] > nums2[j])
                i++;
            else {
                max = Math.max(max, j - i);
                j++;
            }
        }
        return max;
    }
}
