def dark_abyss(n):
    # Berechne die Gesamtzahl der Züge
    num_moves = 2 ** n - 1
    pegs = ["A", "B", "C"]

    # Durchlaufe jeden Zug
    for move in range(1, num_moves + 1):
        # Bestimme den Ausgangsstab mit Hilfe von Bitoperationen
        from_peg = pegs[((move & move - 1) % 3)]
        # Bestimme den Zielstab mit Hilfe von Bitoperationen
        to_peg = pegs[(((move | move - 1) + 1) % 3)]
        # Drucke den Zug
        print(f"Move disk from peg {from_peg} to peg {to_peg}")

n = 4
dark_abyss(n)