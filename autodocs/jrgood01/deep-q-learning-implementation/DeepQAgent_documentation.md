# DeepQAgent.py Documentation

## Code Summary

This Python file contains the `Agent` class that implements the Deep Q-Learning algorithm.

The `Agent` constructor takes in the following parameters:
- `input_width` and `input_height`: integers representing the width and height of the input state.
- `action_set_size`: integer representing the number of possible actions.
- `model_update_horizon`: optional integer representing the number of state transitions before updating the neural network model. Default value is 20.
- `discount_factor`: optional float representing the discount factor used for future rewards in the Bellman update equation. Default value is 0.8.
- `alpha`: optional float representing the learning rate used for the Bellman update equation. Default value is 0.8.
- `epsilon_greedy`: optional float representing the probability of taking a random action instead of the action with the highest Q-value. Default value is 0.1.

The `Agent` class has the following methods:
- `determineAction`: takes in a `state` tensor and returns an action. The `epsilon_greedy` parameter determines whether the method should randomly choose an action (with probability `epsilon_greedy`) or choose an action with the highest Q-value.
- `apply`: takes in `state`, `action`, and `reward` parameters and stores them in the agent's history. If the history is longer than the max buffer length (which is `model_update_horizon * 10`), it calls the `updateWeights` method.
- `calculateBellmanUpdateValue`: takes in `loc` and `action` parameters and calculates the Bellman update equation for that action.
- `updateWeights`: updates the neural network model using stochastic gradient descent.

## Method Summaries

### determineAction

```python
def determineAction(self, state, epsilon_greedy=True):
```

This method takes in a `state` tensor and returns an action. The `epsilon_greedy` parameter determines whether the method should randomly choose an action (with probability `epsilon_greedy`) or choose an action with the highest Q-value.

#### Parameters:
- `state`: a tensor representing the current state of the environment
- `epsilon_greedy`: a boolean indicating whether to use epsilon-greedy policy or greedy policy. Default value is `True`.

#### Returns:
- An integer representing the chosen action.

### apply

```python
def apply(self, state, action, reward, training=True):
```

This method takes in `state`, `action`, and `reward` parameters and stores them in the agent's history. If the history is longer than the max buffer length (which is `model_update_horizon * 10`), it calls the `updateWeights` method.

#### Parameters:
- `state`: a tensor representing the current state of the environment
- `action`: an integer representing the chosen action
- `reward`: a float representing the reward received after taking the chosen action.
- `training`: a boolean indicating whether to train the model with the stored state and reward information. Default value is `True`.

#### Returns:
- None

### calculateBellmanUpdateValue

```python
def calculateBellmanUpdateValue(self, loc, action):
```

This method takes in `loc` and `action` parameters and calculates the Bellman update equation for that action. 

#### Parameters:
- `loc`: an integer representing the location in the Markov Decision Process.
- `action`: an integer representing the chosen action.

#### Returns:
- A tensor representing the updated Q-values.


### updateWeights

```python
def updateWeights(self):
```

This method updates the neural network model using stochastic gradient descent.

#### Parameters:
- None

#### Returns:
- None


## Example Usage

```python
import gym
import numpy as np
from DeepQAgent import Agent

env = gym.make('CartPole-v0')
input_width = 4
input_height = 1
action_set_size = 2
num_episodes = 1000

agent = Agent(input_width, input_height, action_set_size)

for episode in range(num_episodes):
    state = env.reset()
    done = False
    total_reward = 0

    while not done:
        action = agent.determineAction(state)
        next_state, reward, done, _ = env.step(action)
        agent.apply(state, action, reward)
        state = next_state
        total_reward += reward

    if episode > 50:
        agent.updateWeights()

    print(f"Episode {episode} complete. Total reward: {total_reward}")
```