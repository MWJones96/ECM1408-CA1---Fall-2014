def diagonal(text, right_to_left=False):
    num_spaces = len(text) -1 if right_to_left else 0
    for letter in text:
        print(' ' * num_spaces + letter)
        num_spaces += -1 if right_to_left else 1

diagonal('slantwise')
diagonal('slantwise', right_to_left=True)