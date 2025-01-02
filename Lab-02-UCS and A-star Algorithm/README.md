# Pathfinding Algorithm Visualization

A Python-based visualization system that demonstrates and compares two pathfinding algorithms: Uniform Cost Search (UCS) and A* Search. The system features an interactive environment where an agent navigates through a grid to complete tasks while avoiding barriers.

## Features

- Real-time visualization of pathfinding algorithms
- Interactive comparison between UCS and A* Search
- Dynamic obstacle generation
- Task-based navigation challenges
- Performance metrics tracking
- Grid-based movement system

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone this repository
2. Install the required package:
```bash
pip install pygame
```

## Project Structure

- `agent.py`: Defines the Agent class with pathfinding algorithms implementation
- `environment.py`: Handles the grid environment, tasks, and barriers generation
- `run.py`: Main script that creates the visualization window and manages the simulation

## Usage

Run the visualization by executing:
```bash
python run.py
```

## Components

### Agent
- Implements both UCS and A* pathfinding algorithms
- Tracks position and movement
- Maintains performance metrics
- Handles task completion

### Environment
- Generates random task locations
- Creates barrier positions
- Manages grid boundaries
- Tracks task completion status

### Visualization
- Grid-based display with:
  - Blue agent
  - Red task locations with numbers
  - Black barriers
  - Status panel showing current metrics
- Algorithm selection buttons
- Performance comparison display

## Algorithms

### Uniform Cost Search (UCS)
- Explores paths based on cumulative cost
- Guarantees optimal path in terms of movement cost
- Implemented with priority queue for efficiency

### A* Search
- Uses Manhattan distance heuristic
- Combines actual cost and estimated cost to goal
- Generally more efficient than UCS for directional pathfinding

## Controls

- Click the UCS or A* button to start a simulation with the respective algorithm
- Close window to exit the visualization
- Automatic movement with configurable delay

## Performance Metrics

The system tracks and displays:
- Number of tasks completed
- Total path cost
- Task completion order
- Real-time position updates

## Configuration

Key parameters that can be modified in `run.py`:
- `WINDOW_WIDTH`, `WINDOW_HEIGHT`: Window dimensions
- `GRID_SIZE`: Size of each grid cell
- `MOVEMENT_DELAY`: Time between agent moves
- Number of tasks and barriers (in Environment initialization)

## Notes

- Tasks must be completed in order of proximity
- Barriers cannot be crossed
- The agent always starts from the top-left corner
- Each algorithm's performance is recorded separately for comparison