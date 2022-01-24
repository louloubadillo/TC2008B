from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import SimultaneousActivation
from mesa.datacollection import DataCollector
import numpy as np
import pandas as pd

#Animation Libraries
#matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.rcParams["animation.html"] = "jshtml"
matplotlib.rcParams['animation.embed_limit'] = 2**128

#Other libraries
import numpy as np
import pandas as pd
import random
import time
import datetime

def get_grid(model):
    """We need to generate the room which is a MxN grid"""
    grid = np.zeros((model.grid.width, model.grid.height))
    for (content, x, y) in model.grid.coord_iter():
        for data_content in content: 
            if isinstance(data_content, CleaningAgent):
                grid[x][y] = 2 #to differentiate in animation, it will be the darkest color
            else:
                grid[x][y] = data_content.state
    return grid


class Cell(Agent):
    """ Agent in each cell. The possible states are: clean or dirty""" 
    clean = 0
    dirty = 1
    def __init__(self, pos, model, state = clean):
        super().__init__(pos, model)
        self.x, self.y = pos
        self.state = state
        self.type = "cell"
        self.nextPos = pos


class CleaningAgent(Agent):
    """ Agent representing the cleaning machines
        If a cell is dirty, it cleans it. 
        Move to any of its neighboring cells"""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nextPos = None
        self.moves = 0
        self.type = "Robot"
        self.function ="Clean"
    
    def step(self):
        # The agent's step will go here.
        neighbors = self.model.grid.get_neighbors(
            self.pos,
            moore = True, #we want the diagonals too
            include_center = True)
        
        for neighbor in neighbors: 
            if neighbor.pos == self.pos: 
                if neighbor.state == neighbor.dirty:
                    neighbor.state = neighbor.clean #clean it
                    self.nextPos = self.pos #move
                else:
                    possible_steps = self.model.grid.get_neighborhood(
                        self.pos, 
                        moore = True, 
                        include_center = False)
                    nextPos = self.random.choice(possible_steps)
                    self.nextPos = nextPos
                break

        if self.pos != self.nextPos: 
            self.moves += 1

        self.model.grid.move_agent(self, self.nextPos)

class CleaningModel(Model):
    """A model with some number of agents."""

    def __init__(self, M, N, total_agents, dirty_cells):
        self.total_agents = total_agents
        self.dirty_cells = dirty_cells
        self.clean_cells = 1-dirty_cells
        self.grid = MultiGrid(M,N, False) 
        self.schedule = SimultaneousActivation(self)
        self.robot_list = list()

        #List of all cells
        cells = list(self.grid.empties)

        # Create agents
        for i in range(int((M*N)*dirty_cells)):
            rand_cell = random.choice(cells)
            cell = Cell(rand_cell, self)
            cell.state = cell.dirty
            self.grid.place_agent(cell, rand_cell)
            self.schedule.add(cell)
            cells.remove(rand_cell)
        
        #Empty cells are the clean ones
        clean_cells = list(self.grid.empties)
        for cells in clean_cells: 
            cell = Cell(cells, self)
            self.grid.place_agent(cell, cells)
            self.schedule.add(cell)
        
        # Add cleaning agents
        for i in range(total_agents):
            cleaner = CleaningAgent(i, self)
            self.grid.place_agent(cleaner, (1,1))
            self.schedule.add(cleaner)
            self.robot_list.append(cleaner)

        self.data_collector = DataCollector(
           model_reporters={'Grid': get_grid},
           agent_reporters={'Moves': lambda a: getattr(a, 'moves', None)} 
        )

        #Add for JSON data
        self.datacollector = DataCollector(
        model_reporters={"Grid": get_grid},
        agent_reporters={'Moves': lambda a: getattr(a, 'moves', None), 
                        'Position': lambda a: getattr(a, 'nextPos', None),
                        "Type": lambda a: getattr(a, 'type', None)}
        )
    def status_agents(self):
        data = list()
        for r in self.robot_list:
            data.append({'nextPos':r.nextPos, 'type': r.type, 'moves':r.moves, 'function':r.function})
        return data

    def step(self):
        self.data_collector.collect(self)
        self.schedule.step()

    def cleanRoom(self):
        cleaned = 0
        for cell in self.grid.coord_iter():
            cellContent, x, y = cell
            for content in cellContent:
                if isinstance(content, Cell) and content.state == content.clean:
                    cleaned += 1

        self.clean_cells = cleaned / (self.grid.width * self.grid.height)
        if self.clean_cells == 1: 
            return True
        else:
            return False