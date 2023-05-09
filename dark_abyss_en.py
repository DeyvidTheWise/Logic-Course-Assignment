def dark_abyss(n):
    # Calculate the total number of moves
    num_moves = 2 ** n - 1
    pegs = ["A", "B", "C"]

    # Iterate through each move
    for move in range(1, num_moves + 1):
        # Determine the source peg using bitwise operations
        from_peg = pegs[((move & move - 1) % 3)]
        # Determine the destination peg using bitwise operations
        to_peg = pegs[(((move | move - 1) + 1) % 3)]
        # Print the move
        print(f"Move disk from peg {from_peg} to peg {to_peg}")

n = 4
dark_abyss(n)