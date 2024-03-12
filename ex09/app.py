# import subprocess
# import pkg_resources

# def run_command(command, check=True):
#     """Execute a system command and optionally check for errors."""
#     result = subprocess.run(command, capture_output=True, text=True)
#     if check and result.returncode != 0:
#         raise subprocess.CalledProcessError(result.returncode, command, output=result.stdout, stderr=result.stderr)
#     return result

# def build():
#     """Build the package."""
#     print("Building package...")
#     run_command(["python", "setup.py", "sdist", "bdist_wheel"])
#     print("Build complete.")

# def install():
#     """Install the package."""
#     print("Installing package...")
#     # The path to the package file might need to be updated depending on the build result.
#     package_file = "./dist/ft_package-0.0.1.tar.gz"
#     run_command(["pip", "install", package_file])
#     print("Installation complete.")

# def show():
#     """Show package details."""
#     package_name = "ft_package"
#     try:
#         dist = pkg_resources.get_distribution(package_name)
#         print(f"Package details for '{package_name}':")
#         print(f"Version: {dist.version}")
#         print(f"Location: {dist.location}")
#         print(f"Entry points: {dist.get_entry_map()}")
#     except pkg_resources.DistributionNotFound:
#         print(f"Package '{package_name}' is not installed.")

# def test():
#     """Run package tests."""
#     # Adjust this command to match how you run your tests.
#     # This example assumes pytest is being used.
#     print("Running tests...")
#     run_command(["pytest"], check=False)  # `check=False` allows tests to fail without aborting the script.

# if __name__ == "__main__":
#     build()
#     install()
#     show()
#     test()
