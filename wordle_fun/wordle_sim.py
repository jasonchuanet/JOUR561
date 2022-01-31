import json
import copy
import csv
import statistics
def score(test_word, solution_list, answer_list):
    # How many words are still solution guesses, after guessing this word?

    ##Some constants
    GREEN = 10
    YELLOW = 5
    GRAY = 0

    test_word_characters = list(test_word)
    amount_remaining_words = []

    # Loop over every possible answer
    for answer in answer_list:
        #possible_solutions = copy.copy(solution_list)
        possible_solutions = solution_list
        answer_characters = list(answer)
        evaluation = [GRAY,GRAY,GRAY,GRAY,GRAY] # Green, Yellow, or Gray
        # Color the letters Green
        for index in range(0,5):
            if test_word_characters[index] == answer_characters[index]:
                evaluation[index] = GREEN
                answer_characters[index] = " "
        # Color the letters yellow
        for index in range(0,5):
            if test_word_characters[index] in answer_characters: 
                # If this character is repeated in the answer, 
                evaluation[index] = YELLOW
                answer_characters[answer_characters.index(test_word_characters[index])] = " "

        pruned_words = 0
        # Prune based on evaluation colors
        for solution in possible_solutions:
            try:
                for index in range(0,5):
                    #- If a letter is green, every word that does not have the same letter is that position, is pruned
                    if (evaluation[index] == GREEN):
                        if test_word[index] != solution[index]:
                            raise Exception("Pruned")
                    #- If a letter is yellow,
                    if (evaluation[index] == YELLOW):
                        # every word that has that letter in the same position in pruned
                        if test_word[index] == solution[index]:
                            raise Exception("Pruned")
                        # every word that does not contain that letter is pruned
                        if test_word[index] not in solution:
                            raise Exception("Pruned")
                    #- If a letter is grey, every word that has the letter, in any position, is pruned
                    if (evaluation[index] == GRAY):
                        if test_word[index] in solution:
                            raise Exception("Pruned")
            except:
                pruned_words += 1
        amount_remaining_words.append(pruned_words)
    #return sum(amount_remaining_words)/len(amount_remaining_words)
    #return median(amount_remaining_words)
    return test_word, amount_remaining_words

def multi_score(word):
    return score(word, wordle_valid, wordle_answers)