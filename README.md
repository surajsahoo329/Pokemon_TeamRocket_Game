# Pokemon and Team Rocket Game

Solves the pokemons and team rocket problem with **iterative deepening search**.

The problem is as follows:

Three pokemons and three team rocket members are on one side of a river,
along with a boat that can hold one or two people.

Find a way to get everyone to the other side,
without ever leaving a group of pokemons on one side outnumbered by the team rocket.

The current state is represented with a list '[a, b, c]'.
This list represents the number of pokemons on the wrong side,
team rocket on the wrong side, and whether the boat is on the wrong side.
Initially all the pokemons, team rocket members, and the boat are on the wrong side of the river.
The list representing the initial state is '[3, 3, 1]',
while the list representing the goal state is '[0, 0, 0]'.

The program outputs the 11 step path to the goal state to the screen.

## How to Run
'python main.py'

Please run with Python 3. The program was written with Python **3.6.3**.

Minimum screen resolution required : 1280x480
Operating System : Windows 7, Vistas, 8, 10
