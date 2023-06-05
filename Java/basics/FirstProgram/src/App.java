// public class App {
//     public static void main(String[] args) throws Exception {
//         System.out.println("Hello, World!");
//     }
// }

public class App {
    public static void main(String[] args) throws Exception {
        int a = 10;
        System.out.println("Java");
        System.out.println("Programming");
        System.out.println(a);

        TypeCast(args);
        BoolType();
    }

    public static void TypeCast(String[] args) {
        int a = 10;
        float typeCast = a;
        System.out.println(typeCast);
    }

    public static void BoolType() {
        String data = "Data Present";
        Boolean exist = true;
        Boolean notExist = false;
        System.out.println(data);
        if (data == "Data Present") {
            System.out.println(exist);
        } else {
            System.out.println(notExist);
        }
    }

}