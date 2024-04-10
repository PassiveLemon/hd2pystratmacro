{ pkgs ? import <nixpkgs> { } }:
pkgs.mkShellNoCC {
  packages = with pkgs; [
    (import ./default.nix { inherit pkgs; })
  ];
}
