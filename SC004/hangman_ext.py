import random

# This constant controls the number of guess the player has.
N_TURNS = 7

HANGMAN_PICS = [
    """
       +---+
           |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       O   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       O   |
       |   |
           |
           |
           |
    =========
    """,
    """
       +---+
       O   |
      /|   |
           |
           |
           |
    =========
    """,
    """
       +---+
       O   |
      /|\  |
           |
           |
           |
    =========
    """,
    """
       +---+
       O   |
      /|\  |
      /    |
           |
           |
    =========
    """,
    """
       +---+
       O   |
      /|\  |
      / \  |
           |
           |
    =========
    """,
    """
       +---+
       xox | 
      /|\  |
      / \  |
           |
           |You-dead
    =========
    """
]


def hangman(N_TURNS):
    answer = random_word()
    hidden_answer = "-" * len(answer)

    print(f"The word looks like: {hidden_answer}")
    print(f"You have {N_TURNS} guesses left.")

    print(HANGMAN_PICS[0])

    while N_TURNS > 0:
        input_ch = input("Your guess: ").upper()

        # 檢查輸入格式是否合法
        if len(input_ch) != 1 or not input_ch.isalpha():
            print("Illegal format.")
            continue
        
        if input_ch in answer:
            print("You are correct!")
            new_hidden_answer = ""
            for i in range(len(answer)):
                if input_ch == answer[i]:
                    new_hidden_answer += input_ch
                else:
                    new_hidden_answer += hidden_answer[i]
            hidden_answer = new_hidden_answer
            print(f"The word looks like: {hidden_answer}")
        else:
            N_TURNS -= 1
            print(f"There is no '{input_ch}' in the word.")
            print(f"The word looks like: {hidden_answer}")
            print(f"You have {N_TURNS} guesses left.")

            N_TURNS += 1
            print(HANGMAN_PICS[N_TURNS])

        
        # 檢查是否已經猜出完整的答案
        if hidden_answer == answer:
            print("You are correct!")
            print("You win!")
            break

    if N_TURNS == 0:
        print("You are completely hung :(")
    print(f"The answer is: {answer}")


def main():
    hangman(N_TURNS)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#  DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()
