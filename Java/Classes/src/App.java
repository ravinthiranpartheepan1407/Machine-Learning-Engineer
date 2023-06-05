public class App {
    public static void main(String[] args) throws Exception {
        int[] values = new int[4];
        values[0] = 10;
        values[1] = 15;
        values[2] = 20;
        values[3] = 25;
        StandardDeviation out = new StandardDeviation();
        int result = out.StandardDevOut(values);
        System.out.println("The Standard deviation is: " + " " + result);
    }
}
