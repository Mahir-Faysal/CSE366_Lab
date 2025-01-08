# Class Scheduling Optimization using Genetic Algorithm

## Overview
This project implements a class scheduling system using a **genetic algorithm** to optimize time slot assignments for students. The program visualizes the scheduling process and improves alignment with student preferences over several generations.

## Features
- **Genetic Algorithm Optimization**: Implements selection, crossover, and mutation to find optimal class schedules.
- **Class and Student Simulation**: Simulates classes with varying priorities and durations, and students with different availability and preferences.
- **Visualization**: Displays class schedules in a Pygame window, including metrics like best fitness and conflict highlights.

## Files
### `run.py`
The main script that:
- Initializes the environment and agents.
- Implements and runs the genetic algorithm.
- Visualizes scheduling and optimization progress using Pygame.

### `environment.py`
Defines the `Environment` class that:
- Initializes classes with durations and priorities.
- Defines student availability and preferences.
- Provides methods to generate schedules and draw the visualization grid.

### `agent.py`
Defines the `Student` class that:
- Represents students with unique IDs, availability, and preferences.
- Provides methods to assign classes and clear schedules.

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
   - The visualization will automatically start running and optimize the scheduling.
   - Close the Pygame window to exit the program.

## Key Components
### Genetic Algorithm
- **Fitness Function**: Evaluates conflict minimization and preference alignment.
- **Selection**: Retains the top 50% of the population based on fitness.
- **Crossover**: Combines two parents to produce offspring.
- **Mutation**: Randomly alters class assignments to maintain diversity.

### Visualization
- Displays class schedules, priorities, durations, and student preferences in a grid format.
- Shows optimization progress and best fitness scores on the screen.

## Example Output
A grid visualization showing class assignments to time slots, with metrics indicating optimization progress (best fitness, conflict minimization, etc.).

## Future Improvements
- Implement additional genetic algorithm techniques (e.g., elitism, multi-point crossover).
- Add support for dynamic class additions.
- Enhance visualization with more detailed metrics and interactivity.

---
Developed using Python, Pygame, and NumPy.

