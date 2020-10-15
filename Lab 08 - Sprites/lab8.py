import random
import arcade

# --- Constants ---
SPRITE_SCALING_ZOMBIES = 0.3
SPRITE_SCALING_HUMANS = .25
SPRITE_SCALING_BULLETS = .25
HUMANS_COUNT = 40
BULLETS_COUNT = 40

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lab_8"

#Coin=Humans
#Wheel= Bullets
#Player = Zombies
class Human(arcade.Sprite):

    def reset_pos(self):
        # Reset the humans to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the Humans
        self.center_y -= 1

        # See if the humans has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            # Reset the humans to a random spot above the screen
            self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)


class Bullets(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the humans
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.zombies_list = None
        self.humans_list = None
        self.bullets_list = None

        # Set up the player info
        self.zombies_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.YELLOW)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.zombies_list = arcade.SpriteList()
        self.humans_list = arcade.SpriteList()
        self.bullets_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the zombies
        # Character image from kenney.nl
        self.zombies_sprite = arcade.Sprite("character_zombie_attackKick.png", SPRITE_SCALING_ZOMBIES )
        self.zombies_sprite.center_x = 50
        self.zombies_sprite.center_y = 50
        self.zombies_list.append(self.zombies_sprite)

        # Create the humans
        for i in range(HUMANS_COUNT):

            # Create the humans instance
            # Humans image from kenney.nl
            humans = Humans(":resources:images/items/character_malePerson_run1.png", SPRITE_SCALING_HUMANS)

            # Position the humans
            humans.center_x = random.randrange(SCREEN_WIDTH)
            humans.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.humans_list.append(coin)

        # Create the bullets
        for i in range(BULLETS_COUNT):

            # Create the bullet instance
            # Bullets image from kenney.nl
            wheel = Wheel("ammo_machinegun.png", SPRITE_SCALING_BULLETS)

            # Position the bullets
            wheel.center_x = random.randrange(SCREEN_WIDTH)
            wheel.center_y = random.randrange(SCREEN_HEIGHT)
            wheel.change_x = random.randrange(-3, 4)
            wheel.change_y = random.randrange(-3, 4)

            # Add the bullets to the lists
            self.wheel_list.append(bullets)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.humans_list.draw()
        self.bullets_list.draw()
        self.zombies_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 14)

        if len(self.coin_list) == 0:
            arcade.draw_text("WASTED!", 100, 200, arcade.color.BLACK, 100)

    def on_mouse_motion(self, x, y, dx, dy):

        if len(self.humans_list) > 0:
            self.zombies_sprite.center_x = x
            self.zombies_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.humans_list.update()

        if len(self.humans_list) > 0:
            self.bullets_list.update()

        # Generate a list of all sprites that collided with the zombies
        hit_list = arcade.check_for_collision_with_list(self.zombies_sprite, self.humans_list)
        hit_list = arcade.check_for_collision_with_list(self.zombies_sprite, self.bullets_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        hit_list = arcade.check_for_collision_with_list(self.zombies_sprite, self.humans_list)
        for humans in hit_list:
            humans.remove_from_sprite_lists()
            self.score += 1

        hit_list = arcade.check_for_collision_with_list(self.zombies_sprite, self.bullets_list)
        for bullets in hit_list:
            bullets.remove_from_sprite_lists()
            self.score -= 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()