#game_homework
import numpy as np

""" Игра Угадай число.
    Компьютер сам загадывает и угадывает загаданное число менее чем за 20 попыток"""
    
def game_core_v3(predict_number: int = np.random.randint(1, 101)) -> int:
    """
    Args:
        predict_number (int, optional): Случайно загаданное число компьютером

    Returns:
        int: Число попыток
    """
    min_number = 1 
    max_number = 100 
    count = 0  # число попыток
    number = max_number/2 # фиксированное число, с которым будем сравнивать загаданное число
    
    while predict_number != number:
        count += 1
        if predict_number > number:
            min_number = number + 1         
        elif predict_number < number:   
            max_number = number - 1
        number = int((max_number + min_number) / 2)  # выводим новое число для сравнения путем сужения диапазона поиска
    else:
        return count  
print(game_core_v3())   
            
def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v3([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


score_game(game_core_v3)           
            
        
    

   



