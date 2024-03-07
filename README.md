# hd2pystratmacro
A Python based macro script for HELLDIVERS 2 </br>

You can assign Stratagem macros to keybinds. </br>

## Disclaimer
I am not responsible for any bans or data loss as a result of using this. This was a project for me to learn Python. If you are worried about getting banned, don't use it and be a legitimate player :) </br>

# Dependencies
- Linux. <b>This is not supported on Windows or MacOS</b> though it may in the future.
- X11. This is not supported on Wayland.
- Sudo. This requires access to `/dev`.
- Python packages: `evdev pyyaml`

# Usage
### Nix:
- You can get the package in my [flake repository](https://github.com/PassiveLemon/lemonake). </br>
### Source:
- Clone the repo
- Run `sudo python3 __main__.py`
- Edit the generated config file in your `~/.config/hd2pystratmacro/config.yaml`. You can also supply a config file with `-f <path to config.yaml`. Please read the configuration below, you need to configure the file to enable functionality. </br>
  - Arguments can be found by tacking `-h` or `--help`

When running, hold ctrl and press your keybind to activate the macro.

# Configuration (config.yaml)
## Structure format:
```yaml
main:
  (stratagem): "KEY_*"
```
### Example:
```yaml
main:
  reload: "KEY_P"
  reinforce: "KEY_Y"
```
- You can define any Stratagems without duplicates.

## Available Stratagems:
- `reload`: Hot-reload the configuration file to change key-bind without restarting the script

### General
- `reinforce`: Reinforce
- `resupply`: Resupply
- `sos`: SOS Beacon
- `hellbomb`: Hellbomb
- `flare`: Orbital Illumination Flare
- `flag`: Super Earth Flag
- `seaf`: SEAF Artillery

### Patriotic Administration Center
- `machine`: Machine Gun
- `antimaterial`: Anti-Material Rifle
- `stalwart`: Stalwart
- `expendable`: Expendable Anti-Tank
- `recoilless`: Recoilless Rifle
- `flamethrower`: Flamethrower
- `autocannon`: Autocannon
- `railgun`: Railgun
- `spear`: Spear

### Orbital Cannons
- `orbital_gatling`: Orbital Gatling Strike
- `orbital_airburst`: Orbital Airburst Strike
- `orbital_120mm`: Orbital 120MM HE Barrage
- `orbital_380mm`: Orbital 380MM HE Barrage
- `orbital_walking`: Orbital Walking Barrage
- `orbital_laser`: Orbital Laser
- `orbital_railcannon`: Orbital Railcannon Strike

### Hangar
- `eagle_rearm`: Eagle Rearm
- `eagle_strafing`: Eagle Strafing Run
- `eagle_airstrike`: Eagle Airstrike
- `eagle_cluster`: Eagle Cluster Bomb
- `eagle_napalm`: Eagle Napalm Airstrike
- `jump_pack`: Jump Pack
- `eagle_smoke`: Eagle Smoke Strike
- `eagle_110mm`: Eagle 110MM Rocket Pods
- `eagle_500kg`: Eagle 500KG Bomb

### Bridge
- `orbital_precision`: Orbital Precision Strike
- `orbital_gas`: Orbital Gas Strike
- `orbital_ems`: Orbital EMS Strike
- `orbital_smoke`: Orbital Smoke Strike
- `hmg_placement`: HMG Placement
- `shield_relay`: Shield Generator Relay
- `tesla_tower`: Tesla Tower

### Engineering Bay
- `minefield`: Anti-Personnel Minefield
- `supply_pack`: Supply Pack
- `grenade_launcher`: Grenade Launcher
- `laser_cannon`: Laser Cannon
- `incendiary_mines`: Incendiary Mines
- `guard_dog_rover`: Guard Dog Rover
- `ballistic_shield`: Ballistic Shield Backpack
- `arc_thrower`: Arc Thrower
- `shield_generator`: Shield Generator Pack

### Robotics Workshop
- `machine_sentry`: Machine Gun Sentry
- `gatling_sentry`: Gatling Sentry
- `mortar_sentry`: Mortar Sentry
- `guard_dog`: Guard Dog
- `autocannon_sentry`: Autocannon Sentry
- `rocket_sentry`: Rocket Sentry
- `ems_sentry`: EMS Mortar Sentry

You can have other sets of key-binds but the script currently only reads from `main`. Definable sets will be implemented in the future.
