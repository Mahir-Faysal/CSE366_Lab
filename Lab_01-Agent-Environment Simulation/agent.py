# agent.py
class Agent:
    def __init__(self, name, environment):
        self.name = name
        self.environment = environment
        self.position = [0, 0] # Initial position of the agent (x, y)
        self.speed = 1  # Initial speed
        self.prev_position = [0, 0]  # Track previous position for speed increase
        self.speed_increase = 1  # Amount to increase speed by
        self.max_speed = 1000  # Maximum allowed speed

    def move(self, direction):
        """Move the agent in the specified direction."""
         # Store previous position for speed calculation
        self.prev_position = self.position.copy()
        
        # Calculate movement based on speed
        movement = self.speed

        # Create new position first (without modifying self.position)
        new_position = self.position.copy()

        if direction == "up":
            self.position[1] -= movement  
        elif direction == "down":
            self.position[1] += movement  
        elif direction == "left":
            self.position[0] -= movement
        elif direction == "right":
            self.position[0] += movement

        # Make sure the agent stays within the environment boundaries
        self.position = self.environment.limit_position(self.position)
        
        # Increase speed if position changed
        if self.position != self.prev_position:
            self.increase_speed()
    
    def increase_speed(self):
        """Increase the agent's speed up to the maximum."""
        if self.speed < self.max_speed:
            self.speed += self.speed_increase
            #self.speed = min(self.speed, self.max_speed)  # Ensure we don't exceed max speed
    def status(self):
        """Print the current status of the agent."""
        print(f"{self.name} is at position {self.position}.")