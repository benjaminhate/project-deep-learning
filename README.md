# Python Deep Learning

The project is a game where two forms on AI compete against each other.

## Library used

The project was made in Python v3 using Tenserflow and Keras.
The two AI competing are a A* algorithm and Keras Neural Network.
The interface of the game was made using Pygame.

## The game

The game is a pass-through game where one AI is controlling the Player and the other AI is controlling the Gate.

The Player is forced to move forward by one cell each time and can move to the left or the right or stay still.
The Gate can move left and right.

For the Player to win, he must pass the Gate without touching its borders.
For the Game to win, it must block the Player.

The game is also provided with an interface that allows the client to train the neural network or to play the game.
The client can modify the code to implement different types of AI or switch the AI controlling the Gate and the Player.
