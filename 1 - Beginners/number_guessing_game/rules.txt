Number guessing game in Python and C
Last Updated : 11 Jun, 2026
The number guessing game is a programming project used to demonstrate concepts such as random number generation, loops, conditional statements, and user interaction. The program randomly selects a number from a user-defined range and guides the player toward the correct answer by indicating whether each guess is higher or lower than the target number.

How the Game Works
To understand how the number guessing game functions, let’s walk through two practical scenarios. These examples demonstrate how narrowing down the range intelligently, similar to a binary search can help guess the number efficiently.

Example 1: Guessing in a Range from 1 to 100
Suppose the user defines the range from 1 to 100, and the system randomly selects 42 as the target number. The guessing process might look like this:

Guess 1: 50 → Too high
Guess 2: 25 → Too low
Guess 3: 37 → Too low
Guess 4: 43 → Too high
Guess 5: 40 → Too low
Guess 6: 41 → Too low
Guess 7: 42 → Correct!
Total Guesses: 7

Example 2: Guessing in a Range from 1 to 50
Now consider a smaller range, from 1 to 50, with the same target number 42. Here's how the guesses might proceed:

Guess 1: 25 → Too low
Guess 2: 37 → Too low
Guess 3: 43 → Too high
Guess 4: 40 → Too low
Guess 5: 41 → Too low
Guess 6: 42 → Correct!
Total Guesses: 6

Note: In both examples, the maximum number of chances is calculated using the binary search principle. However, the user is free to choose any guessing strategy during gameplay.

Algorithm
Read the lower and upper bounds from the user.
Generate a random number between the specified bounds.
Repeatedly accept guesses from the user until the maximum number of attempts is reached.
Indicate whether each guess is too high or too low.
Stop the game when the correct number is guessed and display the result.
If the user fails to guess the number, display the correct answer and a game-over message.