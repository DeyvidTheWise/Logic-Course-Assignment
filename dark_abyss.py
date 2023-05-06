def dark_abyss(n, source, destination, auxiliary):
    num_moves = 2 ** n - 1
    pegs = [source, auxiliary, destination]

    for move in range(1, num_moves + 1):
        from_peg = pegs[((move & move - 1) % 3)]
        to_peg = pegs[(((move | move - 1) + 1) % 3)]
        print(f"Move disk from source {from_peg} to destination {to_peg}")

n = 4
dark_abyss(n, 'A', 'B', 'C')