# run.py
import pygame
from agent import Agent
from environment import Environment
def main():
     # Initialize Pygame
    pygame.init()

    # Create an environment with dimensions 10x10
    env = Environment(width=800, height=600)
    #env.display()

    # Create an agent within the environment
    agent = Agent(name="Agent A", environment=env)
    #agent.status()

    # Set up the display
    screen = pygame.display.set_mode((env.width, env.height))
    pygame.display.set_caption("Lab_1 Task")

    # Colors
    WHITE = (255, 255, 255)
    
    # Agent size
    AGENT_SIZE = 40

    # Main game loop
    running = True
    clock = pygame.time.Clock()

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Handle continuous keyboard input
        keys = pygame.key.get_pressed()
        # Store initial position to check if movement occurred
        initial_pos = agent.position.copy()

        if keys[pygame.K_UP]:
            agent.move("up")
        if keys[pygame.K_DOWN]:
            agent.move("down")
        if keys[pygame.K_LEFT]:
            agent.move("left")
        if keys[pygame.K_RIGHT]:
            agent.move("right")
        
        # Clear screen
        screen.fill(WHITE)
        
        # Draw agent as a square
        pygame.draw.rect(screen, (0, 0, 255), 
                        (agent.position[0], agent.position[1], 
                         AGENT_SIZE, AGENT_SIZE))
        
        # Display the agent's position and speed
        font = pygame.font.Font(None, 36)
        text = font.render(f"Agent position: ({int(agent.position[0])}, {int(agent.position[1])}) | Speed: {agent.speed:d}", True, (1, 0, 0))
        screen.blit(text, (200, 0))
        
        # Update display
        pygame.display.flip()
        
        # Control frame rate
        clock.tick(60)
    
    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()