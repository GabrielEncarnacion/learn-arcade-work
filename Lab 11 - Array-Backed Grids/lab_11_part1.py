"""
Array Backed Grid version 2
Show how to use a two-dimensional list/array to back the display of a
grid on-screen.
"""
import arcade

# Set how many rows and columns we will have
ROW_COUNT = 10
COLUMN_COUNT = 10

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        """
        Set up the application.
        """
        super().__init__(width, height)

        # Create a 2 dimensional array. A two dimensional
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        arcade.set_background_color(arcade.color.BLACK)

        """ Create a list to hold buffered shapes, and load the list """
        self.grid_shape_list = None
        self.create_shapes_from_grid()

    def create_shapes_from_grid(self):
        """ This creates a list of buffered shapes, and loads the
        rectangles into that list for faster display. """
        self.grid_shape_list = arcade.ShapeElementList()

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):

                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                rectangle = arcade.create_rectangle_filled(x, y, WIDTH, HEIGHT, color)
                self.grid_shape_list.append(rectangle)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        arcade.start_render()

        self.grid_shape_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        # Change the x/y screen coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:

            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0

            if row > 0 and self.grid[row-1][column] == 0:
                self.grid[row-1][column] = 1
            elif row > 0 and self.grid[row-1][column] == 1:
                self.grid[row-1][column] = 0

            if self.grid[row + 1][column] == 1:
                self.grid[row + 1][column] = 0
            else:
                self.grid[row + 1][column] = 1

            if self.grid[row][column - 1] == 1:
                self.grid[row][column - 1] = 0
            else:
                self.grid[row][column - 1] = 1

            if column < COLUMN_COUNT - 1 and self.grid[row][column + 1] == 0:
                self.grid[row][column + 1] = 1
            elif column < COLUMN_COUNT - 1 and self.grid[row][column + 1] == 1:
                self.grid[row][column + 1] = 0

                if self.grid[row - 1][column] == 1:
                    self.grid[row - 1][column] = 0
                else:
                    self.grid[row - 1][column] = 1

                if self.grid[row][column + 1] == 1:
                    self.grid[row][column + 1] = 0
                else:
                    self.grid[row][column + 1] = 1

        self.create_shapes_from_grid()


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()