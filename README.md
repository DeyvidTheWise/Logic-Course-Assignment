# Knight's Tour Problem

The Knight's Tour problem is a classic chess problem where a knight is placed on an empty chessboard and must move according to the rules of chess such that it visits each square exactly once.

## Existing Algorithms

### Depth-First Search (DFS)

Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking. In the context of the Knight's Tour problem, DFS is implemented with backtracking to find a valid sequence of moves for the knight.

**Advantages:**

- DFS can find a solution with less memory overhead than BFS, as it only needs to store the current path on the stack.
- It's easier to implement using recursion.

**Disadvantages:**

- DFS can be slower than other algorithms, as it may need to backtrack often.
- It does not guarantee the shortest path to a solution.

**Time complexity:** O(N!), where N is the number of squares on the chessboard.

### Breadth-First Search (BFS)

Breadth-First Search (BFS) is a graph traversal algorithm that visits all the vertices at the same depth level before moving on to the next level. In the context of the Knight's Tour problem, BFS is used to find the shortest sequence of moves for the knight to visit every square.

**Advantages:**

- BFS guarantees the shortest path to a solution.
- It can handle larger problem spaces, as it does not suffer from deep recursion.

**Disadvantages:**

- BFS requires more memory than DFS, as it stores all vertices at the same depth level in a queue.
- It can be slower than DFS for some problem instances.

**Time complexity:** O(N), where N is the number of squares on the chessboard.

## ShadowWalker Algorithm

The ShadowWalker algorithm is an original algorithm designed to solve the Knight's Tour problem. It uses a combination of heuristics and backtracking to find a valid sequence of moves for the knight. The name "ShadowWalker" is meant to evoke a sense of stealth and agility, reflecting the knight's ability to move in unconventional ways across the chessboard.

**Advantages:**

- The ShadowWalker algorithm incorporates heuristics, which can lead to more efficient search and quicker solutions.
- It can be more efficient than traditional DFS and BFS for certain problem instances.

**Disadvantages:**

- The algorithm's performance may vary depending on the choice of heuristic.
- It may be more complex to implement than standard DFS and BFS.

**Time complexity:** Varies depending on the chosen heuristic and problem instance.

# Springerproblem

Das Springerproblem ist ein klassisches Schachproblem, bei dem ein Springer auf einem leeren Schachbrett platziert wird und sich gemäß den Schachregeln so bewegen muss, dass er jedes Feld genau einmal besucht.

## Existierende Algorithmen

### Tiefensuche (DFS)

Die Tiefensuche (DFS) ist ein Graphentraversierungsalgorithmus, der so weit wie möglich entlang jeder Verzweigung sucht, bevor er zurückverfolgt wird. Im Kontext des Springerproblems wird DFS mit Backtracking implementiert, um eine gültige Zugfolge für den Springer zu finden.

**Vorteile:**

- DFS kann eine Lösung mit weniger Speicherplatz finden als BFS, da es nur den aktuellen Pfad auf dem Stapel speichern muss.
- Es ist einfacher, die Rekursion zu implementieren.

**Nachteile:**

- DFS kann langsamer als andere Algorithmen sein, da es möglicherweise häufig zurückverfolgt werden muss.
- DFS garantiert nicht den kürzesten Weg zu einer Lösung.

**Zeitkomplexität:** O(N!), wobei N die Anzahl der Felder auf dem Schachbrett ist.

### Breitensuche (BFS)

Die Breitensuche (BFS) ist ein Graphentraversierungsalgorithmus, der alle Knoten auf der gleichen Tiefe besucht, bevor er zur nächsten Tiefe übergeht. Im Kontext des Springerproblems wird BFS verwendet, um die kürzeste Zugfolge für den Springer zu finden, um jedes Feld zu besuchen.

**Vorteile:**

- BFS garantiert den kürzesten Weg zu einer Lösung.
- Es kann größere Problembereiche bewältigen, da es nicht unter tiefer Rekursion leidet.

**Nachteile:**

- BFS benötigt mehr Speicher als DFS, da es alle Knoten auf der gleichen Tiefe in einer Warteschlange speichert.
- Es kann langsamer als DFS für einige Problemfälle sein.

**Zeitkomplexität:** O(N), wobei N die Anzahl der Felder auf dem Schachbrett ist.

## ShadowWalker Algorithmus

Der ShadowWalker Algorithmus ist ein origineller Algorithmus zur Lösung des Springerproblems. Er verwendet eine Kombination aus Heuristiken und Backtracking, um eine gültige Zugfolge für den Springer zu finden. Der Name "ShadowWalker" soll ein Gefühl von Heimlichkeit und Wendigkeit vermitteln, das die Fähigkeit des Springers widerspiegelt, sich auf unkonventionelle Weise über das Schachbrett zu bewegen.

