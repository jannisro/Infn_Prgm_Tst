import random

for i in range(100):
    rand = random.randint(1, 100)

    # Append correct lucky number notice
    note = ""
    if rand % 7 == 0:
        note = "(Lucky Number!)"

    # Print index, random number & lucky numer notice
    print("{:d}: {:d} {}".format(i+1, rand, note))

    # Print separator every 5 steps
    if (i+1) % 5 == 0:
        print("------")
