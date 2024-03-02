import argparse
import os
import pwd

from evdev import ecodes as e
import yaml

user: str = os.getlogin()
user_uid: int = pwd.getpwnam(user).pw_uid
user_gid: int = pwd.getpwnam(user).pw_gid
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
    os.chown(user_config_dir, user_uid, user_gid)
    with open(user_config_file, 'w') as user, open (source_config_file, "r") as source:
      for line in source:
        user.write(line)
      os.chown(user_config_file, user_uid, user_gid)
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
  "machine": [e.KEY_S, e.KEY_A, e.KEY_S, e.KEY_W, e.KEY_D],
  "antimaterial": [e.KEY_S, e.KEY_A, e.KEY_D, e.KEY_W, e.KEY_S],
  "stalwart": [e.KEY_S, e.KEY_A, e.KEY_S, e.KEY_W, e.KEY_W, e.KEY_A],
  "expendable": [e.KEY_S, e.KEY_S, e.KEY_A, e.KEY_W, e.KEY_D],
  "recoilless": [e.KEY_S, e.KEY_A, e.KEY_D, e.KEY_D, e.KEY_A],
  "flamethrower": [e.KEY_S, e.KEY_A, e.KEY_W, e.KEY_S, e.KEY_W],
  "autocannon": [e.KEY_S, e.KEY_A, e.KEY_S, e.KEY_W, e.KEY_W, e.KEY_D],
  "railgun": [e.KEY_S, e.KEY_D, e.KEY_S, e.KEY_W, e.KEY_A, e.KEY_D],
  "spear": [e.KEY_S, e.KEY_S, e.KEY_W, e.KEY_S, e.KEY_S],
  # Orbital Cannons
  "orbital_gatling": [e.KEY_D, e.KEY_S, e.KEY_A, e.KEY_W, e.KEY_W],
  "orbital_airburst": [e.KEY_D, e.KEY_D, e.KEY_D],
  "orbital_120mm": [e.KEY_D, e.KEY_D, e.KEY_S, e.KEY_A, e.KEY_D, e.KEY_S],
  "orbital_380mm": [e.KEY_D, e.KEY_S, e.KEY_W, e.KEY_W, e.KEY_A,e.KEY_S, e.KEY_S],
  "orbital_walking": [e.KEY_D, e.KEY_D, e.KEY_S, e.KEY_A, e.KEY_D, e.KEY_S],
  "orbital_laser": [e.KEY_D, e.KEY_S, e.KEY_W, e.KEY_D, e.KEY_S],
  "orbital_railcannon": [e.KEY_D, e.KEY_W, e.KEY_S, e.KEY_S, e.KEY_D],
  # Hangar
  "eagle_rearm": [e.KEY_W, e.KEY_W, e.KEY_A, e.KEY_W, e.KEY_D],
  "eagle_strafing": [e.KEY_W, e.KEY_D, e.KEY_D],
  "eagle_airstrike": [e.KEY_W, e.KEY_D, e.KEY_S, e.KEY_D],
  "eagle_cluster": [e.KEY_W, e.KEY_D, e.KEY_S, e.KEY_S, e.KEY_D],
  "eagle_napalm": [e.KEY_W, e.KEY_D, e.KEY_S, e.KEY_W],
  "jump_pack": [e.KEY_S, e.KEY_W, e.KEY_W, e.KEY_S, e.KEY_W],
  "eagle_smoke": [e.KEY_W, e.KEY_D, e.KEY_W, e.KEY_S],
  "eagle_110mm": [e.KEY_W, e.KEY_D, e.KEY_W, e.KEY_A],
  "eagle_500kg": [e.KEY_W, e.KEY_D, e.KEY_S, e.KEY_S, e.KEY_S],
  # Bridge
  "orbital_precision": [e.KEY_D, e.KEY_D, e.KEY_W],
  "orbital_gas": [e.KEY_D, e.KEY_D, e.KEY_S, e.KEY_D],
  "orbital_ems": [e.KEY_D, e.KEY_D, e.KEY_A, e.KEY_S],
  "orbital_smoke": [e.KEY_D, e.KEY_D, e.KEY_S, e.KEY_W],
  "hmg_replacement": [e.KEY_W, e.KEY_S, e.KEY_A, e.KEY_D, e.KEY_D, e.KEY_A],
  "shield_relay": [e.KEY_S, e.KEY_W, e.KEY_A, e.KEY_D, e.KEY_A, e.KEY_S],
  "tesla_tower": [e.KEY_S, e.KEY_W, e.KEY_D, e.KEY_W, e.KEY_A, e.KEY_D],
  # Engineering Bay
  "minefield": [e.KEY_S, e.KEY_A, e.KEY_W, e.KEY_D],
  "supply_pack": [e.KEY_S, e.KEY_A, e.KEY_S, e.KEY_W, e.KEY_W, e.KEY_S],
  "grenade_launcher": [e.KEY_S, e.KEY_A, e.KEY_W, e.KEY_A, e.KEY_S],
  "laser_cannon": [e.KEY_S, e.KEY_A, e.KEY_W, e.KEY_A, e.KEY_S],
  "incendiary_mines": [e.KEY_S, e.KEY_A, e.KEY_A, e.KEY_S],
  "guard_dog_rover": [e.KEY_S, e.KEY_A, e.KEY_S, e.KEY_W, e.KEY_A, e.KEY_S, e.KEY_S],
  "ballistic_shield": [e.KEY_S, e.KEY_A, e.KEY_W, e.KEY_W, e.KEY_D],
  "arc_thrower": [e.KEY_S, e.KEY_D, e.KEY_W, e.KEY_A, e.KEY_S],
  "shield_generator": [e.KEY_S, e.KEY_W, e.KEY_A, e.KEY_D, e.KEY_A, e.KEY_D],
  # Robotics Workshop
  "machine_sentry": [e.KEY_S,e.KEY_W, e.KEY_D, e.KEY_S, e.KEY_D, e.KEY_S, e.KEY_W],
  "gatling_sentry": [e.KEY_S, e.KEY_W, e.KEY_D, e.KEY_A],
  "mortar_sentry": [e.KEY_S, e.KEY_W, e.KEY_D, e.KEY_D, e.KEY_S],
  "guard_dog": [e.KEY_S, e.KEY_W, e.KEY_A, e.KEY_W, e.KEY_D, e.KEY_S],
  "autocannon_sentry": [e.KEY_S, e.KEY_W, e.KEY_D, e.KEY_W, e.KEY_A, e.KEY_W],
  "rocket_sentry": [e.KEY_S, e.KEY_W, e.KEY_D, e.KEY_D, e.KEY_A],
  "ems_sentry": [e.KEY_S, e.KEY_S, e.KEY_W, e.KEY_W, e.KEY_A],
}

key_press_dict: dict[str, str] = { }

yaml_config: dict = yaml.safe_load(open(arguments.file))
for stratagem, stratagem_key in yaml_config["main"].items():
  key_press_dict[stratagem_key] = stratagem
  print(f"{stratagem_key} - {stratagem}")
