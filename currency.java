import java.util.Scanner;

public class CurrencyConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Currency Converter");
        System.out.println("1: INR to USD");
        System.out.println("2: INR to EUR");
        System.out.println("3: USD to INR");
        System.out.println("4: EUR to INR");
        System.out.print("Choose an option (1-4): ");
        int choice = scanner.nextInt();
 System.out.print("Enter amount: ");
        double amount = scanner.nextDouble();

        double result = 0.0;
        switch (choice) {
            case 1:
                result = inrToUsd(amount);
                System.out.printf("%.2f INR = %.2f USD%n", amount, result);
                break;
            case 2:
                result = inrToEur(amount);
                System.out.printf("%.2f INR = %.2f EUR%n", amount, result);
                break;
            case 3:
                result = usdToInr(amount);
                System.out.printf("%.2f USD = %.2f INR%n", amount, result);
                break;
