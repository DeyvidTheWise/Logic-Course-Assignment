def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        # Bewegung der Scheibe 1 von der Quelle zum Ziel ausgeben
        print(f"Bewege Scheibe 1 von Quelle {source} zum Ziel {destination}")
        return

    # Bewege die obersten n-1 Scheiben von der Quelle zum Hilfsstift mit dem Zielstift
    tower_of_hanoi(n-1, source, auxiliary, destination)

    # Bewege die n-te Scheibe von der Quelle zum Zielstift
    print(f"Bewege Scheibe {n} von Quelle {source} zum Ziel {destination}")

    # Bewege die n-1 Scheiben vom Hilfsstift zum Zielstift mit dem Quellstift
    tower_of_hanoi(n-1, auxiliary, destination, source)

n = 4
tower_of_hanoi(n, 'A', 'B', 'C')
