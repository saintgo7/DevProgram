import java.util.Scanner;

/**
 * BMICalculator - Calculate Body Mass Index
 * Provides health category based on BMI value
 */
public class BMICalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== BMI Calculator ===");
        System.out.print("Enter weight (kg): ");
        double weight = scanner.nextDouble();

        System.out.print("Enter height (m): ");
        double height = scanner.nextDouble();

        double bmi = weight / (height * height);

        System.out.printf("\nYour BMI: %.2f%n", bmi);

        String category;
        if(bmi < 18.5) {
            category = "Underweight";
        } else if(bmi < 25) {
            category = "Normal weight";
        } else if(bmi < 30) {
            category = "Overweight";
        } else {
            category = "Obese";
        }

        System.out.println("Category: " + category);
        scanner.close();
    }
}
