import numpy as np
import math

def game_core_v1(number):
    '''Просто угадываем на random ни как не используя информацию о больше или меньше.
       Функция Принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1, 101) # предполагаемое число
        print ('Predict is {}'.format(predict))
        if number == predict: 
            break
    return(count) # выход из цикла, если угадали
        


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его
       в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1,100)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали

def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его
       в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1,100)
    step = 1.5 # шаг с которым ускоренно подбираемся к цели, подобран экспериментально
    step2 = 0.9 # step = step * step2  if step * step2 > 1 else 1 - шаг с которым медленно подбираемся к цели, подобран экспериментально
    while number != predict:

        if number > predict: 
           
            while number > predict: #ускоренно подбираемся к цели
                count+=1 # каждое изменение predict - это count++ 
                predictCandidate = math.ceil(predict * step)
                
                if number > predictCandidate and step > 1:
                    predict = predictCandidate
                else:
                   #predict += 1 #медленно подбираемся к цели ЗА 8 попыток

                   #медленно подбираемся к цели ЗА 6 попыток
                   predict = math.ceil(predict + step)  
                   step = step * step2  if step * step2 > 1 else 1

                   
        else:
            
            while number < predict: #ускоренно подбираемся к цели
                count+=1 # каждое изменение predict - это count++              
                predictCandidate = predict // step

                if number < predictCandidate and step > 1:
                    predict = predictCandidate
                else:
                     #predict -= 1 #медленно подбираемся к цели ЗА 8 попыток

                     #медленно подбираемся к цели ЗА 6 попыток
                     predict = math.ceil(predict - step)
                     step = step * step2 if step * step2 > 1 else 1
                    
                     

    return(count) # выход из цикла, если угадали    

def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))

    print ('----JOB DONE----\n')
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
    return(score)

# запускаем 
score_game(game_core_v3)
