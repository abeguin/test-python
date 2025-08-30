{
  description = "Terraform dev environment flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/25.05";
    flake-parts.url = "github:hercules-ci/flake-parts";
  };

  outputs = {
    self,
    nixpkgs,
    flake-parts,
    ...
  } @ inputs:
    flake-parts.lib.mkFlake {inherit inputs;} {
      systems = ["x86_64-linux" "x86_64-darwin" "aarch64-darwin"];

      perSystem = {
        system,
        pkgs,
        ...
      }: let
        commonPackages = with pkgs; [xc cocogitto];
        pythonPackages =
          commonPackages
          ++ (with pkgs; [
            uv
            python313
            python313Packages.venvShellHook
          ]);
      in {
        formatter = inputs.nixpkgs.legacyPackages.${system}.alejandra;

        devShells.default = pkgs.mkShell {
          name = "terraform dev shell";
          packages = pythonPackages;
          venvDir = "./.venv";
        };

        # expose packages
        packages = builtins.listToAttrs (map
          (pkg: {
            name = pkg.pname or "unnamed";
            value = pkg;
          })
          pythonPackages);
      };
    };
}
