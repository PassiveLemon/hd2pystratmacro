{ pkgs ? import <nixpkgs> { system = builtins.currentSystem; },
  lib ? pkgs.lib,
  python3Packages ? pkgs.python3Packages
}:
python3Packages.buildPythonApplication rec {
  pname = "hd2pystratmacro";
  version = "1.0.3";

  src = ./.;

  nativeBuildInputs = with python3Packages; [
    setuptools
  ];

  propagatedBuildInputs = with python3Packages; [
    evdev
    pyyaml
  ];

  doCheck = false;

  meta = with lib; {
    description = "A Python based macro script for Helldivers 2";
    homepage = "https://github.com/passiveLemon/hd2pystratmacro";
    changelog = "https://github.com/passiveLemon/hd2pystratmacro/releases/tag/${version}";
    license = licenses.gpl3;
    maintainers = with maintainers; [ passivelemon ];
    platforms = [ "x86_64-linux" ];
    mainProgram = "hd2pystratmacro";
  };
}
