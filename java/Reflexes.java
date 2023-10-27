import java.util.*;

public class Reflexes {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    
    System.out.println("Welcome to the reflexes game!");
    
    // Describe the game
    System.out.println("In this game, you have to press Enter as fast as possible,");
    System.out.println("after you see the word DRAW.");
    
    System.out.println("Ready...");
    
    long waitTime = (long) (Math.random() * 1000); // pick a random time to wait
    try {
      Thread.sleep(waitTime); // wait 1000 milliseconds (1 second)
    } catch (InterruptedException e) {
      System.out.println(e);
    }
    
    long drawTime = System.currentTimeMillis();
    System.out.println("DRAW");
    scanner.nextLine();
    
    long now = System.currentTimeMillis();
    
    double timeElapsed = (now - drawTime);
    
    if (timeElapsed < 100) {
      System.out.println("You pressed enter too early! You lose!");
    } else if (timeElapsed > 600) {
      System.out.println("Too slow! It took you " +
      timeElapsed +
      " milliseconds.");
    } else {
      System.out.println("You were fast! It took you "+
      timeElapsed +
      " milliseconds.");
    }
  }
}