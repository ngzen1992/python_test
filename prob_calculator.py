import copy
import random

class Hat():
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for ball in range(0, int(value), 1):
                self.contents.append(str(key))

    def draw(self, no_to_draw):
        all_balls_drawn = []
        if no_to_draw >= len(self.contents):
            all_balls_drawn = self.contents
            self.contents = []
        else:
            for no in range(0, no_to_draw, 1):
                ball_drawn = random.choice(self.contents)
                all_balls_drawn.append(ball_drawn)
                self.contents.remove(ball_drawn)
        
        return all_balls_drawn

    def draw_no_reduce(self, no_to_draw):
        all_balls_drawn = []
        if no_to_draw >= len(self.contents):
            all_balls_drawn = self.contents
            #self.contents = []
        else:
            for no in range(0, no_to_draw, 1):
                ball_drawn = random.choice(self.contents)
                all_balls_drawn.append(ball_drawn)
                #self.contents.remove(ball_drawn)
        
        return all_balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    total_probability = 0
    for experiment in range(0, num_experiments, 1):
        balls_drawn = hat.draw_no_reduce(num_balls_drawn)
        ### check if meet expected_balls
        fulfilled = 1
        for color, quantity in expected_balls.items():
            filtered = list(filter(lambda b: str(color) in b, balls_drawn))
            if len(filtered) < quantity:
                fulfilled = 0
                break
        
        total_probability += fulfilled

    return total_probability/num_experiments
