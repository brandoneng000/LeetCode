import java.util.HashMap;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> check = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            check.put(target - nums[i], i);
        }
        for(int i = 0; i < nums.length; i++) {
            if(check.containsKey(nums[i]) && i != check.get(nums[i])) {
                return new int[] {i, check.get(nums[i])};
            }
        }

        return new int[] {-1, -1};
    }

}
