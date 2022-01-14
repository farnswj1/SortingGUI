# Imported libraries
import pyglet
import random
from . import algorithms


# Window class
class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(caption="Sorting GUI", width=600, height=512, *args, **kwargs)

        # Get the system mouse cursors and set to the default cursor
        self.cursor_default = self.get_system_mouse_cursor(self.CURSOR_DEFAULT)
        self.cursor_hand = self.get_system_mouse_cursor(self.CURSOR_HAND)
        self.cursor = self.cursor_default
        self.set_mouse_cursor(self.cursor)

        # Set the frame rate
        self.frame_rate = 1/50
        pyglet.clock.schedule_interval(self.update, self.frame_rate)

        # Main batch
        self.main_batch = pyglet.graphics.Batch()

        # Line that divides the buttons from the bars
        self.line = pyglet.shapes.Line(88, 0, 88, 1024, batch=self.main_batch)

        # List of sorting algorithms
        list_of_algorithms = (
            "Bitonic",
            "Bogo",
            "Bubble",
            "Cocktail",
            "Comb",
            "Cycle",
            "Heap",
            "Insertion",
            "Merge",
            "Odd-Even",
            "Pancake",
            "Quick",
            "Radix",
            "Selection",
            "Shell",
            "Stooge"
        )

        # Options (will act as buttons for the UI) 
        self.options = [
            pyglet.text.Label(
                sort_name,
                x=44,
                y=496 - y,
                anchor_x="center",
                anchor_y="center",
                batch=self.main_batch
            ) for sort_name, y in zip(
                list_of_algorithms, range(0, 512, 32)
            )
        ]

        # List of values
        self.values = list(range(4, 513, 4))

        # List of bars used to represent the values
        self.bars = [
            pyglet.shapes.BorderedRectangle(x, 0, 4, value, batch=self.main_batch)
            for x, value in zip(range(88, 600, 4), self.values)
        ]

        # Swap generator (initially null)
        self.next_swap = None

    def update(self, dt):
        """Updates the GUI"""
        # If a generator function is provided, get the next pair of indices to swap if they exist
        if self.next_swap:
            try:
                next(self.next_swap)
                self.update_bars()
            except StopIteration as e:
                self.next_swap = None

    def update_bars(self):
        """Update the bars' heights"""
        for bar, value in zip(self.bars, self.values):
            bar.height = value

    def reset(self):
        """Reset the GUI"""
        # Reset the list of values (to avoid potential data loss if switching mid-sort)
        self.values = random.sample(list(range(4, 513, 4)), k=len(self.values))

        # Update the bars' heights with the randomized values
        self.update_bars()

        # Remove the generator function
        self.next_swap = None

    def on_mouse_motion(self, x, y, dx, dy):
        """Handle the events when the mouse is moved"""
        # Set the cursor to the hand if it's over the buttons. Otherwise, set to default
        if x <= 88 and self.cursor != self.cursor_hand:
            self.cursor = self.cursor_hand
            self.set_mouse_cursor(self.cursor)
        elif 88 < x and self.cursor != self.cursor_default:
            self.cursor = self.cursor_default
            self.set_mouse_cursor(self.cursor)

    def on_mouse_press(self, x, y, button, modifiers):
        """Handle the events when the mouse is pressed"""
        # Handle the left click
        if button == pyglet.window.mouse.LEFT and x < 88:
            self.reset()  # First, reset the GUI

            if 480 <= y < 512:    # Bitonic sort
                self.next_swap = algorithms.bitonic_sort(self.values)
            elif 448 <= y < 480:  # Bogo sort
                self.next_swap = algorithms.bogo_sort(self.values)
            elif 416 <= y < 448:  # Bubble sort
                self.next_swap = algorithms.bubble_sort(self.values)
            elif 384 <= y < 416:  # Cocktail sort
                self.next_swap = algorithms.cocktail_sort(self.values)
            elif 352 <= y < 384:  # Comb sort
                self.next_swap = algorithms.comb_sort(self.values)
            elif 320 <= y < 352:  # Cycle sort
                self.next_swap = algorithms.cycle_sort(self.values)
            elif 288 <= y < 320:  # Heap sort
                self.next_swap = algorithms.heap_sort(self.values)
            elif 256 <= y < 288:  # Insertion sort
                self.next_swap = algorithms.insertion_sort(self.values)
            elif 224 <= y < 256:  # Merge sort
                self.next_swap = algorithms.merge_sort(self.values)
            elif 192 <= y < 224:  # Odd-even sort
                self.next_swap = algorithms.odd_even_sort(self.values)
            elif 160 <= y < 192:  # Pancake sort
                self.next_swap = algorithms.pancake_sort(self.values)
            elif 128 <= y < 160:  # Quick sort
                self.next_swap = algorithms.quick_sort(self.values)
            elif 96 <= y < 128:   # Radix sort
                self.next_swap = algorithms.radix_sort(self.values)
            elif 64 <= y < 96:    # Selection sort
                self.next_swap = algorithms.selection_sort(self.values)
            elif 32 <= y < 64:    # Shell sort
                self.next_swap = algorithms.shell_sort(self.values)
            elif 0 <= y < 32:     # Stooge sort
                self.next_swap = algorithms.stooge_sort(self.values)

    def on_draw(self):
        """Draws the contents onto the window"""
        self.clear()
        self.main_batch.draw()

    @staticmethod
    def run():
        """Runs the GUI"""
        pyglet.app.run()
