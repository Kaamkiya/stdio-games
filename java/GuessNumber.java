import java.util.*;

/**
 * @name GuessNumber
 * @version 0.0.1
 */

public class GuessNumber {
  public static void main(String[] args) {
    int number = (int)(Math.random()*100); // make a random integer between 1 and 100
       
    int guess = 101; // so that the guess cannot be the answer
    Scanner scanner = new Scanner(System.in);
       
    System.out.println("Guess a number between 1 and 100");
        
    while (guess != number) {
      guess = scanner.nextInt();

      if (guess < number) {
        System.out.println(guess + " is too small, try again.");
      } else if (guess > number) {
        System.out.println(guess + " is too big, try again.");
      } else {
        break;
      }
    }
    System.out.println("Correct!");
  }
}
