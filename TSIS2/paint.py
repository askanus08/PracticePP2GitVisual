import pygame
import datetime
from tools import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 560))
    clock = pygame.time.Clock()

    # Default settings
    radius = 5
    color_mode = 'blue'
    tool = 'brush'

    drawings = []  # stores all drawn objects
    current_stroke = None
    shape_start = None
    drawing = False

    # Text tool variables
    text_mode = False
    text_input = ""
    text_pos = (0, 0)

    while True:
        pressed = pygame.key.get_pressed()
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            # Exit program
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:

                # 🔒 TEXT MODE → only handle typing
                if text_mode:
                    if event.key == pygame.K_RETURN:
                        drawings.append({
                            "type": "text",
                            "text": text_input,
                            "pos": text_pos,
                            "color": color_mode
                        })
                        text_mode = False

                    elif event.key == pygame.K_ESCAPE:
                        text_mode = False

                    elif event.key == pygame.K_BACKSPACE:
                        text_input = text_input[:-1]

                    else:
                        text_input += event.unicode

                    continue  # prevent switching tools/colors

                # Normal controls (only when NOT typing)

                if event.key == pygame.K_ESCAPE:
                    return

                # Colors
                if event.key == pygame.K_r:
                    color_mode = 'red'
                elif event.key == pygame.K_g:
                    color_mode = 'green'
                elif event.key == pygame.K_b:
                    color_mode = 'blue'

                # Tools
                elif event.key == pygame.K_p:
                    tool = 'brush'
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_o:
                    tool = 'circle'
                elif event.key == pygame.K_t:
                    tool = 'rectangle'
                elif event.key == pygame.K_l:
                    tool = 'line'
                elif event.key == pygame.K_f:
                    tool = 'fill'
                elif event.key == pygame.K_x:
                    tool = 'text'

                # Clear canvas
                elif event.key == pygame.K_c:
                    drawings.clear()

                # Brush size
                elif event.key == pygame.K_1:
                    radius = 2
                elif event.key == pygame.K_2:
                    radius = 5
                elif event.key == pygame.K_3:
                    radius = 10

                # Save canvas
                if event.key == pygame.K_s and ctrl_held:
                    filename = datetime.datetime.now().strftime("image_%Y%m%d_%H%M%S.png")
                    pygame.image.save(screen, filename)

            # Mouse pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    if tool == 'fill':
                        pixels = flood_fill(screen, event.pos[0], event.pos[1],
                                            get_base_color(color_mode))
                        if pixels:
                            drawings.append({
                                "type": "stroke",
                                "mode": color_mode,
                                "radius": 1,
                                "points": pixels
                            })

                    elif tool == 'text':
                        text_mode = True
                        text_input = ""
                        text_pos = event.pos

                    elif tool in ['brush', 'eraser']:
                        current_stroke = {
                            "type": "stroke",
                            "mode": color_mode if tool == 'brush' else 'eraser',
                            "radius": radius,
                            "points": [event.pos]
                        }
                        drawings.append(current_stroke)

                    else:
                        shape_start = event.pos

                    drawing = True

            # Mouse movement
            if event.type == pygame.MOUSEMOTION and drawing:
                if current_stroke:
                    current_stroke["points"].append(event.pos)

            # Mouse released
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if drawing and shape_start:
                        drawings.append({
                            "type": tool,
                            "mode": color_mode,
                            "width": max(1, radius // 2),
                            "start": shape_start,
                            "end": event.pos
                        })
                    drawing = False
                    current_stroke = None
                    shape_start = None

        # Clear screen every frame
        screen.fill((0, 0, 0))

        # Draw all stored objects
        for d in drawings:
            if d["type"] == "stroke":
                draw_stroke(screen, d)
            else:
                draw_shape(screen, d)

        # Live preview for shapes
        if drawing and shape_start and tool in ['line', 'rectangle', 'circle']:
            mouse_pos = pygame.mouse.get_pos()
            temp_shape = {
                "type": tool,
                "mode": color_mode,
                "width": max(1, radius // 2),
                "start": shape_start,
                "end": mouse_pos
            }
            draw_shape(screen, temp_shape)

        draw_ui(screen, tool, color_mode, radius)

        pygame.display.flip()
        clock.tick(60)


# Draws UI panel
def draw_ui(screen, tool, color_mode, radius):
    font = pygame.font.SysFont("Verdana", 18)

    pygame.draw.rect(screen, (30, 30, 30), (10, 10, 330, 120))

    screen.blit(font.render(f"Tool: {tool}", True, (255, 255, 255)), (20, 20))
    screen.blit(font.render(f"Color: {color_mode}", True, (255, 255, 255)), (20, 45))
    screen.blit(font.render(f"Size: {radius}", True, (255, 255, 255)), (20, 70))

    hints = [
        "P brush  E eraser  O circle  T rectangle  L line",
        "F fill  X text  R/G/B color  1/2/3 size  Ctrl+S save"
    ]

    for i, h in enumerate(hints):
        screen.blit(font.render(h, True, (200, 200, 200)), (20, 95 + i * 18))


main()