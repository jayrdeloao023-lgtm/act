import java.util.Scanner;

class Circle {
void getArea(double radius, double PI) {
    double area = PI * Math.pow(radius, 2);
    System.out.println("Area of the circle: " + area);
}
 public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    Circle circle = new Circle();
    final double PI = 3.14;
    System.out.print("Enter radius of the circle:");
    double radius = scanner.nextDouble();
    circle.getArea(radius, PI);
    scanner.close();    
    }  
}



import java.util.Scanner;

public class loop {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    String password = "12345";
    String enteredPassword;
    int attempts = 0;

    do {
      System.out.print("Enter password: ");
      enteredPassword = scanner.nextLine();

      if (!enteredPassword.equals(password)) {
        System.out.println("Wrong password");
        attempts++;
      }

      if (attempts == 3) {

      }
    } while (password != enteredPassword.equals(password));

    // exit loop and access private
  }

}
