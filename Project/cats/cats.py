"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    selected_p = [i for i in paragraphs if select(i)== True]
    if k > len(selected_p)-1:
        return ''
    else:
        return selected_p[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select(paragraph):
        p_list = lower(remove_punctuation(paragraph)).split()
        for i in topic:
            for j in p_list:
                if i == j:
                    return True
        return False
    return select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    counter = 0
    if len(typed_words) == 0:
        return 0.0
    for i in range(min(len(typed_words), len(reference_words))):
        if typed_words[i] == reference_words[i]:
            counter += 1 
    #print("DEBUG:", counter, max(len(typed_words), len(reference_words)))
    return (counter/len(typed_words))*100.0
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return (len(typed)/5) / (elapsed/60)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    diff_dict = {}
    for word in valid_words:
        diff = diff_function(user_word, word, limit) 
        diff_dict[word] = diff
    min_diff = min(diff_dict.values())
    if min_diff > limit:
        return user_word
    else:
        for k in diff_dict.keys():
            if diff_dict[k] == min_diff:
                return k
    # END PROBLEM 5

#Alternative:
"""
    if user_word in valid_words:
        return user_word
    the_smallest_word = min(valid_words, key = lambda valid_word : diff_function(user_word, valid_word,limit))  
    if diff_function(user_word,the_smallest_word,limit) <= limit:
        return the_smallest_word
    else:
        return user_word
"""


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line'
    
    def helper(start, goal, limit, counter=0):
        if len(start) == 1 and len(goal) ==1:
            return start !=goal
        if len(start) == 0 or len(goal) == 0:
            return abs(len(start) - len(goal))
        if start == goal:
            return 0
        if start[0] != goal[0]:
            counter += 1
        if counter > limit:
            return limit + 1
        else:
            return helper(start[1:], goal[1:], limit, counter) + (start[0] != goal[0])
    return helper(start, goal, limit)
    # END PROBLEM 6
    
#Alternative:
"""
    def helper(start, goal,curr_length):
        if curr_length > limit:
            return limit + 1
        m, n = len(start), len(goal)
        if m == 0 and n == 0:
            return curr_length
        if m == n:
            if start[0] != goal[0]:
                return helper(start[1:],goal[1:],curr_length+1)
            return helper(start[1:],goal[1:],curr_length)
        elif m > n:
            return helper(start[:n],goal,curr_length+m-n)
        else:
            return helper(start,goal[:m],curr_length+n-m)

    return helper(start, goal , 0)
"""
#Alternative2:
"""
    if start == goal:
        return 0
    if limit < 0:
        return 1
    if min(len(start), len(goal)) == 0:
        return max(len(start), len(goal))
    diff = start[0] != goal[0]  # diff = 1 if start and goal have identical initial letter, else 0
    return diff + shifty_shifts(start[1:], goal[1:], limit-diff) # compare two reduced strings and decrease limit by diff
"""

def pawssible_patches(start, goal, limit): 
    """A diff function that computes the edit distance from START to GOAL."""
    #assert False, 'Remove this line'
    """
    if limit < 0: # Fill in the condition
        # BEGIN
        return 0
        # END

    elif len(start) == 0 or len(goal) == 0: # Feel free to remove or add additional cases
        # BEGIN
        return len(start) or len(goal)    # The expression "OR" first evaluates x, if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned
        # END 
    else:
        if start[0] == goal[0]:
            return pawssible_patches(start[1:], goal[1:], limit)
        else:
            add_diff = pawssible_patches(start, goal[1:], limit-1) # Fill in these lines
            remove_diff = pawssible_patches(start[1:], goal, limit-1)
            substitute_diff = pawssible_patches(start[1:], goal[1:], limit-1)
        # BEGIN
            return min(add_diff, remove_diff, substitute_diff) + 1
        # END
    """
# Alternative, more understandable:
    if limit < 0:
        return 1
    elif start == goal: 
        return 0
    elif min(len(start), len(goal)) == 0:
        return max(len(start), len(goal))
    else:
        diff = start[0] != goal[0]
        add_diff = 1 + pawssible_patches(start, goal[1:], limit-1)
        remove_diff = 1 + pawssible_patches(start[1:], goal, limit-1)
        substitute_diff = diff + pawssible_patches(start[1:], goal[1:], limit-diff)
    return min(add_diff, remove_diff, substitute_diff)


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    counter = 0
    d={}
    for i in range(len(typed)):
        if typed[i] == prompt[i]:
            counter += 1
        else:
            break
    progress = counter / len(prompt)
    d['id'] = user_id
    d['progress']= progress
    send(d)
    return progress
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    time_diff_list = []
    for player_index in range(len(times_per_player)):
        time_diff_list.append([times_per_player[player_index][i+1] - times_per_player[player_index][i] for i in range(len(times_per_player[player_index])-1)])
    return game(words, time_diff_list)
    # END PROBLEM 9

# Alternative, more compact:
    """
    for player in times_per_player:
        time_diff_list.append([player[i]-player[i-1] for i in range(1,len(player))])
    """

def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    
    compare_list = [[all_times(game)[p][w] for p in player_indices] for w in word_indices]
    winner_list = [w.index(min(w)) for w in compare_list]
    print("DEBUG:", compare_list, winner_list)
    result_index = [[i for i in range(len(winner_list)) if winner_list[i] == p] for p in player_indices]
    return [[all_words(game)[i] for i in r] for r in result_index]
    # END PROBLEM 10
    
#Alternative:
"""
    result = [[] for _ in player_indices]
    for w in word_indices:
        min_time = float('inf')
        winner_index = 0
        for p in player_indices:
            if time(game, p, w) < min_time:
                min_time = time(game, p, w)
                winner_index = p
        result[winner_index].append(word_at(game, w))
    return result
"""

def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = True  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)