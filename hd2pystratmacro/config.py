import argparse
import os
from typing import Dict, List

from evdev import ecodes as e
import yaml

user: str = os.getenv("SUDO_USER")
user_config_dir: str = os.getenv("XDG_CONFIG_HOME", f"/home/{user}/.config/hd2pystratmacro")
user_config_file: str = os.path.join(user_config_dir, "config.yaml")
source_install_path: str = os.path.dirname(os.path.realpath(__file__))
source_config_file: str = os.path.join(source_install_path, "config.yaml")

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", default=user_config_file, help="Location of configuration file.")
arguments = parser.parse_args()

try:
  yaml.safe_load(open(arguments.file))
except FileNotFoundError:
  if arguments.file is user_config_file:
    print(f"Configuration file does not exist at XDG_CONFIG: {user_config_file}, generating...")
    os.makedirs(user_config_dir)
    with open(user_config_file, 'w') as user, open (source_config_file, "r") as source:
      for line in source:
        user.write(line)
  else:
    raise Exception(f"Configuration file does not exist: {arguments.file}")
except IsADirectoryError:
  raise Exception(f"Configuration file is a directory: {arguments.file}")
except PermissionError:
  raise Exception(f"You do not have the necessary permissions to access configuration file: {arguments.file}")
except:
  raise Exception(f"Configuration file is not valid YAML: {arguments.file}")

# This program requires access to keyboard devices (which requires sudo) so we raise
if os.geteuid() != 0:
  raise Exception("This program requires sudo.")

print(f"Configuration file: {arguments.file}")

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
  "railgun": [e.KEY_S, e.KEY_D, e.KEY_S, e.KEY_W, e.KEY_A, e.KEY_D],
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
  "ems_sentry": [e.KEY_S, e.KEY_S, e.KEY_W, e.KEY_W, e.KEY_A],
  "": [],
}

key_press_dict: Dict[str, str] = { }

yaml_config: Dict = yaml.safe_load(open(arguments.file))
for stratagem, stratagem_key in yaml_config["main"].items():
  key_press_dict[stratagem_key] = stratagem
  print(f"{stratagem_key} - {stratagem}")
