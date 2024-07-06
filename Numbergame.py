import java.util.Random;
import java.util.Scanner;

public class NumberGuessingGame {
    private static final int MAX_ATTEMPTS = 5;
    private static final int MIN_RANGE = 1;
    private static final int MAX_RANGE = 100;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        boolean playAgain = true;
        int score = 0;

        System.out.println("Welcome to the Number Guessing Game!");

        while (playAgain) {
            int targetNumber = random.nextInt(MAX_RANGE - MIN_RANGE + 1) + MIN_RANGE;
            boolean guessedCorrectly = false;
            int attempts = 0;

            System.out.println("\nI have generated a number between " + MIN_RANGE + " and " + MAX_RANGE + ". Can you guess it?");
            
            while (attempts < MAX_ATTEMPTS && !guessedCorrectly) {
                System.out.print("Enter your guess: ");
                int guess = scanner.nextInt();
                attempts++;

                if (guess == targetNumber) {
                    System.out.println("Congratulations! You guessed the correct number.");
                    guessedCorrectly = true;
                    score += MAX_ATTEMPTS - attempts + 1;
                } else if (guess < targetNumber) {
                    System.out.println("Too low!");
                } else {
                    System.out.println("Too high!");
                }
            }

            if (!guessedCorrectly) {
                System.out.println("Sorry, you've used all your attempts. The correct number was " + targetNumber);
            }

            System.out.println("Your current score: " + score);

            System.out.print("Do you want to play another round? (yes/no): ");
            playAgain = scanner.next().equalsIgnoreCase("yes");
        }

        System.out.println("Thank you for playing! Your final score is: " + score);
        scanner.close();
    }
}
