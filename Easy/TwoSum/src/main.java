public class main {
    public static void main(String[] args) {
        int nums[] = new int[]{3, 2, 4};
        int target = 6;
        Solution sol = new Solution();
        int[] answer = sol.twoSum(nums, target);
        System.out.print("The answer is " +  answer[0] + " and " + answer[1]);

    }
}
