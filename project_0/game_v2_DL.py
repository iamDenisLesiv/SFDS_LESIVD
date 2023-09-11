"""Guess number Game
PC creates and guesses the number itself
"""

import numpy as np


def random_predict(number) -> int:
    """Guessing the number with an improved algorithm

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    min_opt = 1
    max_opt = 101
    attempts_count = 1
    predict_number = np.random.randint(1, 101)  #PC guesses number

    while predict_number != number:
        attempts_count += 1 # tries calculation
        
        if max_opt - min_opt < 2:
            break
        
        elif predict_number < number:
            min_opt = predict_number
            predict_number = round((min_opt + max_opt) / 2)
            
        else:
            max_opt = predict_number
            predict_number = round((max_opt + min_opt) / 2)
            

    return attempts_count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorythm finds the number in {score} attempts in average")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
