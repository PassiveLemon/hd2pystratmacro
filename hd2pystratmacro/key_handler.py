import importlib
import random
import time

from evdev import InputEvent, UInput, ecodes as e, categorize

from .config import key_press_dict, input_device
from .stratagem_dict import stratagem_dict

def gaussian(min: int, max: int, sig: int, mu: int) -> float:
  while True:
    value: float = random.gauss(mu, sig)
    if min <= value <= max:
      return value

def press_key(key_press: int) -> None:
  random_key_press_sleep: float = gaussian(36, 112, 28, 81)
  device = UInput.from_device(input_device)
  device.write(e.EV_KEY, key_press, 1)
  device.syn()
  time.sleep(random_key_press_sleep / 1000)
  device.write(e.EV_KEY, key_press, 0)
  device.syn()
  device.close()

def reload_config() -> None:
  config_module = importlib.import_module(".config", package=__package__)
  importlib.reload(config_module)
  print("Config reloaded")

ctrl_hold: bool = False
def handle_key_event(event: InputEvent) -> None:
  global ctrl_hold
  key_event: InputEvent = categorize(event)
  if event.type == e.EV_KEY:
    if key_event.keycode == "KEY_LEFTCTRL":
      if (key_event.keystate == key_event.key_down) or (key_event.keystate == key_event.key_hold):
        ctrl_hold = True
      else:
        ctrl_hold = False

    if ctrl_hold:
      if (key_event.keystate == key_event.key_down) or (key_event.keystate == key_event.key_hold):
        if key_event.keycode in key_press_dict:
          if key_press_dict[key_event.keycode] == "reload":
            reload_config()
          else:
            print(f"{key_event.keycode} - {key_press_dict[key_event.keycode]} - {stratagem_dict[key_press_dict[key_event.keycode]]}")
            for input in stratagem_dict[key_press_dict[key_event.keycode]]:
              press_key(input)
