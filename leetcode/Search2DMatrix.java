import java.util.Arrays;

public class Search2DMatrix {
    public static void main(String[] args) {
        int[][] given = {{1}};
//        int[][] given = {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}};
        System.out.println(solve(given, 0));
    }
    // 9 m 16 s
    public static boolean solve(int[][] matrix, int target){
        // 양옆으로 binary search
        // row에 대해서 bs
        int m = matrix.length;
        int n = matrix[0].length;
        int top = m - 1;
        int bottom = 0;
        int mid = (top + bottom) / 2;
        while (top - bottom >= 0) {
            mid = (top + bottom) / 2;
            if (matrix[mid][0] == target) {
                return true;
            }
            if (matrix[mid][0] > target){
                top = mid - 1;
            } else{
                bottom = mid + 1;
            }
        }
        int targetRow = bottom -1; // zero-index
        if (targetRow < 0) {
            return false;
        }
        bottom = 0;
        top = n - 1;
        mid = (top + bottom) / 2;
        while (top - bottom >= 0) {
            mid = (top + bottom) / 2;
            if (matrix[targetRow][mid] == target) {
                return true;
            }
            if (matrix[targetRow][mid] > target){
                top = mid - 1;
            } else{
                bottom = mid + 1;
            }
        }
        return false;
    }


}
