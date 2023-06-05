public class Mean {
    public static int MeanOut(int[] values) {
        int total = 0;
        for (int elements = 0; elements < values.length; elements++) {
            total += values[elements];
        }
        return total / values.length;
    }
}
