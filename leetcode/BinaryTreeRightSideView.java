import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class BinaryTreeRightSideView {
    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }


    class Solution {
        class DepthTreeNode {
            TreeNode t;
            int d;

            public DepthTreeNode(TreeNode t, int d) {
                this.t = t;
                this.d = d;
            }
        }

        public List<Integer> rightSideView(TreeNode root) {
            List<Integer> result = new ArrayList<>();
            if (root == null) {
                return result;
            }

            Queue<DepthTreeNode> queue = new LinkedList<>();
            queue.add(new DepthTreeNode(root, 1));
            int prevH = 1;
            int prevV = root.val;
            while (!queue.isEmpty()) {
                DepthTreeNode current = queue.remove();
                if (prevH != current.d) {
                    result.add(prevV);
                }
                if (current.t.left != null) {
                    queue.add(new DepthTreeNode(current.t.left, current.d + 1));
                }
                if (current.t.right != null) {
                    queue.add(new DepthTreeNode(current.t.right, current.d + 1));
                }
                prevH = current.d;
                prevV = current.t.val;
            }
            result.add(prevV);

            return result;
        }

        public List<Integer> rightSideView2(TreeNode root) {
            List<Integer> outResult = new ArrayList<>();
            if (root == null) {
                return outResult;
            }
            nextLevel(root, outResult, 0);
            return outResult;
        }


        public void nextLevel(TreeNode node, List<Integer> outResult, int level) {
            if (node == null) {
                return;
            }
            if (outResult.size() == level) {
                outResult.add(node.val);
            }
            nextLevel(node.right, outResult, level + 1);
            nextLevel(node.left, outResult, level + 1);
        }

    }
}
