public class App {
    public static void main(String[] args) throws Exception {
        // Simple Program
        checkGrade("B");
        checkGradeAlt(94);
        // Movie Ticketing Program
        MovieTicket("Gold", "A1", 15);
        // School House Team Selection Programm
        schoolHouseSelection(20, "Blue", "Blue");
    }

    public static void checkGrade(String grade) {
        // Use switch when we want to evaluate with one expression or var against
        // multiple scenarios
        // Evaluate: Conditions -> Results in Equality comparisons
        switch (grade) {
            case "A":
                System.out.println("Excellent");
                break;
            case "B":
                System.out.println("Good");
                break;
            default:
                break;
        }
    }

    public static void checkGradeAlt(int gradeComparison) {
        // Use if-else if-else when we want to evaluate multiple expressions with
        // different conditions involves complex logics
        // Evaluate: Conditons -> Results in different actions
        if (gradeComparison >= 90) {
            System.out.println("Ecellent");
        } else if (gradeComparison >= 80 && gradeComparison < 90) {
            System.out.println("Good");
        } else {
            System.out.println("Failed");
        }
    }

    public static void MovieTicket(String ticketType, String selectSeats, int ticketPrice) {
        switch (ticketType) {
            case "Platinum":
                System.out.println("Thanks for choosing Platinum ticket! Please select your seat and pay 20 Euros");
                if (selectSeats != "" && ticketPrice == 20) {
                    System.out.println("Payment Successful for Platinum seat booking" + " " + " Your seat number is:"
                            + " " + selectSeats);
                } else {
                    System.out.println("Payment Failed!");
                }
                break;
            case "Gold":
                System.out.println("Thanks for choosing Gold ticket! Please select your seat and pay 15 Euros");
                if (selectSeats != "" && ticketPrice == 15) {
                    System.out.println("Payment Successful for Gold seat booking" + " " + " Your seat number is:" + " "
                            + selectSeats);
                } else {
                    System.out.println("Payment Failed");
                }
                break;
            default:
                break;
        }
    }

    public static void schoolHouseSelection(int playerNumber, String playerPreference, String teamName) {
        System.out.println("Playe's preference was: " + playerPreference + " "
                + "Let's see which team he's goign to be in: ");
        for (int totalPlayers = 0; totalPlayers <= 90; totalPlayers++) {
            switch (teamName) {
                case "Blue":
                    if (playerNumber <= 30) {
                        System.out.println(
                                "Players Numbers Slot from: " + totalPlayers + " " + "will be in: " + " " + teamName);
                        System.out.println("So your number" + " " + playerNumber + " will be in: " + " " + teamName);
                        break;
                    } else {
                        System.out.println("Not Selected");
                    }
                    break;
                case "Red":
                    if (playerNumber > 30 && playerNumber <= 60) {
                        System.out.println(
                                "Players Numbers from: " + totalPlayers + " " + "will be in: " + " " + teamName);
                        System.out.println("So your number" + " " + playerNumber + " will be in: " + " " + teamName);
                        break;
                    } else {
                        System.out.println("Not Selected");
                    }
                    break;
                case "Green":
                    if (playerNumber > 60 && playerNumber <= 90) {
                        System.out.println(
                                "Players Numbers from: " + totalPlayers + " " + "will be in: " + " " + teamName);
                        System.out.println("So your number" + " " + playerNumber + " will be in: " + " " + teamName);
                        break;
                    } else {
                        System.out.println("Not Selected");
                    }
                    break;
                default:
                    break;
            }
        }
    }
}
