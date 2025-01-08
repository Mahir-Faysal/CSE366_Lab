# agent.py
import pygame
from collections import deque
import heapq
import math

class Agent(pygame.sprite.Sprite):
    def __init__(self, environment, grid_size):
        super().__init__()
        self.image = pygame.Surface((grid_size, grid_size))
        self.image.fill((0, 0, 255))  # Agent color is blue
        self.rect = self.image.get_rect()
        self.grid_size = grid_size
        self.environment = environment
        self.position = [0, 0]  # Starting at the top-left corner of the grid
        self.rect.topleft = (0, 0)
        self.task_completed = 0
        self.completed_tasks = []
        self.path = []  # List of positions to follow
        self.moving = False  # Flag to indicate if the agent is moving
        self.total_path_cost = 0  # Track total path cost
        self.current_algorithm = 'UCS'  # Default algorithm

    def switch_algorithm(self):
        """Toggle between UCS and A* algorithms"""
        self.current_algorithm = 'A*' if self.current_algorithm == 'UCS' else 'UCS'
        # Reset path and cost when switching
        self.path = []
        self.total_path_cost = 0
        self.task_completed = 0
        self.completed_tasks = []

    def manhattan_distance(self, pos1, pos2):
        """Calculate Manhattan distance between two positions"""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def move(self):
        """Move the agent along the path."""
        if self.path:
            next_position = self.path.pop(0)
            # Calculate path cost (uniform cost is always 1 for grid movement)
            path_cost = 1
            self.total_path_cost += path_cost
            
            self.position = list(next_position)
            self.rect.topleft = (self.position[0] * self.grid_size, self.position[1] * self.grid_size)
            self.check_task_completion()
        else:
            self.moving = False  # Stop moving when path is exhausted

    def check_task_completion(self):
        """Check if the agent has reached a task location."""
        position_tuple = tuple(self.position)
        if position_tuple in self.environment.task_locations:
            task_number = self.environment.task_locations.pop(position_tuple)
            self.task_completed += 1
            self.completed_tasks.append(task_number)
            #self.image.fill((0, 128, 0))

    def find_path_ucs(self, target):
        """Uniform Cost Search pathfinding"""
        start = tuple(self.position)
        goal = target
        
        # Priority queue for UCS
        pq = [(0, start, [start])]
        visited = set()

        while pq:
            current_cost, current_pos, path = heapq.heappop(pq)

            if current_pos == goal:
                return path

            if current_pos in visited:
                continue
            visited.add(current_pos)

            for neighbor in self.get_neighbors(current_pos[0], current_pos[1]):
                if neighbor not in visited:
                    new_cost = current_cost + 1  # Uniform cost
                    new_path = path + [neighbor]
                    heapq.heappush(pq, (new_cost, neighbor, new_path))

        return None

    def find_path_astar(self, target):
        """A* Search pathfinding"""
        start = tuple(self.position)
        goal = target
        
        # Priority queue for A*
        pq = [(0, 0, start, [start])]  # (f_score, g_score, position, path)
        visited = set()

        while pq:
            _, g_score, current_pos, path = heapq.heappop(pq)

            if current_pos == goal:
                return path

            if current_pos in visited:
                continue
            visited.add(current_pos)

            for neighbor in self.get_neighbors(current_pos[0], current_pos[1]):
                if neighbor not in visited:
                    new_g_score = g_score + 1
                    h_score = self.manhattan_distance(neighbor, goal)
                    f_score = new_g_score + h_score
                    new_path = path + [neighbor]
                    heapq.heappush(pq, (f_score, new_g_score, neighbor, new_path))

        return None

    def find_nearest_task(self):
        """Find the nearest task based on the current algorithm"""
        nearest_task = None
        shortest_path = None
        for task_position in self.environment.task_locations.keys():
            # Select path finding algorithm dynamically
            path = (self.find_path_ucs(task_position) 
                    if self.current_algorithm == 'UCS' 
                    else self.find_path_astar(task_position))
            
            if path:
                if not shortest_path or len(path) < len(shortest_path):
                    shortest_path = path
                    nearest_task = task_position

        if shortest_path:
            self.path = shortest_path[1:]  # Exclude the current position
            self.moving = True

    def get_neighbors(self, x, y):
        """Get walkable neighboring positions."""
        neighbors = []
        directions = [("up", (0, -1)), ("down", (0, 1)), ("left", (-1, 0)), ("right", (1, 0))]
        for _, (dx, dy) in directions:
            nx, ny = x + dx, y + dy
            if self.environment.is_within_bounds(nx, ny) and not self.environment.is_barrier(nx, ny):
                neighbors.append((nx, ny))
        return neighbors