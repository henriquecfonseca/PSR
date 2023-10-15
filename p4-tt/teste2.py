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

# Defina uma lista de palavras reais para o teste
palavras_reais = ["gato", "cachorro", "elefante", "tigre", "leão", "girafa", "macaco"]

input_tuple = namedtuple('input_tuple', ['palavra_shown', 'palavra_typed', 'tempo', 'letras_corretas'])

def modoCount(threshold):
    print('O teste começará em breve e terminará após digitar ' + Fore.LIGHTCYAN_EX + Style.BRIGHT + str(threshold) + ' palavras.')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'Pressione qualquer tecla para iniciar o teste!\n')
    _ = readchar.readchar()

    for i in range(1, 4):
        print(Fore.CYAN + Style.BRIGHT + 'O teste começará em ' + str(4 - i) + ' segundos.\n')
        time.sleep(1)

    inputs = []
    time_b4_exec = time.time()
    test_interrupt = False

    for i in range(threshold):
        palavra_correta = palavras_reais[i]
        num_caracteres_corretos = len(palavra_correta)
        time_b4 = time.time()
        print("Digite a palavra " + Style.BRIGHT + Fore.LIGHTBLUE_EX + palavra_correta)
        
        # Initialize an empty string to store user input
        palavra_digitada = ""
        while len(palavra_digitada) < num_caracteres_corretos:
            char = readchar.readchar()
            palavra_digitada += char
            print(char, end='', flush=True)  # Print the character without a newline

        if palavra_digitada == chr(27):   # Clicking the ESC button
            time_after = time.time()  # Stops time function
            test_interrupt = True  # And interrupts function
            break

        time_after = time.time()

        letras_corretas = sum(1 for pc, pt in zip(palavra_correta, palavra_digitada) if pc == pt)
        if letras_corretas == len(palavra_correta):
            print(Back.GREEN + "     Você digitou " + palavra_digitada, '\n')
        else:
            print(Back.RED + "     Você digitou " + palavra_digitada, '\n')

        duration = time_after - time_b4
        input_data = input_tuple(palavra_shown=palavra_correta, palavra_typed=palavra_digitada, tempo=duration, letras_corretas=letras_corretas)
        inputs.append(input_data)

    if not test_interrupt:
        print(Fore.MAGENTA + Style.BRIGHT + '\nTeste concluído!\n')
    else:
        print(Fore.YELLOW + Style.BRIGHT + '\nTeste interrompido!\n')

    return inputs, time_b4_exec


def modoTimed(threshold):
    print('O teste começará em breve e terminará após  ' + Fore.LIGHTCYAN_EX + Style.BRIGHT + str(threshold) + ' segundos.')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'Pressione qualquer tecla para iniciar o teste!\n')
    _ = readchar.readchar()

    for i in range(1, 4):
        print(Fore.CYAN + Style.BRIGHT + 'O teste começará em ' + str(4 - i) + ' segundos.\n')
        time.sleep(1)

    inputs = []
    time_b4_exec = time.time()
    test_interrupt = False
    timing = 0  # Initialize timing
    i=0

    while timing < float(threshold):
        palavra_correta = palavras_reais[i]
        num_caracteres_corretos = len(palavra_correta)
        time_b4 = time.time()
        print("Digite a palavra " + Style.BRIGHT + Fore.LIGHTBLUE_EX + palavra_correta)

        # Initialize an empty string to store user input
        palavra_digitada = ""
        while len(palavra_digitada) < num_caracteres_corretos:
            char = readchar.readchar()
            palavra_digitada += char
            print(char, end='', flush=True)  # Print the character without a newline

        if palavra_digitada == chr(27):  # Clicking the ESC button
            time_after = time.time()  # Stops time function
            test_interrupt = True  # And interrupts function
            break

        letras_corretas = sum(1 for pc, pt in zip(palavra_correta, palavra_digitada) if pc == pt)

        if letras_corretas == len(palavra_correta):
            print(Back.GREEN + "     Você digitou " + palavra_digitada, '\n')
        else:
            print(Back.RED + "     Você digitou " + palavra_digitada, '\n')
        
        i=i+1
        
        time_after = time.time()
        reaction_time = time_after - time_b4
        timing = time_after - time_b4_exec
        input_data = input_tuple(palavra_shown=palavra_correta, palavra_typed=palavra_digitada, tempo=reaction_time, letras_corretas=letras_corretas)
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
    dict_keys = ['n_acertos', 'n_digitadas', 'precisao', 'duracao_teste', 'inicio_teste', 'fim_teste', 'tempo_medio_digitar']
    stat_dict = dict.fromkeys(dict_keys, 0)
    total_tempo_acerto = 0
    n_erros = 0

    for i in range(len(inputs)):
        if inputs[i].palavra_typed == inputs[i].palavra_shown:
            stat_dict['n_acertos'] += 1
            total_tempo_acerto += inputs[i].tempo
        else:
            n_erros += 1

        stat_dict['duracao_teste'] += inputs[i].tempo

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

    stat_dict['tempo_medio_digitar'] = avg_type_time

    stat_dict['palavras'] = inputs
    return stat_dict

def main():
    parser = argparse.ArgumentParser(description='Script para testar velocidade e precisão ao digitar palavras reais')
    parser.add_argument('-utm', '--use_time_mode', action='store_true', default=False,
                        help='Usar modo de tempo: testa até um determinado número de segundos.\n Caso contrário, testa até um número de palavras.')
    parser.add_argument('-mv', '--max_value', type=int, required=True, help='Número de segundos/palavras do teste')
    args = parser.parse_args()

    inputs = []
    my_dict = {}

    if args.use_time_mode == True:
        inputs, time_b4_exec = modoTimed(args.max_value)
    else:
        inputs, time_b4_exec = modoCount(args.max_value)

    my_dict = buildDict(inputs, time_b4_exec)
    print(Fore.GREEN + 'Estatísticas do seu teste são:', '\n')
    pprint.pprint(my_dict, sort_dicts=False)

if __name__ == '__main__':
    main()
