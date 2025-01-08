# Agent Movement Simulation

A Python-based simulation that demonstrates agent movement in a 2D environment using Pygame. The project features an agent that can move around the screen with increasing speed and screen wrapping capabilities.

## Features

- Interactive agent movement using arrow keys
- Dynamic speed increase as the agent moves
- Screen wrapping (agent appears on opposite side when reaching boundaries)
- Real-time position and speed display
- Smooth animation with controlled frame rate

## Project Structure

The project consists of three main Python files:

- `agent.py`: Defines the Agent class with movement and speed control logic
- `environment.py`: Contains the Environment class that handles boundaries and screen wrapping
- `run.py`: Main script that initializes Pygame and runs the simulation

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/agent-movement-simulation.git
cd agent-movement-simulation
```

2. Install Pygame:
```bash
pip install pygame
```

## Usage

Run the simulation using:
```bash
python run.py
```

### Controls

- **Arrow Up**: Move agent upward
- **Arrow Down**: Move agent downward
- **Arrow Left**: Move agent left
- **Arrow Right**: Move agent right
- **Close Window**: Exit the simulation

## Implementation Details

### Agent Class
- Manages agent properties including:
  - Position tracking
  - Speed control with acceleration
  - Maximum speed limit (1000 units)
  - Movement in four directions

### Environment Class
- Handles the simulation space:
  - Defines boundaries (800x600 pixels)
  - Implements screen wrapping for continuous movement
  - Manages position validation

### Main Simulation
- 60 FPS animation
- Real-time display of agent position and speed
- Blue square represents the agent
- White background with position/speed information

## Customization

You can modify various parameters in the code to customize the simulation:

### Agent Parameters (`agent.py`)
```python
self.speed = 1          # Initial speed
self.speed_increase = 1 # Acceleration rate
self.max_speed = 1000   # Maximum speed limit
```

### Environment Parameters (`environment.py`)
```python
width = 800    # Screen width
height = 600   # Screen height
```

### Display Parameters (`run.py`)
```python
AGENT_SIZE = 40  # Size of the agent square
```

## Contributing

Feel free to fork the project and submit pull requests. You can also open issues for bugs or feature suggestions.

## License

This project is open source and available under the MIT License.