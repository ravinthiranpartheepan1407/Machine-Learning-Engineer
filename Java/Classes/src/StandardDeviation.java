public class StandardDeviation {
    /* Formaula: Variance = (value[index] - mean)^2 */

    public int StandardDevOut(int[] values) {
        /*
         * If object instantitated for Mean like Mean meanCalc = new Mean() it cannot be
         * called because it was created in dynamic manner
         */

        // Accessing the static method in a static way
        int meanOut = Mean.MeanOut(values);
        System.out.println("The mean is: " + " " + meanOut);
        int std = 0;
        for (int elements = 0; elements < values.length; elements++) {
            std += Math.pow((values[elements] - meanOut), 2) / meanOut;
            System.out.println("Standard Deviation: " + " " + std);
        }
        return std;
    }
}
