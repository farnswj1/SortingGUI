# Imported libraries
import pyglet
import random
import time
from . import algorithms


# Window class
class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(caption="Sorting GUI", width=1000, height=800, *args, **kwargs)

        # Set the frame rate
        self.frame_rate = 1/30
        pyglet.clock.schedule_interval(self.update, self.frame_rate)

        # Main batch
        self.main_batch = pyglet.graphics.Batch()

        # Line that divides the buttons from the bars
        self.line = pyglet.shapes.Line(200, 0, 200, 1000, batch=self.main_batch)

        # List of sorting algortihms
        list_of_algorithms = (
            "Bitonic Sort",
            "Bogo Sort",
            "Bubble Sort",
            "Cocktail Sort",
            "Counting Sort",
            "Gnome Sort",
            "Heap Sort",
            "Insertion Sort",
            "Merge Sort",
            "Odd-Even Sort",
            "Pancake Sort",
            "Quick Sort",
            "Radix Sort",
            "Selection Sort",
            "Shell Sort",
            "Stooge Sort"
        )

        # Options (will act as buttons for the UI) 
        self.options = [
            pyglet.text.Label(
                sort_name,
                x=100,
                y=775 - y,
                anchor_x="center",
                anchor_y="center",
                batch=self.main_batch
            ) for sort_name, y in zip(
                list_of_algorithms, range(0, 800, 50)
            )
        ]

        # List of values in random order
        self.values = list(range(8, 801, 8))

        # List of sprites used to represent the values
        self.sprites = [
            pyglet.shapes.BorderedRectangle(x, 0, 8, value, batch=self.main_batch)
            for x, value in zip(range(200, 1000, 8), self.values)
        ]

        # Swap generator (initially null)
        self.next_swap = None

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
        if button == pyglet.window.mouse.LEFT and 0 <= x < 200:
            self.reset()  # First, reset the GUI

            if 750 <= y < 800:    # Bitonic sort
                pass  #self.next_swap = algorithms.bitonic_sort(self.values)
            elif 700 <= y < 750:  # Bogo sort
                pass  #self.next_swap = algorithms.bogo_sort(self.values)
            elif 650 <= y < 700:  # Bubble sort
                self.next_swap = algorithms.bubble_sort(self.values)
            elif 600 <= y < 650:  # Cocktail sort
                self.next_swap = algorithms.cocktail_sort(self.values)
            elif 550 <= y < 600:  # Counting sort
                pass  #self.next_swap = algorithms.counting_sort(self.values)
            elif 500 <= y < 550:  # Gnome sort
                self.next_swap = algorithms.gnome_sort(self.values)
            elif 450 <= y < 500:  # Heap sort
                self.next_swap = algorithms.heap_sort(self.values)
            elif 400 <= y < 450:  # Insertion sort
                self.next_swap = algorithms.insertion_sort(self.values)
            elif 350 <= y < 400:  # Merge sort
                self.next_swap = algorithms.merge_sort(self.values)
            elif 300 <= y < 350:  # Odd-even sort
                self.next_swap = algorithms.odd_even_sort(self.values)
            elif 250 <= y < 300:  # Pancake sort
                self.next_swap = algorithms.pancake_sort(self.values)
            elif 200 <= y < 250:  # Quick sort
                self.next_swap = algorithms.quick_sort(self.values)
            elif 150 <= y < 200:  # Radix sort
                pass  #self.next_swap = algorithms.radix_sort(self.values)
            elif 100 <= y < 150:  # Selection sort
                self.next_swap = algorithms.selection_sort(self.values)
            elif 50 <= y < 100:   # Shell sort
                self.next_swap = algorithms.shell_sort(self.values)
            elif 0 <= y < 50:     # Stooge sort
                self.next_swap = algorithms.stooge_sort(self.values)

    def on_draw(self):
        """Draws the contents onto the window"""
        self.clear()
        self.main_batch.draw()

    def run(self):
        """Runs the GUI"""
        pyglet.app.run()
