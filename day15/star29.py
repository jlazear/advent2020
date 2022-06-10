input_tests = ['1,3,2',
               '2,1,3',
               '1,2,3',
               '2,3,1',
               '3,2,1',
               '3,1,2']
input_test_end = 2020
input_test_answers = [1, 10, 27, 78, 438, 1836]

inputs = '2,20,0,4,1,17'

def play(inputs, end_turn, verbose=3000000):
    inputs = [int(x) for x in inputs.split(',')]
    history = {}

    turn_num = 0
    for x in inputs[:-1]:
        history[x] = turn_num
        turn_num += 1

    turn_num += 1
    prev_num = inputs[-1]

    while turn_num < end_turn:
        if prev_num in history:
            prev_turn = history[prev_num]
            delta = turn_num - prev_turn - 1
            history[prev_num] = turn_num - 1
            prev_num = delta
        else:
            history[prev_num] = turn_num - 1
            prev_num = 0
        turn_num += 1
        if verbose and turn_num % verbose == 0:
            print("({}/{}) {}".format(turn_num//verbose, end_turn//verbose, turn_num))
    return prev_num

for i in range(len(input_tests)):
    input_test = input_tests[i]
    ans = input_test_answers[i]
    print("it = {}, ans = {}".format(input_test, ans))
    assert ans == play(input_test, input_test_end)
    print("passed\n-----")

print(play(inputs, 2020))
