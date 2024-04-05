import pygame

class main:
    def __init___():
      pass
        
    def main():
        screen = pygame.display.set_mode((300, 300)) 
        WIDTH = 500
        HEIGHT = 500

        ball = pygame.Rect((150, 400), (20, 20))
        paddle = pygame.Rect((480, 200), (20, 60))
        vx = 4
        vy = 4

        def draw():
            screen.fill('black')

        def update():
            global vx, vy
            ball.x += vx
            ball.y += vy
            if ball.bottom > HEIGHT or ball.top < 0:
                vy = -vy
            if ball.colliderect(paddle) or ball.left < 0:
                vx = -vx
            if ball.right > WIDTH:
                exit()
            if(keyboard.down):
                paddle.y += 2
            elif(keyboard.up):
                paddle.y -= 2
        
        draw()
        
        # from https://www.geeksforgeeks.org/how-to-make-a-pygame-window/

        running = True
        while running: 
    
        # for loop through the event queue   
            for event in pygame.event.get(): 
              
                # Check for QUIT event       
                if event.type == pygame.QUIT: 
                    running = False
        pygame.quit()



