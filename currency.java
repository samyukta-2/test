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

