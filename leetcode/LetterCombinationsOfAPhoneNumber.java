// 2340 2358

import java.util.ArrayList;
import java.util.List;

public class LetterCombinationsOfAPhoneNumber {
    public static void main(String[] args) {
        LetterCombinationsOfAPhoneNumberSolution sol = new LetterCombinationsOfAPhoneNumberSolution();
        String digits = "23";
//        String digits = "23";
        System.out.println(sol.letterCombinations(digits).toString());
    }
}

class LetterCombinationsOfAPhoneNumberSolution {
    String[] pad = {
            "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };
    ArrayList<String> results = new ArrayList<>();


    public List<String> letterCombinations(String digits) {
        ArrayList<String> ing = new ArrayList<>();
        ing.add("");
        letterCombi(digits, ing);
        if (results.size() == 1) {
            return new ArrayList<>();
        }
        return results;
    }

    public void letterCombi(String digits, List<String> ing) {
        if (digits.isEmpty()) {
            System.out.println(ing.toString());
            results.addAll(ing);
            return;
        }
        List<String> culmulated = new ArrayList<>();
        for (String current : ing) {
            String letters = getPad(digits.charAt(0));
            for (int k = 0; k < letters.length(); k++) {
                String e = current + letters.charAt(k);
                culmulated.add(e);
            }
        }
        letterCombi(digits.substring(1), culmulated);
    }

    private String getPad(char digit) {
        int num = digit - '0';
        return pad[num - 2];
    }
}