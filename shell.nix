{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShellNoCC {
  packages = with pkgs; [
    (python311.withPackages (ps: with ps; [
      evdev
      pyyaml
    ]))
  ];
}
