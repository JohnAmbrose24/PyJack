# PyJack

A collection of Python blackjack implementations, built as a teaching resource.

## Files

### `pyjack_game.py`
A blackjack game in progress by John Ambrose. Started as a procedural script and is 
evolving toward OOP — currently a hybrid of both styles.

Has two classes so far:
- `Card` — tracks rank, suit, and value; includes ace adjustment logic
- `Player` — tracks name, wallet, bet, hand, and win/loss record

Supporting functions handle dealing, printing hands, calculating hand values, 
and fixing aces when a hand goes over 21. The game logic (betting, dealing, 
hit/stand loop) runs at the module level rather than inside a class or `main()`.

Notable: card values are assigned with a chain of `if` statements in `__init__` — 
a good candidate for refactoring to a dictionary lookup later. (CLEARED)

Update as of 5/21/2026: 
- Card value instantiation has improved using the dictionary lookup method.
- Additional supporting function determines a winner between two players' hands.
- Game-running module is now contained in a while-loop, continuing to run new rounds until the player runs out of money.

Areas of Improvement:
- Turning the modular game logic (betting, dealing, hit/stand loop) into functions ran inside a `main()` function. 

**Status:** Work in progress — multiple rounds playable, game continues until player's balance is depleted. 
