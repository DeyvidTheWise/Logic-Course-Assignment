def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        # Print the move of disk 1 from source to destination
        print(f"Move disk 1 from source {source} to destination {destination}")
        return

    # Move the top n-1 disks from the source to the auxiliary peg using the destination peg
    tower_of_hanoi(n-1, source, auxiliary, destination)

    # Move the nth disk from the source to the destination peg
    print(f"Move disk {n} from source {source} to destination {destination}")

    # Move the n-1 disks from the auxiliary peg to the destination peg using the source peg
    tower_of_hanoi(n-1, auxiliary, destination, source)

n = 4
tower_of_hanoi(n, 'A', 'B', 'C')