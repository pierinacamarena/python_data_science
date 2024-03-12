import subprocess
import pkg_resources
import os

def run_command(command, check=True):
    """Execute a system command and optionally check for errors."""
    result = subprocess.run(command, capture_output=True, text=True)
    if check and result.returncode != 0:
        raise subprocess.CalledProcessError(result.returncode,
                                            command,
                                            output=result.stdout,
                                            stderr=result.stderr)
    return result


def build():
    """Build the package."""
    print("Building package...")
    run_command(["python", "setup.py", "sdist", "bdist_wheel"])
    print("Build complete.")


def install():
    """Install the package."""
    print("Installing package...")
    package_file = "./dist/ft_package-0.0.1.tar.gz"
    run_command(["pip", "install", package_file])
    print("Installation complete.")


def show():
    """Show package details."""
    package_name = "ft_package"
    try:
        dist = pkg_resources.get_distribution(package_name)
        print(f"Package details for '{package_name}':")
        print(f"Version: {dist.version}")
        print(f"Location: {dist.location}")
        print(f"Entry points: {dist.get_entry_map()}")
    except pkg_resources.DistributionNotFound:
        print(f"Package '{package_name}' is not installed.")


def test():
    """Run package tests."""
    print("Running tests...")
    os.system("python3.10 tester.py")


if __name__ == "__main__":
    build()
    install()
    show()
    test()
