import argparse
import os
import pwd

from evdev import InputDevice
import yaml

user: str = os.getlogin()
user_uid: int = pwd.getpwnam(user).pw_uid
user_gid: int = pwd.getpwnam(user).pw_gid
user_config_dir: str = os.getenv("XDG_CONFIG_HOME", f"/home/{user}/.config")
user_config_file: str = os.path.join(user_config_dir, "hd2pystratmacro/config.yaml")
source_install_path: str = os.path.dirname(os.path.realpath(__file__))
source_config_file: str = os.path.join(source_install_path, "config.yaml")

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", default=user_config_file, help="Location of configuration file")
parser.add_argument("-d", "--device", default="/dev/input/event0", help="Input device to use")
arguments = parser.parse_args()

try:
  yaml.safe_load(open(arguments.file))
except FileNotFoundError:
  # We only attempt to generate the config file if it's at XDG_CONFIG_HOME because we don't want to create extraneous directories in the case of a mistyped path
  if arguments.file == user_config_file:
    print(f"Configuration file does not exist at XDG_CONFIG_HOME: {user_config_file}, generating...")
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

input_device: InputDevice = InputDevice(arguments.device)

print(f"Configuration file: {arguments.file}")

key_press_dict: dict[str, str] = { }

yaml_config: dict = yaml.safe_load(open(arguments.file))
for stratagem, stratagem_key in yaml_config["main"].items():
  key_press_dict[stratagem_key] = stratagem
  print(f"{stratagem_key} - {stratagem}")
