#!/usr/bin/env python3

from collections import namedtuple
import pprint
import argparse
import random
import readchar
import time

import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

# Define a list of real words for the test
real_word = ["The" , "quick" , "brown", "fox" , "jumps" , "over" , "the" , "lazy" , "dog",] 

input_tuple = namedtuple('input_tuple', ['palavra_shown', 'palavra_typed', 'time', 'letras_corretas']) 

#Mode where the test ends after 'threshold' inputs
def ContWordMode(threshold):   
    print('The test will end after ' + str(threshold)+ ' inputs.')
    print('Pressing any key will begin the test.\n')
    _ = readchar.readchar()

    # Starts a countdown after pressing a key
    for i in range(1, 4):
        print(Fore.CYAN + Style.BRIGHT + 'The test will begin in ' + str(4 - i) + ' seconds.\n')
        time.sleep(1)

    inputs = []
    time_b4_exec = time.time()
    test_interrupt = False

    for i in range(threshold): # Defines a range
        right_word = real_word[i]
        num_characters = len(right_word)
        time_b4 = time.time()
        print("Type " + Style.BRIGHT + Fore.LIGHTBLUE_EX + right_word)
        
        # Initialize an empty string to store user input
        typed_word = ""
        while len(typed_word) < num_characters:
            char = readchar.readchar()
            typed_word += char
            print(char, end='', flush=True)  # Print the character without a newline

        if typed_word == chr(27):   # Clicking the ESC button
            time_after = time.time()  # Stops time function
            test_interrupt = True  # And interrupts function
            break

        time_after = time.time()

        right_letters = sum(1 for pc, pt in zip(right_word, typed_word) if pc == pt)
        if right_letters == len(right_word):
            print ('Correct! You typed '+ typed_word, '\n')
        else:
            print('Incorrect! It was '+ right_word, ' but you typed '+typed_word, '\n')

        duration = time_after - time_b4
        input_data = input_tuple(palavra_shown=right_word, palavra_typed=typed_word, time=duration, letras_corretas=right_letters)
        inputs.append(input_data)

    if not test_interrupt:
        print('\nThe test has now been completed!\n')
    else:
        print('\nThe test has been interrupted.\n')

    return inputs, time_b4_exec

#Mode where the test ends after 'threshold' seconds
def TimeWordMode(threshold):
    print('The test will end after ' + str(threshold)+ ' seconds.')
    print('Pressing any key will begin the test.\n')
    _ = readchar.readchar()

    for i in range(1, 4):
        print(Fore.CYAN + Style.BRIGHT + 'The test will begin in ' + str(4 - i) + ' segundos.\n')
        time.sleep(1)

    inputs = []
    time_b4_exec = time.time()
    test_interrupt = False
    timing = 0  # Initialize timing
    i=0

    while timing < float(threshold):
        right_word = real_word[i]
        num_characters = len(right_word)
        time_b4 = time.time()
        print("Type " + Style.BRIGHT + Fore.LIGHTBLUE_EX + right_word)

        # Initialize an empty string to store user input
        typed_word = ""
        while len(typed_word) < num_characters:
            char = readchar.readchar()
            typed_word += char
            print(char, end='', flush=True)  # Print the character without a newline

        if typed_word == chr(27):  # Clicking the ESC button
            time_after = time.time()  # Stops time function
            test_interrupt = True  # And interrupts function
            break

        right_letters = sum(1 for pc, pt in zip(right_word, typed_word) if pc == pt)

        if right_letters == len(right_word):
            print ('Correct! You typed '+ typed_word, '\n')
        else:
            print('Incorrect! It was '+ right_word, ' but you typed '+typed_word, '\n')

        
        i=i+1
        
        time_after = time.time()
        reaction_time = time_after - time_b4
        timing = time_after - time_b4_exec
        input_data = input_tuple(palavra_shown=right_word, palavra_typed=typed_word, time=reaction_time, letras_corretas=right_letters)
        inputs.append(input_data)

    if not test_interrupt:
        time_after = time.time()
        timing = time_after - time_b4_exec
        exceeded_time = timing - float(threshold)  # Calculate the exceeded time
        print(Fore.MAGENTA + Style.BRIGHT + 'Test is finished! You exceeded the maximum test duration (' + str(threshold) + ' sec) by ' + str(round(exceeded_time, 2)) + ' seconds\n')
    else:
        print(Fore.YELLOW + Style.BRIGHT + '\nTest interrupted!\n')

    return inputs, time_b4_exec


def buildDict(inputs, abs_b4_time):
    dict_keys = ['n_acertos', 'n_digitadas', 'precisao', 'duracao_teste', 'inicio_teste', 'fim_teste', 'time_medio_digitar']
    stat_dict = dict.fromkeys(dict_keys, 0)
    total_time_acerto = 0
    n_erros = 0

    for i in range(len(inputs)):
        if inputs[i].palavra_typed == inputs[i].palavra_shown:
            stat_dict['n_acertos'] += 1
            total_time_acerto += inputs[i].time
        else:
            n_erros += 1

        stat_dict['duracao_teste'] += inputs[i].time

    stat_dict['n_digitadas'] = len(inputs)

    if stat_dict['n_digitadas'] == 0:
        stat_dict['precisao'] = 0
    else:
        stat_dict['precisao'] = stat_dict['n_acertos'] / stat_dict['n_digitadas']

    stat_dict['inicio_teste'] = time.ctime(abs_b4_time)
    stat_dict['fim_teste'] = time.ctime(abs_b4_time + stat_dict['duracao_teste'])

    if len(inputs) == 0:
        avg_type_time = 0
    else:
        avg_type_time = stat_dict['duracao_teste'] / len(inputs)

    stat_dict['time_medio_digitar'] = avg_type_time

    stat_dict['palavras'] = inputs
    return stat_dict

def main():
    parser = argparse.ArgumentParser(description='Script para testar velocidade e precisão ao digitar palavras reais')
    parser.add_argument('-utm', '--use_time_mode', action='store_true', default=False,
                        help='Usar modo de time: testa até um determinado número de segundos.\n Caso contrário, testa até um número de palavras.')
    parser.add_argument('-mv', '--max_value', type=int, required=True, help='Número de segundos/palavras do teste')
    args = parser.parse_args()

    inputs = []
    my_dict = {}

    if args.use_time_mode == True:
        inputs, time_b4_exec = TimeWordMode(args.max_value)
    else:
        inputs, time_b4_exec = ContWordMode(args.max_value)

    my_dict = buildDict(inputs, time_b4_exec)
    print(Fore.GREEN + 'Estatísticas do seu teste são:', '\n')
    pprint.pprint(my_dict, sort_dicts=False)

if __name__ == '__main__':
    main()
