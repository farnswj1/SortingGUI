# Imported libraries
import pyglet
import random
import time


# Sorting GUI class
class SortingGUI(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(caption="Sorting GUI", width=800, height=800, *args, **kwargs)

        # Set the frame rate
        self.frame_rate = 1/30
        pyglet.clock.schedule_interval(self.update, self.frame_rate)

        # Main batch
        self.main_batch = pyglet.graphics.Batch()

        # List of values in random order
        self.values = random.sample(list(range(10, 810, 10)), k=80)

        # List of sprites used to represent the values
        self.sprites = [
            pyglet.shapes.BorderedRectangle(x, 0, 10, value, batch=self.main_batch)
            for x, value in zip(range(0, 800, 10), self.values)
        ]

        # Swap generator (initially null)
        self.next_swap = None

    def bubble_sort(self):
        """Bubble sort generator that yields the next indices to be swapped"""
        # Start sorting using bubble sort technique
        for i in range(len(self.values) - 1):

            # After this iteration max element will come at last
            for j in range(len(self.values) - i - 1):

                # Starting element is greater than the next element
                if self.values[j] > self.values[j + 1]:
                    yield j, j + 1

    def selection_sort(self):
        """Selection sort generator that yields the next indices to be swapped"""
        for i in range(len(self.values)):
            min_idx = i

            # Find the minimum element in the remaining unsorted list
            for j in range(i + 1, len(self.values)):
                if self.values[j] < self.values[min_idx]:
                    min_idx = j

            # Swap the minimum element with the first element
            yield i, min_idx

    def insertion_sort(self):
        """Insertion sort generator that yields the next indices to be swapped"""
        # Traverse through 1 upwards
        for i in range(1, len(self.values)):
            key = self.values[i]
            j = i - 1

            # Push the element down until it's not less than the next element
            while j >= 0 and key < self.values[j]:
                yield j, j + 1
                j -= 1

    def update(self, dt):
        """Updates the GUI"""

        # If a generator function is provided, get the next pair of indices to swap if they exist
        if self.next_swap:
            try:
                i, j = next(self.next_swap)
                self.swap(i, j)
            except StopIteration as e:
                self.next_swap = None

    def swap(self, i, j):
        """Swaps the values and their respective sprites based on the indices given"""
        self.values[i], self.values[j] = self.values[j], self.values[i]
        self.sprites[i].height, self.sprites[j].height = self.sprites[j].height, self.sprites[i].height

    def reset(self):
        """Reset the GUI"""
        random.shuffle(self.values)

        # Update the sprites' heights with the randomized values
        for sprite, value in zip(self.sprites, self.values):
            sprite.height = value

        # Remove the generator function
        self.next_swap = None

    # Handle the events when the mouse is pressed
    def on_mouse_press(self, x, y, button, modifiers):
        # Handle the left click
        if button == pyglet.window.mouse.LEFT:
            self.reset()
            self.next_swap = self.bubble_sort()
        elif button == pyglet.window.mouse.RIGHT:
            self.reset()
            self.next_swap = self.selection_sort()

    def on_draw(self):
        """Draws the contents onto the window"""
        self.clear()
        self.main_batch.draw()

    def run(self):
        """Runs the GUI"""
        self.next_swap = self.insertion_sort()
        pyglet.app.run()


# Executes the program
if __name__ == "__main__":
    SortingGUI().run()
