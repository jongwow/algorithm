import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;
import java.util.TreeSet;

public class snakesAndLadders {
    public static void main(String[] args) {
        System.out.println("Hello World");
//        int[][] given = {
//                {1, 1, -1},
//                {1, 1, 1,},
//                {-1, 1, 1}
//        };
        int[][] given = {
                {-1, -1, 19, 10, -1},
                {2, -1, -1, 6, -1},
                {-1, 17, -1, 19, -1},
                {25, -1, 20, -1, -1},
                {-1, -1, -1, -1, 15}
        };

//        int[][] given = {
//                {-1, -1},
//                {-1, 3},
//        };
//        int[][] given = {
//                {-1, -1, -1},
//                {-1, 9, 8},
//                {-1, 8, 9}
//        };
//        int[][] given = {
//                {-1, -1, -1, -1, -1, -1},
//                {-1, -1, -1, -1, -1, -1},
//                {-1, -1, -1, -1, -1, -1},
//                {-1, 35, -1, -1, 13, -1},
//                {-1, -1, -1, -1, -1, -1},
//                {-1, 15, -1, -1, -1, -1}
//        };
        MySnakeAndLadders solution = new MySnakeAndLadders();
        System.out.println(solution.solve(given));
    }


}

class MySnakeAndLadders {
    class Pair {
        int Pos;
        int Depth;

        public Pair(int pos, int depth) {
            Pos = pos;
            Depth = depth;
        }
    }

    public int solve(int[][] board) {
        int n = board.length;
        // 1부터 시작
        Queue<Pair> queue = new LinkedList<>();
        Set<Integer> visited = new TreeSet<>();
        queue.add(new Pair(1, 0));
        // queue
        while (!queue.isEmpty()) {
            Pair current = queue.remove();
            if (visited.contains(current.Pos)) {
                continue;
            }
            visited.add(current.Pos);
            System.out.println("Current: " + current.Pos + ", " + current.Depth);
            if (current.Pos == n * n) {
                return current.Depth;
            }
            int[] next = getNext(current.Pos, n);
            if (next[1] == n * n) {
                queue.add(new Pair(next[1], current.Depth + 1));
                continue;
            }
            for (int i = next[0]; i <= next[1]; i++) {
                int[] coord = currentToCoordinate(i, n);
                if (board[coord[0]][coord[1]] != -1) {
                    queue.add(new Pair(board[coord[0]][coord[1]], current.Depth + 1));
                } else {
                    queue.add(new Pair(i, current.Depth + 1));

                }
            }
        }
        return -1;
    }

    public int[] currentToCoordinate(int curr, int n) {
        int row = (n - 1) - (curr - 1) / n;
        int col = (curr - 1) % n;
        if (((curr - 1) / n) % 2 != 0) {
            col = n - 1 - col;
        }
        return new int[]{row, col};
    }

    public int[] getNext(int curr, int n) {
        int start = curr + 1;
        int end = curr + 6 < n * n ? curr + 6 : n * n;
        return new int[]{start, end};
    }

}
