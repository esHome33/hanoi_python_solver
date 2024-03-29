# Tower of Hanoi solver package.
## A package for an old mathematical game :
Invented by the french mathematician Edouard Lucas and published in 1889, this game presents three rods and a number of disks that can be sled on the rods. There are also three easy rules : 
- only one disk can be moved 
- a move is done from a rod to another one
- you always can slide a disk on an empty rod. If a destination rod contains disks, you must not slide a disk over a smaller disk.

This package constructs data structures representing the game (with methods like `executeMove()` or `possibleMoves()` ) and a static function named `discoverAllPositions()` that that allows you to discover all the positions the game can take. This is particularly useful when you're not in the starting position and want to know the shortest route to a final position.

## ABC notation :
A game position can be represented by an ***ABC notation*** string : rods a named **A**, **B** and **C**. The letter placed in the most left position in the string is the name of the rod where the biggest disk is place. The letter placed in the most right position in the string gives the position of the smallest disk. Thus, the length of an ABC notation string is equal to the total number of disks in the game.

Here's an example from [Mathoutils.fr](https://www.mathoutils.fr):

![example position](https://www.mathoutils.fr/wp-content/uploads/2022/08/expl2.png)

this position is described by the ABC notation string `"AABCB"`

## Combination of all n letters of an ABC notation string (when dealing with n disks) :

When dealing with 3 rods and n disks, there are $3^n$ different positions of n disks on the 3 rods. It also possible to create a graph that connects each position to the 2 or 3 legal allowed moves starting from this position (thus joining two or three other positions).

This package contains a method that constructs such a graph, in which each node is labelled with an ABC notation string. This allows you to easily get the shortest path from a position to another one.

I implemented my own graph structure and the only methods needed to solve the problem of a Tower of Hanoi game : that is why this package depends on no other package.

## how to use this package :

Install it from PyPI :
```shell
pip install hanoi-python-solver
```

After installation succeeded, open a new *.py file and create a python program. Create a new Tower of Hanoi game by instancianting a new `Hanoi` object and indicate the total desired number of disks. The starting situation of disks is that all disks are stacked on the **A** rod.

Then, get all the possible legal moves from this new position or use the `move()` method to play as you like.

After a move, try to get the new ABC notation of the game with `getABC()` method from Hanoi.

If you want to get the path to the goal (solution, end position, ...) or any other position of your choice : call Hanoi class `pathToSolution(position)` method to get a dictionnary with "path" and "moves" keys, that lists all different ABC notation string to follow in order to reach the end position, and a list of moves to play from current position to reach the end position.

Here is a simple Tower of Hanoi player in Python language :

```python

from hanoi_python_solver.hanoi import Hanoi

h = Hanoi(3)
print("You are playing with Tower of Hanoi game and 3 disks all placed on 1st rod ! Enjoy ...\n")
s=""
while s != "END":
    s = input("a move or SIT or SOL or END : ")
    if s == "SIT":
        print(h.getABC())
    elif s == "SOL":
        t = input(f" ==> position to reach ({h.nbDisks} letters) : ")
        result = h.pathToSolution(t)
        print(f"path = {result["path"]}")
        print(f"moves = {result["moves"]}")
    elif s == "END":
        break
    else:
        mvt = s.split(",")
        if len(mvt) == 2:
            m1 = mvt[0]
            m2 = mvt[1]
            result_move = h.move((int(m1), int(m2)))
            if not result_move:
                print("Move not done !")
            else:
                print(f"after move ({m1},{m2}) : {h.getABC()}")
        else:
            print("Bad move ... try 1,2")

```

#

> *&#169; ESHome33 - feb 2024*