import java.util.ArrayList;
import java.util.List;

public class MaximumSubarray {
    public static void main(String[] args) {
        MaximumSubarraySolution sol = new MaximumSubarraySolution();
//        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
//        int[] nums = {1};
//        int[] nums = {5,4,-1,7,8};
//        int[] nums = {-2,1};
//        int[] nums = {-2,-1};
        int[] nums = {-2};
        int res = sol.maxSubArray(nums);
        System.out.println(res);

    }
}

class MaximumSubarraySolution {
    public int maxSubArray(int[] nums) {
        // partial sum 하면서 확인
        List<Integer> partialSum = new ArrayList<>();
        partialSum.add(0);
        int smallest = 0;
        int answer = nums[0];
        for (int i = 0; i < nums.length; i++) {
            int current = partialSum.get(i) + nums[i];
            partialSum.add(current);
            if (answer < current - smallest) {
                answer = current - smallest;
            }
            if (current < smallest) {
                smallest = current;
            }
        }
        return answer;
    }
}
//[-2, 1, -3, 4, -1, 2, 1, -5, 4],
//        [1],
//        [5, 4, -1, 7, 8],
//[-1],
//        [-2, -1],
//        [-2, -1, -3],
//        [-2, 0, -3, -3],
//        [0, -3, 1, 1]