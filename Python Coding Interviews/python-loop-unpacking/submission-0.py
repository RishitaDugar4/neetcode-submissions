from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best_n, best_s = scores[0]

    for n, s in scores:
        if s > best_s:
            best_s, best_n = s, n    
    return best_n


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
