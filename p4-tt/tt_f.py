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

real_word = ["The" , "quick" , "brown", "fox" , "jumps" , "over" , "the" , "lazy" , "dog,","unafraid","of","what","might","happen","as","a","result.","The","dog","although","lazy","jumped","back","and","started","growling"] 

input_tuple = namedtuple('input_tuple', ['question', 'answer', 'time', 'letras_corretas']) 

#Mode where the test ends after 'threshold' inputs with words
def CountWordMode(threshold):   
    print('The test will end after ' + Fore.LIGHTCYAN_EX + Style.BRIGHT + str(threshold)+ ' inputs.')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'Pressing any key will begin the test.\n')
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

        if typed_word == chr(32):     # Clicking the ESC button
            time_after = time.time()  # Stops time function
            test_interrupt = True     # And interrupts function
            break

        time_after = time.time()

        right_letters = sum(1 for pc, pt in zip(right_word, typed_word) if pc == pt)
        if right_letters == len(right_word):
            print (Back.GREEN + '\nCorrect! You typed '+ typed_word + '\n' +  Style.RESET_ALL)
        else:
            print(Back.RED + '\nIncorrect! It was '+ right_word + ' but you typed ' + '\n' + typed_word + Style.RESET_ALL)

        duration = time_after - time_b4
        input_data = input_tuple(question=right_word, answer=typed_word, time=duration, letras_corretas=right_letters)
        inputs.append(input_data)

    if not test_interrupt:
        print(Fore.MAGENTA + Style.BRIGHT + '\nThe test has now been completed!\n')
    else:
        print(Fore.YELLOW + Style.BRIGHT + '\nThe test has been interrupted.\n')

    return inputs, time_b4_exec

#Mode where the test ends after 'threshold' seconds with words

def TimeWordMode(threshold):
    print('The test will end after ' + Fore.LIGHTCYAN_EX + Style.BRIGHT + str(threshold)+ ' seconds.')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'Pressing any key will begin the test.\n')
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

        if typed_word == chr(32):  # Clicking the ESC button
            time_after = time.time()  # Stops time function
            test_interrupt = True  # And interrupts function
            break

        right_letters = sum(1 for pc, pt in zip(right_word, typed_word) if pc == pt)

        if right_letters == len(right_word):
            print (Back.GREEN + '\nCorrect! You typed ' + typed_word  + '\n' + Style.RESET_ALL)
        else:
            print(Back.RED + '\nIncorrect! It was ' + right_word + ' but you typed ' + '\n' + typed_word + Style.RESET_ALL)

        
        i=i+1
        
        time_after = time.time()
        reaction_time = time_after - time_b4
        timing = time_after - time_b4_exec
        input_data = input_tuple(question=right_word, answer=typed_word, time=reaction_time, letras_corretas=right_letters)
        inputs.append(input_data)

    if not test_interrupt:
        time_after = time.time()
        timing = time_after - time_b4_exec
        exceeded_time = timing - float(threshold)  # Calculate the exceeded time
        print(Fore.MAGENTA + Style.BRIGHT + 'Test is finished! You exceeded the maximum test duration (' + str(threshold) + ' sec) by ' + str(round(exceeded_time, 2)) + ' seconds\n')
    else:
        print(Fore.YELLOW + Style.BRIGHT + '\nTest interrupted!\n')

    return inputs, time_b4_exec

def CountLetterMode(threshold):  # Mode where the test ends after 'threshold' inputs 
    print('The test will end after ' + Fore.LIGHTCYAN_EX + Style.BRIGHT + str(threshold)+ ' inputs.')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'Pressing any key will begin the test.\n')
    _ = readchar.readchar()

    # Starts a countdown after pressing a key
    for i in range(1,4): 
        print (Fore.CYAN + Style.BRIGHT + 'The test will begin in '+ str(4-i)+ ' seconds.\n')
        time.sleep(1)

    inputs=[]
    time_b4_exec=time.time()
    test_interrupt = False
    
    for i in range(1,threshold+1): # Defines a range
        target_input=chr(random.randint(97,122))
        time_b4=time.time()
        print("Type " + Style.BRIGHT + Fore.LIGHTBLUE_EX + target_input)
        typed_input= readchar.readchar()

        if typed_input == chr(32):   # Clicking the ESC button
            time_after = time.time() # Stops time function
            test_interrupt= True     # And interrupts function
            break

        time_after = time.time()
        if typed_input == target_input:
            print (Back.GREEN  + '  Correct! You typed '+ typed_input, '\n')
        else:
            print(Back.RED + '  Incorrect! It was '+ target_input, ' but you typed '+typed_input, '\n')

        duration=time_after-time_b4

        right_letters = sum(1 for pc, pt in zip(target_input, typed_input) if pc == pt)

        input=input_tuple(question=target_input, answer=typed_input, time=duration,letras_corretas=right_letters)

        inputs.append(input)

    if not test_interrupt:
        print(Fore.MAGENTA + Style.BRIGHT + '\nThe test has now been completed!\n')
    else:
        print(Fore.YELLOW + Style.BRIGHT + '\nThe test has been interrupted.\n')

    return inputs, time_b4  



