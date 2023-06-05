// Variance, Mean, Median
// Min-Max Scaling
// Z-Score
// Modified Z-Score
// Freeman Diaconis
// Rank Transform
// Probability
// Shannon Entropy
// Skewness and Kurtosis
// Fano Factor and Co-efficient of Variance

public class StatLib {
    public static void main(String[] args) throws Exception {
        Mean(null);
        Variance(null);
    }

    public static void Mean(int[] values) {
        // Set array size
        int[] input_size = new int[4];
        System.out.println(input_size.length);
        // Insert values
        values = new int[input_size.length];
        values[0] = 15;
        values[1] = 25;
        values[2] = 75;
        values[3] = 50;

        int summation = 0;
        for (int digits = 0; digits < values.length; digits++) {
            summation += values[digits];
            System.out.println(summation);
            float CalcMean = summation / input_size.length;
            System.out.println("The mean is: " + " " + CalcMean);
        }
    }

    public static void Variance(int[] values) {
        // Set array size
        int[] input_size = new int[4];
        // Insert values
        values = new int[input_size.length];
        values[0] = 15;
        values[1] = 25;
        values[2] = 75;
        values[3] = 50;
        System.out.println(values);
        int summation = 0;
        for (int digits = 0; digits < values.length; digits++) {
            summation += values[digits];
            System.out.println("Summation of digits: " + " " + summation);
            float calcVariance = (values[digits] - (summation / input_size.length)) ^ 2;
            System.out.println("The variance is: " + " " + calcVariance);
        }
    }
}
