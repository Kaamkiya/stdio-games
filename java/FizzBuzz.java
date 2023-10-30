/**
 * @name FizzBuzz
 * @version 0.0.1
 ** Te classic FizzBuzz challenge
 */

import java.util.Scanner;

public class FizzBuzz {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    
    System.out.println("FizzBuzz");
    System.out.println("How high would you like to go?");
    
    int amount = 0;
    
    try {
      amount = scanner.nextInt();
    } catch (Exception e) {
      System.out.println("Not a valid number. ");
      System.exit(0);
    }

    for (int i = 1; i <= amount; i++) {
      if (i % 15 == 0) {
        System.out.println("FizzBuzz");
      } else if (i % 5 == 0) {
        System.out.println("Buzz");
      } else if (i % 3 == 0) {
        System.out.println("Fizz");
      } else {
        System.out.println(i);
      }
    }
  }
}