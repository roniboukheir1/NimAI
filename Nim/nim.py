import random
from typing import Self


class Nim():
    
    def __init__(self, initial = [1,3,5,7]):
        
        
        self.pile = initial.copy()
        self.player = 0
        self.winner = None
    
    def switch_player(self):
        return self.other_player(self.player)
    
    @classmethod
    def other_player(cls,player):
            return 0 if player == 1 else 1
    
    @classmethod 
    def available_action(cls, pile):
        
        actions = set()
        
        for p in range(len(pile)):
            
            for i in range(1,pile[p] + 1):
                
                actions.add((p,i))
        return actions
    
    def move(self, action):
        
        pile, count = action
        
        if pile < 0 or pile >= len(self.pile):
            raise("Invalid pile")
        
        if count < 1 or count > self.pile[pile]:
            raise("Invalid count")
        
        if self.winner:
            raise("Game is already over")

        self.pile[pile] -= count
        
        self.switch_player()
        
        if all(pile == 0 for pile in self.pile):
            self.winner = self.player
      
class NimAI():
    
    def __init__(self, alpha = 0.5, epsilon = 0.1):
        """ alpha: learning rate
            epsilon: future reward value rate
        """
        
        self.q = {}
        self.alpha = alpha 
        self.epsilon = epsilon
    
    def update(self, old_state, action, new_state, reward):
            
       pass
    def get_q_value(self, state, action):
        
        if (tuple(state), action) not in self.q:
            return 0
        else:
            return self.q[(tuple(state), action)]

    def update_q_value(self, state, action, old_q, r, future_rewards):
            
            state = tuple(state)
            
            self.q[state,action] = old_q + self.alpha * (r + future_rewards - old_q)    
        
    def best_future_reward(self,state):
        
        maxReward = 0
        for action in Nim.available_action(state):
            
            key = tuple(state),action
            if key in self.q:
                maxReward = self.q[key] if self.q[key] > maxReward else maxReward
                
        return maxReward
    def choose_action(self,state, epsilon = False):
        
        available_action = Nim.available_action(state)
        if not available_action:
            raise "No available actions"
        
        if epsilon and random.random() < self.epsilon:
               return random.choice(list(Nim.available_action(state)))
            
        bestFutureReward = self.best_future_reward(state)
        for action in Nim.available_action(state):
            
            key = tuple(state),action
            if key in self.q and self.get_q_value(state,action) == bestFutureReward:
                return action
        return available_action.pop() 
                
        
def train(n):
    
    player = NimAI()

    for i in range(n):
        
        print(f"Playing training game {i + 1}")
        game = Nim()

        last = {
            0: {"state": None, "action": None},
            1: {"state": None, "action": None}
        }
        
        while True:
            
            state = game.pile.copy()
            action = player.choose_action(state, player)

            last[game.player]["state"] = state
            last[game.player]["action"] = action
            
            game.move(action)
            new_state = game.pile.copy()
            # When game is over, update Q values with rewards
            if game.winner:
                player.update(state, action, new_state, -1)
                player.update(
                    last[game.player]["state"],
                    last[game.player]["action"],
                    new_state,
                    1
                )
                break

            # If game is continuing, no rewards yet
            elif last[game.player]["state"] is not None:
                player.update(
                    last[game.player]["state"],
                    last[game.player]["action"],
                    new_state,
                    0
                )

    print("Done training")

    # Return the trained AI
    return player


def play(ai, human_player=None):

    # If no player order set, choose human's order randomly
    if human_player is None:
        human_player = random.randint(0, 1)

    # Create new game
    game = Nim()

    # Game loop
    while True:

        # Print contents of piles
        print()
        print("Piles:")
        for i, pile in enumerate(game.piles):
            print(f"Pile {i}: {pile}")
        print()

        # Compute available actions
        available_actions = Nim.available_actions(game.piles)
        time.sleep(1)

        # Let human make a move
        if game.player == human_player:
            print("Your Turn")
            while True:
                pile = int(input("Choose Pile: "))
                count = int(input("Choose Count: "))
                if (pile, count) in available_actions:
                    break
                print("Invalid move, try again.")

        # Have AI make a move
        else:
            print("AI's Turn")
            pile, count = ai.choose_action(game.piles, epsilon=False)
            print(f"AI chose to take {count} from pile {pile}.")

        # Make move
        game.move((pile, count))

        # Check for winner
        if game.winner is not None:
            print()
            print("GAME OVER")
            winner = "Human" if game.winner == human_player else "AI"
            print(f"Winner is {winner}")
            return

