###############################################################################
# Add your answers to the dictionary below. Possible answers are:             #
#     'bubble'                                                                #
#     'selection'                                                             #
#     'insertion'                                                             #
#     'merge'                                                                 #
#     'quick'                                                                 #
#                                                                             #
# Run this file locally to verify you spelled everything correctly.           #
###############################################################################
import random
import time

answers = {'alg_a': 'selection',
           'alg_b': 'quick',
           'alg_c': 'bubble',
           'alg_d': 'merge',
           'alg_e': 'insertion'
          }


# Results from run 1 with 2000 samples:
# ================
# n = 2000
# ----------------
# alg    t (ms)
# ----------------
# alg_a  125
# alg_b  3.61
# alg_c  287
# alg_d  5.48
# alg_e  200
# ----------------

# Results from run 2 with 1000 samples:
# ================
# n = 1000
# ----------------
# alg    t (ms)
# ----------------
# alg_a  28.9
# alg_b  1.56
# alg_c  65.7
# alg_d  2.35
# alg_e  47.2
# ----------------

# Results from run 3 with 500 samples:
# ================
# n = 500
# ----------------
# alg    t (ms)
# ----------------
# alg_a  6.92
# alg_b  0.673
# alg_c  15.2
# alg_d  1.07
# alg_e  10.9
# ---------------

# Results from run 4 with 250 samples:
# ================
# n = 250
# ----------------
# alg    t (ms)
# ----------------
# alg_a  1.71
# alg_b  0.289
# alg_c  3.55
# alg_d  0.485
# alg_e  2.45
# ----------------

# Results from run 5 with 100 samples:
# ================
# n = 100
# ----------------
# alg    t (ms)
# ----------------
# alg_a  0.293
# alg_b  0.0968
# alg_c  0.565
# alg_d  0.195
# alg_e  0.386
# ----------------

# Results from run 6 with 2000 samples in a reverse sorted list:
# ================
# n = 2000
# ----------------
# alg    t (ms)
# ----------------
# alg_a  130
# alg_b  169
# alg_c  392
# alg_d  3.7
# alg_e  396
# ----------------

# Results from run 7 with 2000 samples in a normal sorted list:
# ================
# n = 2000
# ----------------
# alg    t (ms)
# ----------------
# alg_a  127
# alg_b  137
# alg_c  0.157
# alg_d  3.39
# alg_e  0.643
# ----------------

# Results from run 8 with 1000 samples in a normal sorted list:
# ================
# n = 1000
# ----------------
# alg    t (ms)
# ----------------
# alg_a  39.3
# alg_b  39.8
# alg_c  0.152
# alg_d  1.89
# alg_e  0.333
# ----------------

# Time complexity of each algorithm:
# best case, average case, worst case
# bubble: O(n), O(n^2), O(n^2)
# selection: O(n^2), O(n^2), O(n^2)
# insertion: O(n), O(n^2), O(n^2)
# merge: O(n log n), O(n log n), O(n log n)
# quick: O(n log n), O(n log n), O(n^2)

# Each algorithm is used exactly once.
#
# The bubble and insertion sorts are adaptive - they can sort in O(n) in the best case.
#
# The quicksort algorithm always uses the last element in a sublist as the pivot.

# Guesses using the data above and the time complexity of each algorithm:
# alg_a: selection
# alg_b: quick
# alg_c: bubble
# alg_d: merge
# alg_e: insertion




# Do not edit anything below this line. This checks that you spelled all answers
# correctly when you run this file.
valid_ans = {'bubble', 'selection', 'insertion', 'merge', 'quick'}

for k, v in answers.items():
    if v not in valid_ans:
        raise ValueError(f"Value '{v}' for key '{k}' is not in {valid_ans}")

print("Valid answer! Find out if it's right after the due date.")