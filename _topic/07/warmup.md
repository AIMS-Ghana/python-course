[Yahtzee](https://en.wikipedia.org/wiki/Yahtzee) is a dice game.

There are 13 rounds.  In each round, a player rolls 5 dice.  They may pick any of those dice to re-roll, and after that re-roll, they may again re-roll any number of dice on last time.

After completing their rolls, they assign their final five dice to one of 13 scoring categories:

| Category |   Value   |                Category                |        Value         |
|:--------:|:---------:|:--------------------------------------:|:--------------------:|
|   Aces   | sum of 1s |                 Chance                 |   sum of all dice    |
|    2s    | sum of 2s |              3 of a kind               | sum of all dice OR 0 |
|    3s    | sum of 3s |              4 of a kind               | sum of all dice OR 0 |
|    4s    | sum of 4s | 3 of a kind, 2 of another (Full House) |       25 OR 0        |
|    5s    | sum of 5s |               seq. of 4                |       30 OR 0        |
|    6s    | sum of 6s |               seq. of 5                |       40 OR 0        |

And a special category, *Yahtzee* for 5 of a kind, worth 50 OR 0.

Once a category has been used, it is no longer available.  The "OR 0" categories
award their points if the criteria is met.  The *Yahtzee* is special because of the
*Yahtzee Bonus*: if a player throws 5-of-a-kind and they have already scored a *Yahtzee*,
then they get 100 points + whatever points for the category they assign the roll to, and they may use the roll to satisfy the Full House or Sequence categories.