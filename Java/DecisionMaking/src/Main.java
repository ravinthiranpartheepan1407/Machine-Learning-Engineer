public class Main {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        postfixAndprefix();
        ternaryOperator();
        calCompundInterest();
    }

    public static void postfixAndprefix() { // Static function must reference to a static func only..
        int dataByte = 128;
        System.out.println(dataByte++);
        System.out.println(++dataByte);
    }

    public static void ternaryOperator() { /* O(1) */
        int fundsRequired = 1500;
        int investedAmount = 1100;
        int fundThreshold = 500;
        int spent = fundsRequired - investedAmount;
        int statusAvailable = spent - fundThreshold;
        int statusNotAvailable = fundThreshold - spent;
        int checkStatus = (spent > fundThreshold) ? (statusAvailable) : (statusNotAvailable); // Ternary operator should
                                                                                              // follow same datatype
                                                                                              // (int ? int : int) or
                                                                                              // (condition or logic or
                                                                                              // func) ? bool :
                                                                                              // bool...
        System.out.println(checkStatus);
    }

    public static void calCompundInterest() { /* O(n) */
        int investment = 1812000;
        int interest = 5;
        int period = 365;

        // Calculating exponent decay or growth
        int threshold = 5000;

        float calCI = investment * interest / 100;
        System.out.println("The compound interest for the 1st annual year 2023 is:" + calCI);
        if (calCI > threshold) {
            float annualCI = (calCI + threshold) * period; // Annual Threshold Trasnfer
            float monthlyCI = (calCI / period) + (threshold / period); // Month thresold
            System.out.println(
                    "The Month threshold is: " + monthlyCI + " " + "and" + " " + "The yearly threshold is: "
                            + annualCI);
        } else {
            calCI -= threshold;
            System.out.println("Withdraw has been made so there will be an exponential decay");
        }
    }
}
