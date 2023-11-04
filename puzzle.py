from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Ground Rules
    Not(And(AKnight, AKnave)),
    Or(AKnave, AKnight),

    # Statement
    Biconditional(And(AKnight, AKnave), AKnight)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Ground Rules
    And(Not(And(AKnight, AKnave)), Not(And(BKnight, BKnave))),
    And(Or(AKnave, AKnight), Or(BKnave, BKnight)),
    
    # Statements
    Biconditional(And(AKnave, BKnave), AKnight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Ground Rules
    And(Not(And(AKnight, AKnave)), Not(And(BKnight, BKnave))),
    And(Or(AKnave, AKnight), Or(BKnave, BKnight)),

    # Statements
    Biconditional(Biconditional(AKnight, BKnight), AKnight),
    Biconditional(Not(Biconditional(AKnight, BKnight)), BKnight)    
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Ground Rules
    And(Not(And(AKnight, AKnave)), Not(And(BKnight, BKnave)), Not(And(CKnight, CKnave))),
    And(Or(AKnave, AKnight), Or(BKnave, BKnight), Or(CKnave, CKnight)),

    # Statements
    Biconditional(Or(Biconditional(AKnight, AKnight), Biconditional(Not(AKnave), AKnave)), AKnight),
    Biconditional(Biconditional(Not(AKnave), AKnave), BKnight),
    Biconditional(CKnave, BKnight),
    Biconditional(AKnight, CKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
