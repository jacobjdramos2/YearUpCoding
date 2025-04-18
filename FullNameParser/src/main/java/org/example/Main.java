package org.example;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Please enter your name (first,last or first, middle, last): ");
        String input = sc.nextLine();
        input = input.trim();
        String[] inputSplit = input.split(" ");

        System.out.println("First name: " + inputSplit[0]);
        System.out.println("Middle name: " + inputSplit[1]);
        System.out.println("Last name: " + inputSplit[2]);
    }


}