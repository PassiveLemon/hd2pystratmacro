import argparse
import os

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
    os.makedirs(user_config_dir, exist_ok=True)
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

stratagem_dict: dict[str, list[int]] = {
  # General
  "reinforce": [e.KEY_W, e.KEY_S, e.KEY_D, e.KEY_A, e.KEY_W],
  "resupply": [e.KEY_S, e.KEY_S, e.KEY_W, e.KEY_D],
  "sos": [e.KEY_W, e.KEY_S, e.KEY_D, e.KEY_W],
  "hellbomb": [e.KEY_S, e.KEY_W, e.KEY_A, e.KEY_S, e.KEY_W, e.KEY_D, e.KEY_S, e.KEY_W],
  "flare": [e.KEY_D, e.KEY_D, e.KEY_A, e.KEY_A],
  "flag": [e.KEY_S, e.KEY_W, e.KEY_S, e.KEY_W],
  "seaf": [e.KEY_D, e.KEY_W, e.KEY_W, e.KEY_S],
  # Patriotic Administration Center
  "machine": [],
  "antimaterial": [],
  "stalwart": [],
  "expendable": [],
  "recoilless": [],
  "flamethrower": [],
  "autocannon": [e.KEY_S, e.KEY_A, e.KEY_S, e.KEY_W, e.KEY_W, e.KEY_D],
  "railgun": [e.KEY_S, e.KEY_D, e.KEY_S, e.KEY_W, e.KEY_A, e.KEY_D],
  "spear": [],
  # Orbital Cannons
  "orbital_gatling": [],
  "orbital_airburst": [],
  "orbital_120mm": [],
  "orbital_380mm": [],
  "orbital_walking": [],
  "orbital_laser": [e.KEY_D, e.KEY_S, e.KEY_W, e.KEY_D, e.KEY_S],
  "orbital_railcannon": [],
  # Hangar
  "eagle_rearm": [e.KEY_W, e.KEY_W, e.KEY_A, e.KEY_W, e.KEY_D],
  "eagle_strafing": [],
  "eagle_airstrike": [e.KEY_W, e.KEY_D, e.KEY_S, e.KEY_D],
  "eagle_cluster": [e.KEY_W, e.KEY_D, e.KEY_S, e.KEY_S, e.KEY_D],
  "eagle_napalm": [],
  "jump_pack": [],
  "eagle_smoke": [],
  "eagle_110mm": [],
  "eagle_500kg": [e.KEY_W, e.KEY_D, e.KEY_S, e.KEY_S, e.KEY_S],
  # Bridge
  "orbital_precision": [e.KEY_D, e.KEY_D, e.KEY_W],
  "orbital_gas": [],
  "orbital_ems": [],
  "orbital_smoke": [],
  "hmg_replacement": [],
  "shield_relay": [],
  "tesla_tower": [],
  # Engineering Bay
  "minefield": [],
  "supply_pack": [],
  "grenade_launcher": [e.KEY_S, e.KEY_A, e.KEY_W, e.KEY_A, e.KEY_S],
  "laser_cannon": [],
  "incendiary_mines": [],
  "guard_dog_rover": [],
  "ballistic_shield": [],
  "arc_thrower": [],
  "shield_generator": [e.KEY_S, e.KEY_W, e.KEY_A, e.KEY_D, e.KEY_A, e.KEY_D],
  # Robotics Workshop
  "machine_sentry": [],
  "gatling_sentry": [],
  "mortar_sentry": [e.KEY_S, e.KEY_W, e.KEY_D, e.KEY_D, e.KEY_S],
  "guard_dog": [],
  "autocannon_sentry": [e.KEY_S, e.KEY_W, e.KEY_D, e.KEY_W, e.KEY_A, e.KEY_W],
  "rocket_sentry": [],
  "ems_sentry": [e.KEY_S, e.KEY_S, e.KEY_W, e.KEY_W, e.KEY_A],
}

key_press_dict: dict[str, str] = { }

yaml_config: dict = yaml.safe_load(open(arguments.file))
for stratagem, stratagem_key in yaml_config["main"].items():
  key_press_dict[stratagem_key] = stratagem
  print(f"{stratagem_key} - {stratagem}")
