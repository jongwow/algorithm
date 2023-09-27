// 2259 2334

import java.util.HashMap;
import java.util.Map;

public class ImplementTrie {
    public static void main(String[] args) {
        Trie trie = new Trie();
        trie.insert("apple");
        System.out.println(trie.search("apple"));
        System.out.println(trie.search("app"));
        System.out.println(trie.startsWith("app"));
        trie.insert("app");
        System.out.println(trie.search("app"));
    }
}

class Trie {

    // 이건 없애도 될 듯.
    private boolean exist = false;
    private Map<String, Trie> child = new HashMap<>();

    public Trie() {

    }

    public void insert(String word)  {
        if (word.isEmpty()) {
            exist = true;
            return;
        }
        String current = word.substring(0, 1);
        String rest = word.substring(1);
        if (child.containsKey(current)) {
            child.get(current).insert(rest);
            return;
        }
        Trie trie = new Trie();
        child.put(current, trie);
        trie.insert(rest);
    }

    public boolean search(String word) {
//        System.out.println(word);
        if (word.isEmpty()) {
            return exist;
        }
        String current = word.substring(0, 1);

        if (child.containsKey(current)) {
            return child.get(current).search(word.substring(1));
        }
        return false;
    }

    public boolean startsWith(String prefix) {
        if (prefix.isEmpty()) {
            return false;
        }
        String current = prefix.substring(0, 1);
        if (prefix.length() == 1) {
            return child.containsKey(current);
        }
        if (child.containsKey(current)) {
            return child.get(current).startsWith(prefix.substring(1));
        }
        return false;
    }
}