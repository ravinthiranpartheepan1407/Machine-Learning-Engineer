public class App {
    public static void main(String[] args) throws Exception {

        int[] marks = { 83, 97 };
        studentRank("Ravi", 01, marks);
        float[] floatMarks = { 83.5f, 97.0f };
        System.out.println("Student's Average is: " + " " + studentRank("Ravi", floatMarks));

        // studentMarks("Ravi", 01);
        // System.out.println("Students list: " + " " + students());
    }

    public static String studentMarks(String studentName, int rollNo, int[] marks) {
        switch (studentName) { /* O(n) */
            case "Ravi":
                if (rollNo == 01) {
                    System.out.println("Student Name: " + " " + studentName);
                    System.out.println("Roll No:" + " " + rollNo + " " + "Verified");
                    System.out.println("Maths: " + " " + marks[0] + "," + " " + "English: " + " " + marks[1]);
                }
                break;
            case "Suren":
                if (rollNo == 02) {
                    System.out.println("Student Name: " + " " + studentName);
                    System.out.println("Roll No:" + rollNo + "Verified");
                    System.out.println("Maths: " + " " + marks[0] + "," + " " + "English: " + " " + marks[1]);
                }
                break;

            default:
                break;
        }
        return (studentName);
    }

    public static void studentRank(String studentName, int rollNo, int[] marks) {
        switch (studentName) {
            case "Ravi":
                System.out.println(studentMarks(studentName, rollNo, marks));
                break;
            case "Suren":
                System.out.println(studentMarks(studentName, rollNo, marks));
                break;
            default:
                break;
        }
    }

    public static float studentRank(String studentName, float[] marks) { /*
                                                                          * Method Overloading: Same Func Name with
                                                                          * Different param types
                                                                          */
        float total = 0;
        switch (studentName) {
            case "Ravi":
                for (int scores = 0; scores < marks.length; scores++) {
                    total += marks[scores];
                }
                break;
            case "Suren":
                for (int scores = 0; scores < marks.length; scores++) {
                    total += marks[scores];
                }
                break;
            default:
                break;
        }
        return total / marks.length;
    }

    public static String students() {
        String[] studentName = new String[1];
        studentName[0] = "Ravi";
        return studentName[0]; /* O(1) */
    }
}
