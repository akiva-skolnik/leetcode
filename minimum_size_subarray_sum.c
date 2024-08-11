int minSubArrayLen(int target, int* nums, int numsSize) {
        int low, high, sub_sum, global_min;
        low = high = global_min = sub_sum = 0;
        while (high < numsSize) {
            sub_sum += nums[high++];

            while (sub_sum >= target) {
                global_min = (!global_min || high - low < global_min) ? high - low : global_min;
                sub_sum -= nums[low++];
            }
        }
        return global_min;
}