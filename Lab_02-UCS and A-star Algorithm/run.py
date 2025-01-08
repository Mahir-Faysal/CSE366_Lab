# run.py
import pygame
import sys
from agent import Agent
from environment import Environment

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 800
GRID_SIZE = 40
STATUS_WIDTH = 300
BACKGROUND_COLOR = (255, 255, 255)
BARRIER_COLOR = (0, 0, 0)       # Barrier color is black
TASK_COLOR = (255, 0, 0)        # Task color is red
TEXT_COLOR = (0, 0, 0)
green = (0, 128, 0)
BUTTON_COLOR = (0, 200, 0)
BUTTON_HOVER_COLOR = (0, 255, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)
MOVEMENT_DELAY = 70  # Milliseconds between movements

def main():
    pygame.init()

    # Set up display with an additional status panel
    screen = pygame.display.set_mode((WINDOW_WIDTH + STATUS_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pathfinding Algorithm Simulation")

    # Clock to control frame rate
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 24)

    # Initialize environment and agent
    environment = Environment(WINDOW_WIDTH, WINDOW_HEIGHT, GRID_SIZE, num_tasks=5, num_barriers=15)
    initial_task_locations = environment.task_locations.copy()  # Save initial task locations
    initial_barrier_locations = environment.barrier_locations.copy()  # Save initial barrier locations
    agent = Agent(environment, GRID_SIZE)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(agent)

    # Algorithm buttons
    button_spacing = 20
    # Button dimensions
    button_width, button_height = 150, 50

    ucs_button_y = WINDOW_HEIGHT -  4 * button_height - button_spacing
    astar_button_y = WINDOW_HEIGHT - 2 * button_height

    ucs_button_rect = pygame.Rect(
        WINDOW_WIDTH + (STATUS_WIDTH - button_width) // 2, 
        ucs_button_y, 
        button_width, 
        button_height
    )
    astar_button_rect = pygame.Rect(
        WINDOW_WIDTH + (STATUS_WIDTH - button_width) // 2, 
        astar_button_y, 
        button_width, 
        button_height
    )


    selected_algorithm = None  # Algorithm choice is initially None
    simulation_started = False

    # Performance storage
    performance = {
        "UCS": None,
        "A*": None
    }

    # Variables for movement delay
    last_move_time = pygame.time.get_ticks()

    def reset_environment():
        """Reset environment and agent state to initial values."""
        environment.task_locations = initial_task_locations.copy()
        environment.barrier_locations = initial_barrier_locations.copy()
        agent.path = []
        agent.total_path_cost = 0
        agent.task_completed = 0
        agent.completed_tasks = []
        agent.position = [0, 0]
        agent.rect.topleft = (0, 0)
        agent.moving = False

    # Main loop
    running = True
    while running:
        clock.tick(60)  # Limit to 60 FPS

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Algorithm selection starts the simulation
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ucs_button_rect.collidepoint(event.pos):
                    selected_algorithm = 'UCS'
                elif astar_button_rect.collidepoint(event.pos):
                    selected_algorithm = 'A*'

                if selected_algorithm:
                    simulation_started = True
                    reset_environment()
                    agent.current_algorithm = selected_algorithm
                    agent.find_nearest_task()

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Draw grid and barriers
        for x in range(environment.columns):
            for y in range(environment.rows):
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)  # Draw grid lines

        # Draw barriers
        for (bx, by) in environment.barrier_locations:
            barrier_rect = pygame.Rect(bx * GRID_SIZE, by * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, BARRIER_COLOR, barrier_rect)

        # Draw tasks with numbers
        for (tx, ty), task_number in environment.task_locations.items():
            task_rect = pygame.Rect(tx * GRID_SIZE, ty * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, TASK_COLOR, task_rect)
            # Draw task number
            task_num_surface = font.render(str(task_number), True, (255, 255, 255))
            task_num_rect = task_num_surface.get_rect(center=task_rect.center)
            screen.blit(task_num_surface, task_num_rect)

        # Draw agent
        all_sprites.draw(screen)

        # Display status panel
        status_x = WINDOW_WIDTH + 10
        algorithm_text = f"Algorithm: {selected_algorithm or 'None'}"
        status_surface = font.render(algorithm_text, True, green)
        screen.blit(status_surface, (status_x, 20))

        position_text = f"Position: {agent.position}"
        position_surface = font.render(position_text, True, TEXT_COLOR)
        screen.blit(position_surface, (status_x, 400))
        completed_tasks_text = f"Completed Tasks: {agent.completed_tasks}"
        completed_tasks_surface = font.render(completed_tasks_text, True, TEXT_COLOR)
        screen.blit(completed_tasks_surface, (status_x, 420))

        # Show performance for both algorithms
        y_offset = 60
        for algo in ["UCS", "A*"]:
            algo_title = f"{algo} Performance:"
            
            algo_surface = font.render(algo_title, True, TEXT_COLOR)
            screen.blit(algo_surface, (status_x, y_offset))
            #screen.blit(completed_tasks_surface, (status_x, 140))
            y_offset += 20

            if performance[algo]:
                details = performance[algo]
                task_surface = font.render(f"Tasks Completed: {details['tasks']}", True, TEXT_COLOR)
                cost_surface = font.render(f"Path Cost: {details['cost']}", True, TEXT_COLOR)
                completed_surface = font.render(f"Path: {details['path']}", True, TEXT_COLOR)
                screen.blit(task_surface, (status_x, y_offset))
                screen.blit(cost_surface, (status_x, y_offset + 20))
                screen.blit(completed_surface, (status_x, y_offset + 40))
                y_offset += 120
            else:
                no_data_surface = font.render("No data yet", True, TEXT_COLOR)
                screen.blit(no_data_surface, (status_x, y_offset))
                y_offset += 100

        # Draw algorithm buttons
        for rect, text in [(ucs_button_rect, "UCS"), (astar_button_rect, "A*")]:
            mouse_pos = pygame.mouse.get_pos()
            color = BUTTON_HOVER_COLOR if rect.collidepoint(mouse_pos) else BUTTON_COLOR
            pygame.draw.rect(screen, color, rect)
            button_text = font.render(text, True, BUTTON_TEXT_COLOR)
            text_rect = button_text.get_rect(center=rect.center)
            screen.blit(button_text, text_rect)

        # Automatic movement with delay
        if simulation_started:
            current_time = pygame.time.get_ticks()
            if current_time - last_move_time > MOVEMENT_DELAY:
                if not agent.moving and environment.task_locations:
                    # Find the nearest task
                    agent.find_nearest_task()
                elif agent.moving:
                    agent.move()
                last_move_time = current_time

                # Check if all tasks are completed
                if not environment.task_locations:
                    # Store performance data
                    performance[selected_algorithm] = {
                        "tasks": agent.task_completed,
                        "cost": agent.total_path_cost,
                        "path": agent.completed_tasks,
                    }
                    simulation_started = False

        pygame.draw.line(screen, (0, 0, 0), (WINDOW_WIDTH, 0), (WINDOW_WIDTH, WINDOW_HEIGHT))

        # Update the display
        pygame.display.flip()

    # Quit Pygame properly
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
