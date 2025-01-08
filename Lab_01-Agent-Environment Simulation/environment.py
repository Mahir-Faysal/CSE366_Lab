# environment.py
class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def limit_position(self, position):
        """Ensure the agent's position stays within the environment
        boundaries.
        x, y = position
        x = max(0, min(x, self.width - 40))
        y = max(0, min(y, self.height - 40))
        return [x, y]"""
        """Wrap the agent's position around the screen when it goes out of bounds."""
        x, y = position
        
        # Wrap horizontally
        if x < 0:
            x = self.width - 1  # Appear on right side
        elif x >= self.width:
            x = 0  # Appear on left side
            
        # Wrap vertically    
        if y < 0:
            y = self.height - 1  # Appear on bottom
        elif y >= self.height:
            y = 0  # Appear on top
            
        return [x, y]

    
    def display(self):
        """Display environment details."""
        print(f"Environment size: {self.width}x{self.height}")