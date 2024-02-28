import os
import random
import threading
import time
from typing import Dict, List, Type

from evdev import categorize, ecodes as e, InputDevice, UInput

stratagem_dict: Dict[str, List[int]] = {
  # WIP
  # General
  "reinforce": [e.KEY_W, e.KEY_S, e.KEY_D, e.KEY_A, e.KEY_W],
  "resupply": [e.KEY_S, e.KEY_S, e.KEY_W, e.KEY_D],
  "sos": [e.KEY_W, e.KEY_S, e.KEY_D, e.KEY_W],
  "hellbomb": [e.KEY_S, e.KEY_W, e.KEY_A, e.KEY_S, e.KEY_W, e.KEY_D, e.KEY_S, e.KEY_W],
  "flare": [e.KEY_D, e.KEY_D, e.KEY_A, e.KEY_A],
  "flag": [e.KEY_S, e.KEY_W, e.KEY_S, e.KEY_W],
  "seaf": [e.KEY_D, e.KEY_W, e.KEY_W, e.KEY_S],
  # PAC
  "autocannon": [e.KEY_S, e.KEY_A, e.KEY_S, e.KEY_W, e.KEY_W, e.KEY_D],
  # Orbital
  "laser": [e.KEY_D, e.KEY_S, e.KEY_W, e.KEY_D, e.KEY_S],
  # Hangar
  "rearm": [e.KEY_W, e.KEY_W, e.KEY_A, e.KEY_W, e.KEY_D],
  "airstrike": [e.KEY_W, e.KEY_D, e.KEY_S, e.KEY_D],
  "cluster": [e.KEY_W, e.KEY_D, e.KEY_S, e.KEY_S, e.KEY_D],
  "500kg": [e.KEY_W, e.KEY_D, e.KEY_S, e.KEY_S, e.KEY_S],
  # Bridge
  "precision": [e.KEY_D, e.KEY_D, e.KEY_W],
  # Engineering
  "grenade_launcher": [e.KEY_S, e.KEY_A, e.KEY_W, e.KEY_A, e.KEY_S],
  "shield_generator": [e.KEY_S, e.KEY_W, e.KEY_A, e.KEY_D, e.KEY_A, e.KEY_D],
  # Robotics
  "mortar_sentry": [e.KEY_S, e.KEY_W, e.KEY_D, e.KEY_D, e.KEY_S],
  "autocannon_sentry": [e.KEY_S, e.KEY_W, e.KEY_D, e.KEY_W, e.KEY_A, e.KEY_W],
  "": [],
}

key_press_dict: Dict[str, str] = {
  "KEY_F1": "reinforce",
  "KEY_F2": "precision",
  "KEY_F3": "laser",
  "KEY_F4": "autocannon",
  "KEY_F5": "autocannon_sentry",
  "KEY_F0": "resupply",
}

dev: Type[InputDevice] = InputDevice("/dev/input/event0")

def key_press(key_press: int) -> None:
  def gaussian(min: int, max: int, sig: int, mu: int) -> float:
    while True:
      value: float = random.gauss(mu, sig)
      if min <= value <= max:
        return value
  random_key_press_sleep: int = gaussian(54, 112, 21, 81)
  ui: Type[UInput] = UInput.from_device(dev)
  ui.write(e.EV_KEY, key_press, 1)
  ui.syn()
  time.sleep(random_key_press_sleep / 1000)
  ui.write(e.EV_KEY, key_press, 0)
  ui.syn()
  ui.close()

def main() -> None:
  ctrl_hold: bool = False
  try:
    while True:
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
                print(f"{key_event.keycode} - {key_press_dict[key_event.keycode]} - {stratagem_dict[key_press_dict[key_event.keycode]]}")
                for input in stratagem_dict[key_press_dict[key_event.keycode]]:
                  key_press(input)
  except:
    exit()

if __name__ == "__main__":
  main()
