# Code Summary
This file contains a class called `PongGym` which represents a pong game environment for reinforcement learning. It also contains `Paddle` and `Ball` classes that represent the paddles and ball respectively. The `PongGym` class inherits from the `Gym` class and overrides its methods.

The `PongGym` class contains methods for moving the paddles, applying actions, checking for collisions, and updating the game state.

# Class Summaries
## Paddle
This class represents a Paddle object in the game. It has the properties 'x', 'y', 'w', and 'h' representing the coordinates, width and height of the paddle, respectively. It has methods to draw the paddle on the game screen and to detect collisions with other objects in the game.

## Ball
This class represents a Ball object in the game. It has the properties 'x', 'y', 'dx', and 'dy' representing the coordinates and speeds of the ball, respectively. It has a method to draw the ball on the game screen.

## PongGym
This class represents the game environment for reinforcement learning. It inherits from the `Gym` class, and overrides its methods. It contains properties for the paddles and ball, as well as methods for moving paddles, applying actions, checking for collisions, and updating game state.

# Method Summaries
## Paddle.drawPaddle(curState)
The `drawPaddle` method of the `Paddle` class takes in `curState` which is a 2D numpy array representing the game screen. It updates the relevant section of `curState` to draw the paddle.

## Paddle.detectHit(x, y, w, h)
The `detectHit` method of the `Paddle` class takes in the coordinates (`x` and `y`) and dimensions (`w` and `h`) of a rectangle, and checks if it collides with the paddle.

## Ball.drawBall(curState)
The `drawBall` method of the `Ball` class takes in `curState` which is a 2D numpy array representing the game screen. It updates the relevant section of `curState` to draw the ball.

## PongGym.paddleRUp()
This method moves the right paddle up on the screen, given that it won't go off the screen.

## PongGym.paddleRDown()
This method moves the right paddle down on the screen, given that it won't go off the screen.

## PongGym.paddleLUp()
This method moves the left paddle up on the screen, given that it won't go off the screen.

## PongGym.paddleLDown()
This method moves the left paddle down on the screen, given that it won't go off the screen.

## PongGym.applyAction(action)
This method applies the specified action to the game, and returns the updated game state.

## PongGym.update()
This method updates the game state after applying an action.

## PongGym.reset()
This method resets the game state to its initial values.

# Example Usage
```python
env = PongGym(500, 600) # initialize the game environment with a screen size of 500x600

curState = env.get_state() # get the current game state

env.paddleRUp() # move the right paddle up

action = 1 # specify an action to apply
rewards = env.applyAction(action) # apply the action and get the rewards

curState = env.get_state() # get the updated game state
```