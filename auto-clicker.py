import time
import random
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Key

from pynput.mouse import Listener as MListener
from pynput.keyboard import Listener as KListener

maximum_time_on = 5
delay = 0.04
button = Button.left
start_stop_button = Button.x1
exit_button = Button.x2


class ClickMouse(threading.Thread):
	def __init__(self, delay, button):
		super().__init__()
		self.delay = delay
		self.button = button
		self.stopped_while_running = False
		self.running = False
		self.program_running = True
		self.last_activated = time.time()
		self.random_nums = []

	def start_clicking(self):
		print("Starting to click...")
		self.running = True
		self.last_activated = time.time()
		time.sleep(0.1)

	def stop_clicking(self):
		print("Halting clicking process...")
		self.running = False

	def exit(self):
		self.stop_clicking()
		self.program_running = False

	def refill_random(self):
		self.random_nums = [e/10000 for e in random.sample(range(1, 200), 100)]

	def get_random_num(self):
		if not len(self.random_nums) > 0:
			self.refill_random()
		return self.random_nums.pop()

	def run(self):
		print("Running")
		while self.program_running:
			while self.running:
				# print("Clicking...")
				mouse.click(self.button)
				time.sleep(self.delay + self.get_random_num())

				if time.time() - self.last_activated > maximum_time_on:
					self.running = False
			time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_click(x, y, b, pressed):
	# print("PRESSED", b, pressed)
	if b == start_stop_button and pressed:
		# print(pressed)
		if not click_thread.running:
			click_thread.start_clicking()
		else:
			click_thread.stop_clicking()
	elif b == exit_button:
		print("EXITING! Pressed", b)
		click_thread.exit()
		mouse_listener.stop()
		keyboard_listener.stop()
		exit()


last_state = False
enabled = False
def on_press(key):
	# print(key)
	# stop clicking if user presses shift
	global last_state, enabled
	key_down = key == Key.shift
	if key_down != last_state:
		last_state = key_down
		if last_state:
			if click_thread.running:
				click_thread.stop_clicking()
				click_thread.stopped_while_running = True


def on_release(key):
	if key == Key.shift:
		if click_thread.stopped_while_running:
			click_thread.start_clicking()
			click_thread.stopped_while_running = False


# Setup the listener threads
keyboard_listener = KListener(on_press=on_press, on_release=on_release)
mouse_listener = MListener(on_click=on_click)

# Start the threads and join them so the script doesn't end early
keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()