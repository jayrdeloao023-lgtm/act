import java.util.Scanner;

public class ExceptionExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Ask user for a number
            System.out.print("Enter a number: ");
            int num = scanner.nextInt();   // May cause InputMismatchException

            // Division operation
            int result = 100 / num;        // May cause ArithmeticException

            System.out.println("Result: " + result);

        } catch (ArithmeticException e) {
            System.out.println("Error: You cannot divide by zero!");
        
        } catch (Exception e) {
            // Catches any other exception
            System.out.println("An unexpected error occurred: " + e.getMessage());

        } finally {
            // Always runs whether exception occurs or not
            System.out.println("Program has ended. Closing scanner...");
            scanner.close();
        }
    }
}
