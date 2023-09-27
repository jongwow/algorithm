import java.util.LinkedList;
import java.util.Queue;

// 0033 ~ 0049
public class NumberOfIslands {
    class Pair {
        int row, col;

        public Pair(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }

    public static int[] dr = new int[]{0, 0, -1, 1};
    public static int[] dc = new int[]{1, -1, 0, 0};


    public int numIslands(char[][] grid) {
        int cnt = 1;
        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[0].length; col++) {
                if (grid[row][col] == '1') {
                    cnt += 1;
                    Queue<Pair> queue = new LinkedList();
                    queue.add(new Pair(row, col));
                    char c = (char) (cnt + '0');
                    grid[row][col] = c;
                    while (!queue.isEmpty()) {
                        Pair cur = queue.remove();
                        // adjacent available
                        for (int d = 0; d < 4; d++) {
                            int newR = cur.row + dr[d];
                            int newC = cur.col + dc[d];
                            if (0 <= newR && newR < grid.length && 0 <= newC && newC < grid[0].length) {
                                if (grid[newR][newC] == '1') {
                                    grid[newR][newC] = c;
                                    queue.add(new Pair(newR, newC));
                                }
                            }
                        }
                    }
                }
            }
        }
        return cnt - 1;
    }

}
