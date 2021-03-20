# Tic-Tac-Toe-with-AI
the second algorithm I've ever "written."
has ui options commented out. currently configed to play 190 or so games a second against its self.
currently the win rate is 50/50 but it doesn't know how to tie or consider them.

#TODO: I plan to I probably could create a value for total moves made in a game,
  and use that as a weight so when the algorithm considers an attacking or blocking move,
  it also considers how much longer or shorter it would make the game and which strong(outside) and weak(inside) tiles are left
  If the confidence in winning is below 50% maximize total moves made in game To maximize the likelihood of a tie.
