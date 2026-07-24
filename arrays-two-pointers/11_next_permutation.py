class Solution {
    public void nextPermutation(int[] nums) {
        if (nums.length < 2) {
            return;
        }
        int p1 = nums.length - 2;
        while (p1 >= 0 && nums[p1] >= nums[p1 + 1]) {
            p1--;
        }
        if (p1 >= 0) {
            int p2 = nums.length - 1;
            while (nums[p2] <= nums[p1]) {
                p2--;
            }
            swap(nums, p1, p2);
        }
        reverse(p1 + 1, nums);
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    private void reverse(int start, int[] nums) {
        int end = nums.length - 1;
        while (start < end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }
}
