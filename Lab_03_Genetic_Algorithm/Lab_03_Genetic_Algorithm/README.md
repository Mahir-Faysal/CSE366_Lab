# Task Assignment and Visualization using Genetic Algorithm

## Overview
This project implements a task assignment system using a **genetic algorithm** to distribute tasks among robots efficiently. The program visualizes the task allocation process and optimizes the workload distribution over several generations.

## Features
- **Genetic Algorithm Optimization**: Implements selection, crossover, and mutation to find optimal task assignments.
- **Task and Robot Simulation**: Simulates tasks with varying priorities and durations and robots with different efficiencies.
- **Visualization**: Displays task assignments in a Pygame window, including metrics like best fitness and workload balance.

## Files
### `run.py`
The main script that:
- Initializes the environment and agents.
- Implements and runs the genetic algorithm.
- Visualizes task assignments and optimization progress using Pygame.

### `environment.py`
Defines the `Environment` class that:
- Initializes tasks with durations and priorities.
- Defines robot efficiencies.
- Provides methods to generate task assignments and draw the visualization grid.

### `agent.py`
Defines the `Agent` class that:
- Represents robots with unique IDs and efficiency factors.
- Provides methods to assign tasks and calculate workload.

## How to Run
1. **Install Dependencies**:
   ```bash
   pip install pygame numpy
   ```

2. **Run the Program**:
   ```bash
   python run.py
   ```

3. **Control and Exit**:
   - The visualization will automatically start running and optimize the task allocation.
   - Close the Pygame window to exit the program.

## Key Components
### Genetic Algorithm
- **Fitness Function**: Evaluates workload balance and maximum task completion time among robots.
- **Selection**: Retains the top 50% of the population based on fitness.
- **Crossover**: Combines two parents to produce offspring.
- **Mutation**: Randomly alters task assignments to maintain diversity.

### Visualization
- Displays tasks, priorities, durations, and robot preferences in a grid format.
- Shows optimization progress and best fitness scores on the screen.

## Customization
- **Parameters**: Modify constants in `run.py` for experimentation:
  - `num_tasks`: Number of tasks.
  - `num_robots`: Number of robots.
  - `population_size`, `mutation_rate`, `n_generations`: Genetic algorithm parameters.
- **Task and Robot Properties**: Adjust task durations, priorities, and robot efficiencies in `environment.py`.

## Example Output
A grid visualization showing tasks assigned to robots, with metrics indicating optimization progress (best fitness, workload balance, etc.).

## Future Improvements
- Implement additional genetic algorithm techniques (e.g., elitism, multi-point crossover).
- Add support for dynamic task arrivals.
- Enhance visualization with more detailed metrics and interactivity.


---
Developed using Python, Pygame, and NumPy.

