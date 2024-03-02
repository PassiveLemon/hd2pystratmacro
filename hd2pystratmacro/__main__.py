import importlib
import os
import random
import threading
import time

from evdev import categorize, ecodes as e, InputDevice, UInput
import yaml

from .config import arguments, stratagem_dict, key_press_dict

dev = InputDevice("/dev/input/event0")

def key_press(key_press: int) -> None:
  def gaussian(min: int, max: int, sig: int, mu: int) -> float:
    while True:
      value: float = random.gauss(mu, sig)
      if min <= value <= max:
        return value
  random_key_press_sleep: int = gaussian(36, 112, 28, 81)
  ui = UInput.from_device(dev)
  ui.write(e.EV_KEY, key_press, 1)
  ui.syn()
  time.sleep(random_key_press_sleep / 1000)
  ui.write(e.EV_KEY, key_press, 0)
  ui.syn()
  ui.close()

def main() -> None:
  ctrl_hold: bool = False
  try:
    for event in dev.read_loop():
      if event.type == e.EV_KEY:
        key_event: str = categorize(event)
        if key_event.keycode == "KEY_LEFTCTRL":
          if (key_event.keystate == key_event.key_down) or (key_event.keystate == key_event.key_hold):
            ctrl_hold = True
          else:
            ctrl_hold = False
        if ctrl_hold:
          if (key_event.keystate == key_event.key_down) or (key_event.keystate == key_event.key_hold):
            if key_event.keycode in key_press_dict:
              if key_press_dict[key_event.keycode] == "reload":
                config_module = importlib.import_module(".config", package=__package__)
                importlib.reload(config_module)
                print("Config reloaded")
              else:
                print(f"{key_event.keycode} - {key_press_dict[key_event.keycode]} - {stratagem_dict[key_press_dict[key_event.keycode]]}")
                for input in stratagem_dict[key_press_dict[key_event.keycode]]:
                  key_press(input)
  except:
    exit()

if __name__ == "__main__":
  main()
