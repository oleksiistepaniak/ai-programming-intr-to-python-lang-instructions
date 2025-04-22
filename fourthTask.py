sentence = """A programmer is a programming specialist who develops software (in
simpler cases, individual programs) for programmable devices, which
usually contain one or more processors"""

words = sentence.split()

N = int(input(f"Enter N (1 ≤ N < 20): "))

i, j = N - 1, 20 - N - 1

if 0 <= i < len(words) and 0 <= j < len(words):
    words[i], words[j] = words[j], words[i]
    new_sentence = " ".join(words)
    print("Unmodified sentence:")
    print(" ".join(sentence.split()))
    print("Modified sentence:")
    print(new_sentence)
else:
    print("Invalid N. Not enough words in the sentence.")
