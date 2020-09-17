import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)


def draw_tractor(x, y):
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Draw the engine
    arcade.draw_rectangle_filled(x, 600, 120 + y, 140, arcade.color.GRAY)
    arcade.draw_rectangle_filled(x, 590, 105 + y, 90, arcade.color.BLACK)

    # Draw the smoke stack
    arcade.draw_rectangle_filled(x, 580, 175 + y, 10, arcade.color.BLACK)

    # Back wheel
    arcade.draw_circle_filled(x, 490, 110 + y, arcade.color.BLACK)
    arcade.draw_circle_filled(x, 490, 110 + y, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(x, 490, 110 + y, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(x, 490, 110 + y, arcade.color.RED)

    # Front wheel
    arcade.draw_circle_filled(x, 650, 90 + y, arcade.color.BLACK)
    arcade.draw_circle_filled(x, 650, 90 + y, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(x, 650, 90 + y, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(x, 650, 90 + y, arcade.color.RED)


def on_draw():
    """ Draw everything """
    arcade.start_render()
    draw_grass()
    draw_tractor(on_draw, 140)
    draw_tractor(450, 180)

    on_draw.tractor_x += 1

    on_draw.tractor_x = 150


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Iowa Perspective")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.start_render()

    draw_grass()
    draw_tractor(500, 350)

    # --- Draw the barn ---

    # Barn cement base
    arcade.draw_lrtb_rectangle_filled(30, 350, 210, 170, arcade.color.ASH_GREY)

    # Bottom half
    arcade.draw_lrtb_rectangle_filled(30, 350, 350, 210, arcade.color.BARN_RED)

    # Left-bottom window
    arcade.draw_rectangle_filled(70, 260, 30, 40, arcade.color.ANTIQUE_WHITE)
    arcade.draw_rectangle_filled(70, 260, 20, 30, arcade.color.BLACK)

    # Right-bottom window
    arcade.draw_rectangle_filled(310, 260, 30, 40, arcade.color.ANTIQUE_WHITE)
    arcade.draw_rectangle_filled(310, 260, 20, 30, arcade.color.BLACK)

    # Barn door
    arcade.draw_rectangle_filled(190, 230, 100, 100, arcade.color.BLACK_LEATHER_JACKET)

    # Rail above the door
    arcade.draw_rectangle_filled(190, 280, 180, 5, arcade.color.BLACK_BEAN)

    # Draw second level of barn
    arcade.draw_polygon_filled([[20, 350],
                                [100, 470],
                                [280, 470],
                                [360, 340]], arcade.color.BARN_RED)

    # Draw loft of barn
    arcade.draw_triangle_filled(100, 470, 280, 470, 190, 500, arcade.color.BARN_RED)

    # Left-top window
    arcade.draw_rectangle_filled(130, 440, 30, 40, arcade.color.ANTIQUE_WHITE)
    arcade.draw_rectangle_filled(130, 440, 20, 30, arcade.color.BLACK)

    # Right-top window
    arcade.draw_rectangle_filled(250, 440, 30, 40, arcade.color.ANTIQUE_WHITE)
    arcade.draw_rectangle_filled(250, 440, 20, 30, arcade.color.BLACK)

    # Draw 2nd level door
    arcade.draw_rectangle_outline(190, 310, 30, 60, arcade.color.ANTIQUE_WHITE, 5)

    # Draw the engine
    arcade.draw_rectangle_filled(600, 120, 140, 70, arcade.color.GRAY)
    arcade.draw_rectangle_filled(590, 105, 90, 40, arcade.color.BLACK)

    # Draw the smoke stack
    arcade.draw_rectangle_filled(580, 175, 10, 40, arcade.color.BLACK)

    # Back wheel
    arcade.draw_circle_filled(490, 110, 50, arcade.color.BLACK)
    arcade.draw_circle_filled(490, 110, 45, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(490, 110, 35, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(490, 110, 10, arcade.color.RED)

    # Front wheel
    arcade.draw_circle_filled(650, 90, 30, arcade.color.BLACK)
    arcade.draw_circle_filled(650, 90, 25, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(650, 90, 18, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(650, 90, 5, arcade.color.RED)

    # Cloud
    arcade.draw_circle_filled(450, 500, 45, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(380, 525, 56, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(335, 515, 50, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(290, 515, 30, arcade.color.LIGHT_GRAY)

    # Stars
    arcade.draw_circle_filled(720, 575, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(710, 575, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(680, 575, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(500, 580, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(645, 580, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(685, 580, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(750, 580, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(700, 580, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(500, 500, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(550, 500, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(450, 490, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(480, 700, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(380, 600, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(550, 510, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(630, 500, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(580, 490, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(210, 520, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(660, 537, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(340, 550, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(200, 555, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(250, 550, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(660, 275, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(678, 350, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(699, 275, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(300, 280, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(400, 275, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(200, 275, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(500, 250, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(550, 300, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(400, 300, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(475, 375, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(490, 400, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(380, 380, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(375, 325, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(325, 400, 2, arcade.color.YELLOW)
    arcade.draw_circle_filled(730, 540, 2, arcade.color.YELLOW)

    # Moon
    arcade.draw_circle_filled(785, 525, 85, arcade.color.GHOST_WHITE)

    # Shed
    arcade.draw_rectangle_filled(760, 215, 98, 94, arcade.color.BARN_RED)
    arcade.draw_rectangle_filled(760, 190, 40, 45, arcade.color.BLACK_LEATHER_JACKET)

    "# Windows of Shed"
    arcade.draw_rectangle_filled(760, 220, 60, 20, arcade.color.ANTIQUE_WHITE)
    arcade.draw_rectangle_filled(760, 220, 50, 10, arcade.color.BLACK)

    arcade.finish_render()
    arcade.run()


main()
