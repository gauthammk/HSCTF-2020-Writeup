public class Reverse {
    public static void main(String[] args) {
        String output = "inagzgkpm)Wl&Tg&io";
        System.out.println(unshift(unshift2(output)));
    }

    public static String unshift2(String input) {
        String ret = "";
        for (int i = 0; i < input.length(); i++) {
            ret += (char) (input.charAt(i) - Integer.toString((int) input.charAt(i)).length());
        }
        return ret;
    }

    public static String unshift(String input) {
        String ret = "";
        for (int i = 0; i < input.length(); i++) {
            ret += (char) (input.charAt(i) + i);
        }
        return ret;
    }

}