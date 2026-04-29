import pygame

# Flood fill: fills a closed area and returns list of pixels
def flood_fill(screen, x, y, new_color):
    target_color = screen.get_at((x, y))

    # If same color → nothing to fill
    if target_color == new_color:
        return []

    filled_pixels = []
    stack = [(x, y)]  # DFS stack

    while stack:
        px, py = stack.pop()

        if screen.get_at((px, py)) == target_color:
            screen.set_at((px, py), new_color)
            filled_pixels.append((px, py))

            # Add neighbors
            if px > 0: stack.append((px - 1, py))
            if px < 799: stack.append((px + 1, py))
            if py > 0: stack.append((px, py - 1))
            if py < 559: stack.append((px, py + 1))

    return filled_pixels


# Returns RGB color based on mode
def get_base_color(color_mode):
    if color_mode == 'blue':
        return (0, 0, 255)
    elif color_mode == 'red':
        return (255, 0, 0)
    elif color_mode == 'green':
        return (0, 255, 0)
    elif color_mode == 'eraser':
        return (0, 0, 0)
    return (255, 255, 255)


# Draw freehand strokes (pencil / eraser)
def draw_stroke(screen, stroke):
    points = stroke["points"]
    color = get_base_color(stroke["mode"])

    for i in range(len(points) - 1):
        pygame.draw.line(screen, color, points[i], points[i + 1], stroke["radius"])


# Draw shapes and text
def draw_shape(screen, shape):

    # TEXT (separate because uses "color" field instead of "mode")
    if shape["type"] == "text":
        font = pygame.font.SysFont("Verdana", 20)
        text_surface = font.render(shape["text"], True,
                                   get_base_color(shape["color"]))
        screen.blit(text_surface, shape["pos"])
        return

    # Other shapes use "mode"
    color = get_base_color(shape["mode"])

    # Rectangle
    if shape["type"] == "rectangle":
        rect = pygame.Rect(min(shape["start"][0], shape["end"][0]),
                           min(shape["start"][1], shape["end"][1]),
                           abs(shape["start"][0] - shape["end"][0]),
                           abs(shape["start"][1] - shape["end"][1]))
        pygame.draw.rect(screen, color, rect, shape["width"])

    # Circle
    elif shape["type"] == "circle":
        center = ((shape["start"][0] + shape["end"][0]) // 2,
                  (shape["start"][1] + shape["end"][1]) // 2)
        radius = max(abs(shape["start"][0] - shape["end"][0]),
                     abs(shape["start"][1] - shape["end"][1])) // 2
        pygame.draw.circle(screen, color, center, radius, shape["width"])

    # Line
    elif shape["type"] == "line":
        pygame.draw.line(screen, color,
                         shape["start"], shape["end"], shape["width"])