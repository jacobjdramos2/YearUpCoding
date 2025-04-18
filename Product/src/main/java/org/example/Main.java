package org.example;

import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        String input = "111|Hot Chocolate (12-count)|21|4.99";
        String input2 = "221|Coled Chocolate (12-count)|21|5.99";

        Product p1 = splitString(input);
        Product p2 = splitString(input2);

        double total = 0;
        total += p1.addToTotal(p1,total) + p2.addToTotal(p2,total);

        System.out.println(total);
    }

    public static Product splitString(String input) {
        String[] tokens = input.split(Pattern.quote("|"));
        int id = Integer.parseInt(tokens[0]);
        String name = tokens[1];
        int quantity = Integer.parseInt(tokens[2]);
        double price = Double.parseDouble(tokens[3]);

        return new Product(name, price, quantity, id);
    }
}