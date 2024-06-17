import random

class Task1:
    def main(self):
        min_num = 1
        max_num = 100
        rounds = 0
        wins = 0
        max_attempts = 8

        while True:
            attempts = 0
            rounds += 1
            print("Round:", rounds)
            random_num = random.randint(min_num, max_num)
            print(f"Guess a random number between {min_num} & {max_num}:")

            while attempts < max_attempts:
                guess = int(input())
                attempts += 1
                if guess == random_num:
                    print("You guessed it! The number is", guess, ", you win!!")
                    wins += 1
                    print("Attempts taken:", attempts)
                    break
                elif guess < random_num:
                    print("Too low, try again:")
                else:
                    print("Too high, try again:")

            if attempts >= max_attempts:
                print("Oops! You have no more lives!. The number was", random_num, ".")
                
            print("Wanna play again? (Type 'yes' to continue):")
            answer = input().lower()
            print(" ")

            if answer != "yes":
                break

        print("Rounds played:", rounds)
        print("Rounds won:", wins)

if __name__ == "__main__":
    Task1().main()
