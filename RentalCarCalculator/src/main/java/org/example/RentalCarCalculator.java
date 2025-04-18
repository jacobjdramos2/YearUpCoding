package org.example;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class RentalCarCalculator {
    public String date;
    public int numDays;
    public Scanner sc = new Scanner(System.in);

    public RentalCarCalculator(String d, int nd) {
        date = d;
        numDays = nd;
    }

    public boolean electronicTag() {
        System.out.println("Do you want an electronic toll tag? (yes/no): ");
        String ans = sc.nextLine();
        ans = ans.toLowerCase();
        if (ans.equals("yes")) {
            return true;
        } else if (ans.equals("no")) {
            return false;
        } else {
            System.out.println("Please type yes or no.");
        }

        return false;
    }

    public boolean wantGPS() {
        System.out.println("Do you want a GPS at $2.95/day? (yes/no): ");
        String ans = sc.nextLine();
        ans = ans.toLowerCase();
        if (ans.equals("yes")) {
            return true;
        } else if (ans.equals("no")) {
            return false;
        } else {
            System.out.println("Please type yes or no.");
        }

        return false;
    }

    public boolean wantRoadSideAssistance() {
        System.out.println("Do you want roadside assistance at $3.95/day? (yes/no): ");
        String ans = sc.nextLine();
        ans = ans.toLowerCase();
        if (ans.equals("yes")) {
            return true;
        } else if (ans.equals("no")) {
            return false;
        } else {
            System.out.println("Please type yes or no.");
        }

        return false;
    }

    public double surCharge(int age) {

        return (age < 25) ? 0.30 : 0.0;
    }

    public double calculatePrice(int age) {
        double basicRental = 29.99;

        double surCharge = 0;
        if (age < 25) {
            surCharge = surCharge(age);
        }

        double total = basicRental * numDays * (1 + surCharge);

        if (electronicTag()) {
            total += 3.95 * numDays;
        }

        if (wantGPS()) {
            total += 2.95 * numDays;
        }

        if (wantRoadSideAssistance()) {
            total += 3.95 * numDays;
        }

        return total;
    }
}
