# Import the "arcade" library
import arcade

arcade.open_window(800, 600, "Iowa Perspective")

# Set the background color
arcade.set_background_color(arcade.color.BLACK)

# Get ready to draw
arcade.start_render()

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

# Barn 1
arcade.draw_lrtb_rectangle_filled(0, 180, 380, 168.5, arcade.color.BARN_RED)

# Barn Door 1
arcade.draw_rectangle_filled(80, 190, 65, 45.5, arcade.color.BLACK_LEATHER_JACKET)

# Barn Window 1
arcade.draw_rectangle_filled(80, 280, 60, 30, arcade.color.ANTIQUE_WHITE)
arcade.draw_rectangle_filled(80, 280, 50, 15, arcade.color.BLACK)

# Barn 2
arcade.draw_lrtb_rectangle_filled(530, 720, 380, 168.5, arcade.color.BARN_RED)

# Barn Door 2
arcade.draw_rectangle_filled(630, 190, 65, 45.5, arcade.color.BLACK_LEATHER_JACKET)

# Barn Window 2
arcade.draw_rectangle_filled(630, 280, 60, 30, arcade.color.ANTIQUE_WHITE)
arcade.draw_rectangle_filled(630, 280, 50, 15, arcade.color.BLACK)

# Shed 1
arcade.draw_rectangle_filled(220, 215, 98, 94, arcade.color.BARN_RED)
arcade.draw_rectangle_filled(220, 190, 40, 45, arcade.color.BLACK_LEATHER_JACKET)

# Windows of Shed 1
arcade.draw_rectangle_filled(220, 220, 60, 20, arcade.color.ANTIQUE_WHITE)
arcade.draw_rectangle_filled(220, 220, 50, 10, arcade.color.BLACK)

# Shed 2
arcade.draw_rectangle_filled(760, 215, 98, 94, arcade.color.BARN_RED)
arcade.draw_rectangle_filled(760, 190, 40, 45, arcade.color.BLACK_LEATHER_JACKET)

# Windows of Shed 2
arcade.draw_rectangle_filled(760, 220, 60, 20, arcade.color.ANTIQUE_WHITE)
arcade.draw_rectangle_filled(760, 220, 50, 10, arcade.color.BLACK)

# River
arcade.draw_rectangle_filled(420, 0, 60, 400, arcade.color.BLUE)

# Dirt side of River left
arcade.draw_rectangle_filled(390, 0, 10, 400, arcade.color.DARK_BROWN)

# Dirt side of River right
arcade.draw_rectangle_filled(445, 0, 10, 400, arcade.color.DARK_BROWN)

# Cloud
arcade.draw_circle_filled(450, 500, 45, arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(380, 525, 56, arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(335, 515, 50, arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(290, 515, 30, arcade.color.LIGHT_GRAY)

# Stars
arcade.draw_circle_filled(730, 575, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(680, 575, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(500, 580, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(695, 580, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(685, 580, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(740, 580, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(500, 500, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(510, 500, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(450, 490, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(480, 700, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(380, 600, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(745, 500, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(687, 510, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(210, 520, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(510, 537, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(340, 550, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(200, 555, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(250, 550, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(683, 418, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(688, 450, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(699, 475, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(300, 280, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(400, 520, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(200, 530, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(500, 350, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(666, 500, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(400, 300, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(475, 375, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(490, 400, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(380, 380, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(375, 325, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(325, 400, 2, arcade.color.YELLOW)

# Moon
arcade.draw_circle_filled(785, 525, 85, arcade.color.GHOST_WHITE)

# Shed 2
arcade.draw_rectangle_filled(760, 215, 98, 94, arcade.color.BARN_RED)
arcade.draw_rectangle_filled(760, 190, 40, 45, arcade.color.BLACK_LEATHER_JACKET)

# Windows of Shed 2
arcade.draw_rectangle_filled(760, 220, 60, 20, arcade.color.ANTIQUE_WHITE)
arcade.draw_rectangle_filled(760, 220, 50, 10, arcade.color.BLACK)

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
