# PROBABILITY CALCULATOR

""" This is an real Life Fun application using an PROBABILITY CALCULATOR, The main objective of this probability calculator is to estimate the likelihood of drawing a specified combination of colored balls from a hat, based on random draws """

""" It uses simulations to approximate the probability by performing a large number of experiments and counting successful outcomes according to the given criteria """

""" The calculated probability helps in understanding the chances of obtaining the desired ball combination """

# Starting Up, By taking the necessary imports "copy" and "random".

# "copy" module is used for creating copies of objects, ensuring that changes to one copy don't affect the other.
# "random" module provides functions for generating random numbers.
import copy
import random

# Now, Let's define a class named "Hat" and here we use initiliser and constructor method to Initialize an instance of Hat with a certain number of balls of various colors based on the provided arguments.
class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():  # For counting the number of balls
            self.contents.extend([color] * count)

# There is need to obtain the desired pobability, only when the user draws balls from the set/bunch of balls. Hence, Let's define a function named "draw".
# Allows us to draw a specified number of balls randomly from the hat.
    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            drawn_balls = self.contents 
            self.contents = []
# If the number of balls to draw is more or equal to the total number of balls, it returns all the balls and empties the hat.

# If the number of balls to draw is less, it uses random.sample to draw without replacement and updates the hat's contents accordingly.
        else:
            drawn_balls = random.sample(self.contents, num_balls) # that's why import "random" has to be used.
            for ball in drawn_balls:
                self.contents.remove(ball)
        return drawn_balls

""" Let's now, experiment with all the combinations and data we have, by defining "experiment" with various parameters as given in the Rules. This function calculates the probability based on the provided parameters.  """

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
# "hat_copy = copy.deepcopy(hat)" creates a deep copy of the hat to avoid modifying the original hat's contents during experiments.
      
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_dict = {}
        for ball in drawn_balls:
            drawn_balls_dict[ball] = drawn_balls_dict.get(ball, 0) + 1
# The function then performs the experiments, counting successful ones where the drawn balls match the expected balls.
        success = True
        for color, count in expected_balls.items():
            if color not in drawn_balls_dict or drawn_balls_dict[color] < count:
                success = False
                break

        if success:
            successful_experiments += 1
          
    """ The final Probability, is calculated by dividing the number of successful experiments by the total number of experiments"""

    return successful_experiments / num_experiments

    """ Hence, The Probability calculator has been executed successfully without any Errors """