import pathlib
import subprocess


def test_command_a() -> None:
    result = subprocess.run(
        [
            "python",
            pathlib.Path(__file__).parent.parent
            / "src"
            / "sfy_python_template"
            / "__main__.py",
            "package-a",
            "command-a",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"Script failed: {result.stderr}"

    ## some others useful asserts


def test_command_b() -> None:
    result = subprocess.run(
        [
            "python",
            pathlib.Path(__file__).parent.parent
            / "src"
            / "sfy_python_template"
            / "__main__.py",
            "package-b",
            "command-b",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"Script failed: {result.stderr}"

    ## some others useful asserts
