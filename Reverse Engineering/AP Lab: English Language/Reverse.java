public class Reverse {
    public static void main(String[] args) {
        String output = "1dd3|y_3tttb5g`q]^dhn3j";
        for (int i = 0; i < 3; i++) {
            output = rev_xor(output);
            output = rev_transpose(output);
        }
        System.out.println(output);
    }

    public static String rev_transpose(String input) {
        int[] new_transpose = { 11, 19, 7, 20, 16, 6, 9, 13, 4, 22, 21, 0, 8, 14, 15, 2, 17, 5, 1, 3, 18, 10, 12 };
        String ret = "";
        for (int i : new_transpose) {
            ret += input.charAt(i);
        }
        return ret;
    }

    public static String rev_xor(String input) {
        int[] xor = { 4, 1, 3, 1, 2, 1, 3, 0, 1, 4, 3, 1, 2, 0, 1, 4, 1, 2, 3, 2, 1, 0, 3 };
        String ret = "";
        for (int i = 0; i < input.length(); i++) {
            ret += (char) (input.charAt(i) ^ xor[i]);
        }
        return ret;
    }
}
