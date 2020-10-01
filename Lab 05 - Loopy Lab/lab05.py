import arcade

column_space = 10
row_space = 10
left_border = 5
bottom_border = 5


arcade.open_window("Lab_05", 1200, 600)

arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

arcade.start_render()


def draw_section_outlines():

    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = (column * 10) + 5
            y = (row * 10) + 5
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    for row in range(30):
        for column in range(30):
            x = (column * 10 + 5) + 300
        y = (row * 10 + 5)
        if column % 2 == 1:
            print(arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK))
        else:
            print(arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE))


def draw_section_3():
    for row in range(30):
        for column in range(30):
            x = (column * 10 + 5) + 600
        y = (row * 10 + 5)
        if row % 2 == 1:
            print(arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK))
        else:
            print(arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE))


def draw_section_4():
    for row in range(30):
        for column in range(30):
            x = (column * 10 + 5) + 900
        y = (row * 10 + 5)
        if row % 2 == 1 and column % 2 == 1:
            print(arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK))


def draw_section_5():
    for row in range(30):
        for column in range(row, 30):
            x = (column * 10 + 5)
            y = (row * 10 + 5) + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_6():
    for row in range(30):
        for column in range(30 - row):
            x = (column * 10 + 5) + 300
            y = (row * 10 + 5) + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_7():
    for row in range(30):
        for column in range(30 - (row - 1)):
            x = (column * 10 + 5) + 600
            y = 300 - (row * 10 + 5) + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_8():
    for row in range(30):
        for column in range(row + 2):
            x = (column * 10 + 5) + 900
            y = 300 - (row * 10 + 5) + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()