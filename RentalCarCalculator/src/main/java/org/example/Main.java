package org.example;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy");

    System.out.println("Pickup Date (MM/dd/yyyy): ");
    String pickupD = sc.nextLine();

    System.out.println("Number of days for rental: ");
    int numDays = sc.nextInt();

    LocalDate pickupDate = LocalDate.parse(pickupD, formatter);
    LocalDate returnDate = pickupDate.plusDays(numDays);
    DayOfWeek returnDay = returnDate.getDayOfWeek();
    System.out.println("Return will be on: " + returnDay);

    RentalCarCalculator rcc = new RentalCarCalculator(pickupD, numDays);
    rcc.electronicTag();
    rcc.wantGPS();
    rcc.wantRoadSideAssistance();

    System.out.println("What is your current age?");
    int age = sc.nextInt();

    double total = rcc.calculatePrice(age);

    System.out.println("Your total is: " + total);
}