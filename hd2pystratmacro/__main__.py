from .config import input_device
from .key_handler import handle_key_event

def main() -> None:
  try:
    for event in input_device.read_loop():
      handle_key_event(event)
  except KeyboardInterrupt:
    exit()

if __name__ == "__main__":
  main()