def TimeLetterMode(threshold):                 # Mode where the test ends after 'threshold' seconds 

    print('The test will begin shortly, ending after ' + Fore.LIGHTCYAN_EX + Style.BRIGHT + str(threshold) + ' seconds.')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'Press any key to begin the test!\n')
    _ = readchar.readchar()
    timed_inputs = []

    # After pressing a key, there's a 3 second countdown before the test starts for the user to prepare.
    for i in range(1,4):
        print(Style.BRIGHT + Fore.CYAN + 'The test will start in '+ str(4-i) +' seconds.\n')
        time.sleep(1)

    time_b4_exec = time.time()                               #Stores the time when the test was started
    timing = 0
    test_interrupt = False                                          #Define value 0 to the variable that is going to be used during the while cycle

    #The function will run until the duration limit is reached
    while timing < float(threshold):

        target_input = chr(random.randint(97,122))         #Generates a random letter
        print('Type letter ' + Fore.LIGHTBLUE_EX + Style.BRIGHT + target_input)  #Prints the generated letter
        time_b4_chr = time.time()                      #Gets the time before the input

        typed_input = readchar.readkey()              #Reads the input letter
        
        #! Its important that this if statement is before appending the result to the output
        if  typed_input == chr(32):                    #Clicking on the space bar 
            time_after = time.time()                    #End date of the text
            test_interrupt = True
            break

        if typed_input == target_input:
            print(Back.GREEN + "     You typed " + typed_input,'\n')
        else:
            print(Back.RED + "     You typed " + typed_input , '\n')

        right_letters = sum(1 for pc, pt in zip(target_input, typed_input) if pc == pt)


        time_after = time.time()                            #Gets the time after the input 
        reaction_time = time_after - time_b4_chr            #Reaction time
        timing = time_after - time_b4_exec                  #Elapsed time
        input=input_tuple(question=target_input, answer= typed_input,time = reaction_time, letras_corretas=right_letters ) #Stores the information from the test
        timed_inputs.append(input)
        dif = timing - threshold


    if not test_interrupt:
        print(Fore.MAGENTA + Style.BRIGHT + 'Test is finished! You exceeded the maximum test duration (' + str(threshold) + ' sec) by ' + str(round(dif,2)) + ' seconds\n')
    else:
        print(Fore.YELLOW + Style.BRIGHT + '\nTest interrupted!\n')

    return(timed_inputs, time_b4_exec)




def buildDict(inputs, abs_b4_time):
    dict_keys = ['accuracy', 'types', 'n_hits', 'n_types', 'test_duration', 'test_end', 'test_start', 'type_avg_dur', 'hit_avg_dur', 'miss_avg_dur']
    stat_dict = dict.fromkeys(dict_keys, 0)
    total_hit_time = 0
    total_miss_time = 0
    n_misses = 0

    for i in range(len(inputs)):
        if inputs[i].question == inputs[i].answer:
            stat_dict['n_hits'] += 1
            total_hit_time += inputs[i].time
        else:
            total_miss_time += inputs[i].time
            n_misses += 1

        stat_dict['test_duration'] += inputs[i].time

    stat_dict['n_types'] = len(inputs)

    stat_dict['accuracy'] = stat_dict['n_hits'] / stat_dict['n_types'] if stat_dict['n_types'] != 0 else 0

    stat_dict['test_start'] = time.ctime(abs_b4_time)

    stat_dict['test_end'] = time.ctime(abs_b4_time + stat_dict['test_duration'])

    if not inputs:
        avg_type_time = 0
    else:
        avg_type_time = stat_dict['test_duration'] / len(inputs)
    
    stat_dict['type_avg_dur'] = '{:.3f}s'.format(avg_type_time)

    miss_avg_time = total_miss_time / n_misses if n_misses != 0 else 0
    stat_dict['miss_avg_dur'] = '{:.3f}s'.format(miss_avg_time)

    hit_avg_time = total_hit_time / stat_dict['n_hits'] if stat_dict['n_hits'] != 0 else 0
    stat_dict['hit_avg_dur'] = '{:.3f}s'.format(hit_avg_time)

    stat_dict['types'] = inputs

    return stat_dict


def main():
    parser = argparse.ArgumentParser(description='Script to test typing speed and precision')
    parser.add_argument('-utm', '--use_time_mode', action='store_true', default=False,help='Use timed mode : tests up to max_value seconds.\n Otherwise tests up to max_value letters')
    parser.add_argument('-mv', '--max_value', type=int, required=True, help='Max value, either number of inputs or seconds, depending on the selected mode')
    parser.add_argument('-uw', '--use_words', action='store_true', default=False, help='Use word typing mode instead of single character typing (turned off by default)')
    args = parser.parse_args()

    inputs = []
    my_dict = {}

    if args.use_words == True:
        if args.use_time_mode == True:
            inputs, time_b4_exec = TimeWordMode(args.max_value)
        else:
            inputs, time_b4_exec = CountWordMode(args.max_value)
    else:
        if args.use_time_mode == True:
            inputs, time_b4_exec = TimeLetterMode(args.max_value)
        else:
            inputs, time_b4_exec = CountLetterMode(args.max_value)

    my_dict = buildDict(inputs, time_b4_exec)
    print(Fore.GREEN + 'Estatísticas do seu teste são:', '\n')
    pprint.pprint(my_dict, sort_dicts=False)

if __name__ == '__main__':
    main()