**Vorteile:**

- Der ShadowWalker-Algorithmus beinhaltet Heuristiken, die zu einer effizienteren Suche und schnelleren Lösungen führen können.
- Er kann bei bestimmten Problemfällen effizienter sein als herkömmliche DFS- und BFS-Methoden.

**Nachteile:**

- Die Leistung des Algorithmus kann je nach Wahl der Heuristik variieren.
- Es kann komplexer sein, ihn im Vergleich zu standardmäßigen DFS- und BFS-Methoden zu implementieren.

**Zeitkomplexität:** Hängt von der gewählten Heuristik und dem Problemfall ab.

# Eight Queens Problem

The Eight Queens problem is a classic chess problem where eight queens are placed on an 8x8 chessboard in such a way that no two queens threaten each other. This means that no two queens should be on the same row, column, or diagonal.

## Existing Algorithms

### Depth-First Search (DFS)

Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking. In the context of the Eight Queens problem, DFS is implemented with backtracking to find a valid arrangement of queens on the chessboard.

**Advantages:**

- DFS can find a solution with less memory overhead than BFS, as it only needs to store the current path on the stack.
- It's easier to implement using recursion.

**Disadvantages:**

- DFS can be slower than other algorithms, as it may need to backtrack often.
- It does not guarantee the shortest path to a solution.

**Time complexity:** O(N!), where N is the number of squares on the chessboard.

## RegalRuler Algorithm

The RegalRuler algorithm is an original algorithm designed to solve the Eight Queens problem. It uses a combination of heuristics and backtracking to find a valid arrangement of queens on the chessboard. The name "RegalRuler" is meant to evoke a sense of power and authority, reflecting the dominance of the queen piece in the game of chess.

**Advantages:**

- The RegalRuler algorithm incorporates heuristics, which can lead to more efficient search and quicker solutions.
- It can be more efficient than traditional DFS for certain problem instances.

**Disadvantages:**

- The algorithm's performance may vary depending on the choice of heuristic.
- It may be more complex to implement than standard DFS.

**Time complexity:** Varies depending on the chosen heuristic and problem instance.

# Acht-Damen-Problem

Das Acht-Damen-Problem ist ein klassisches Schachproblem, bei dem acht Damen auf einem 8x8 Schachbrett so platziert werden, dass keine zwei Damen sich gegenseitig bedrohen. Das bedeutet, dass keine zwei Damen auf der gleichen Reihe, Spalte oder Diagonale stehen dürfen.

## Existierende Algorithmen

### Tiefensuche (DFS)

Die Tiefensuche (DFS) ist ein Graphentraversierungsalgorithmus, der so weit wie möglich entlang jeder Verzweigung sucht, bevor er zurückverfolgt wird. Im Kontext des Acht-Damen-Problems wird DFS mit Backtracking implementiert, um eine gültige Anordnung der Damen auf dem Schachbrett zu finden.

**Vorteile:**

- DFS kann eine Lösung mit weniger Speicherplatz finden als BFS, da es nur den aktuellen Pfad auf dem Stapel speichern muss.
- Es ist einfacher, die Rekursion zu implementieren.

**Nachteile:**

- DFS kann langsamer als andere Algorithmen sein, da es möglicherweise häufig zurückverfolgt werden muss.
- Es garantiert nicht den kürzesten Weg zu einer Lösung.

**Zeitkomplexität:** O(N!), wobei N die Anzahl der Felder auf dem Schachbrett ist.

## RegalRuler Algorithmus

Der RegalRuler Algorithmus ist ein origineller Algorithmus zur Lösung des Acht-Damen-Problems. Er verwendet eine Kombination aus Heuristiken und Backtracking, um eine gültige Anordnung der Damen auf dem Schachbrett zu finden.

**Vorteile:**

- Der RegalRuler-Algorithmus beinhaltet Heuristiken, die zu einer effizienteren Suche und schnelleren Lösungen führen können.
- Er kann bei bestimmten Problemfällen effizienter sein als herkömmliche DFS-Methoden.

**Nachteile:**

- Die Leistung des Algorithmus kann je nach Wahl der Heuristik variieren.
- Es kann komplexer sein, ihn im Vergleich zu standardmäßigen DFS-Methoden zu implementieren.

**Zeitkomplexität:** Hängt von der gewählten Heuristik und dem Problemfall ab.
