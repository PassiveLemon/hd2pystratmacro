{ pkgs ? import <nixpkgs> { system = builtins.currentSystem; },
  lib ? pkgs.lib,
  python3Packages ? pkgs.python3Packages
}:

with python3Packages;
let
  shell = import ./shell.nix { inherit pkgs; };
in
buildPythonApplication rec {
  pname = "hd2pystratmacro";
  version = "1.0.2";

  src = ./.;

  nativeBuildInputs = [
    setuptools
  ];

  propagatedBuildInputs = shell;
  
  doCheck = false;

  meta = with lib; {
    description = "A Python based macro script for Helldivers 2";
    homepage = "https://github.com/passiveLemon/hd2pystratmacro";
    changelog = "https://github.com/passiveLemon/hd2pystratmacro/releases/tag/${version}";
    license = licenses.gpl3;
    maintainers = with maintainers; [ passivelemon ];
    platforms = [ "x86_64-linux" ];
  };
}
