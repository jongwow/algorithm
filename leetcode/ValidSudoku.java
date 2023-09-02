import java.util.HashMap;

class Solution {
    public boolean isValidSudoku(char[][] board) {
        // 1. check col
        for (char[] chars : board) {
            HashMap<Character, Boolean> map = new HashMap<>();
            for (char ch : chars) {
                if (ch != '.' && map.containsKey(ch)) {
                    return false;
                }
                map.put(ch, true);
            }
        }
        // 2. check row
        for (int col = 0; col < board[0].length; col++) {
            HashMap<Character, Boolean> map = new HashMap<>();
            for (char[] chars : board) {
                char ch = chars[col];
                if (ch != '.' && map.containsKey(ch)) {
                    return false;
                }
                map.put(ch, true);
            }
        }
        // 3. check square
        for (int startR = 0; startR < 9; startR += 3) {
            for (int startC = 0; startC < 9; startC += 3) {
                HashMap<Character, Boolean> mp = new HashMap<>();
                for (int r = 0; r < 3; r++) {
                    for (int c = 0; c < 3; c++) {
                        char ch = board[startR + r][startC + c];
                        if (ch != '.' && mp.containsKey(ch)) {
                            return false;
                        }
                        mp.put(ch, true);
                    }
                }
            }
        }
        return true;
    }
}

public class ValidSudoku {
    public static void main(String[] args) {

        Solution sol = new Solution();
        char[][][] boards =
                {
                        {
                                {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
                                {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
                                {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
                                {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
                                {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
                                {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
                                {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
                                {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
                                {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
                        },
                        {
                                {'8', '3', '.', '.', '7', '.', '.', '.', '.'},
                                {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
                                {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
                                {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
                                {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
                                {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
                                {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
                                {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
                                {'.', '.', '.', '.', '8', '.', '.', '7', '9'},
                        },
                        {
                                {'.', '.', '4', '.', '.', '.', '6', '3', '.'},
                                {'.', '.', '.', '.', '.', '.', '.', '.', '.'},
                                {'5', '.', '.', '.', '.', '.', '.', '9', '.'},
                                {'.', '.', '.', '5', '6', '.', '.', '.', '.'},
                                {'4', '.', '3', '.', '.', '.', '.', '.', '1'},
                                {'.', '.', '.', '7', '.', '.', '.', '.', '.'},
                                {'.', '.', '.', '5', '.', '.', '.', '.', '.'},
                                {'.', '.', '.', '.', '.', '.', '.', '.', '.'},
                                {'.', '.', '.', '.', '.', '.', '.', '.', '.'}
                        }
                };


        for (char[][] board : boards) {
            boolean result = sol.isValidSudoku(board);
            System.out.println(result);
        }

    }
}