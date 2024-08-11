int minSubArrayLen(int target, int* nums, int numsSize) {
        int low, high, sub_sum, global_min, sub_min;
        low = high = global_min = 0;
        sub_sum = nums[low];
        while (low < numsSize) {
            while (sub_sum < target && high+1 < numsSize)
                sub_sum += nums[++high];

            if (sub_sum < target)
                break;

            while (sub_sum - nums[low] >= target)
                sub_sum -= nums[low++];

            sub_min = high - low + 1;
            if (!global_min || sub_min < global_min)
                global_min = sub_min;

            sub_sum -= nums[low++];
        }
        return global_min;
}