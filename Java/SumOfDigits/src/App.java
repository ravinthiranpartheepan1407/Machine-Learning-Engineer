public class App {
    public static void main(String[] args) throws Exception {
        countChars("Hello");
        sumOfDigits(null);
    }

    public static void countChars(String text) {
        for (int i = 0; i < text.length(); i++) {
            System.out.println(text.charAt(i));
        }
    }

    public static void sumOfDigits(int[] values) {
        // sum = values[index]
        // sum = values[0] + values[1]...+values[4]
        values = new int[5];
        values[0] = 25;
        values[1] = 30;
        values[2] = 15;
        values[3] = 10;
        values[4] = 5;

        int sum = 0;

        for (int digits = 0; digits < values.length; digits++) {
            System.out.println(values[digits]);
            // Sum = 0 + 25, sum = 25+30, sum=55+15....
            sum += values[digits];
            System.out.println(sum);
        }

    }
}
