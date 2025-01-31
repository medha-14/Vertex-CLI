import subprocess
import pytest

# This test module is underdevelopment and can be improved further.


def run_command(command):
    """Helper function to run shell commands and return output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr, result.returncode


def test_tex_basic_query():
    """Test querying the CLI with a basic prompt."""
    stdout, stderr, returncode = run_command("tex 'tell me about solar system'")
    assert returncode == 0, f"Query execution failed: {stderr}"
    assert stdout, "Query response is empty"


def test_tex_debug():
    """Test debugging the last two commands."""
    stdout, stderr, returncode = run_command("tex --debug")
    assert returncode == 0, f"Debug command failed: {stderr}"
    assert stdout, "Debug output is empty"


def test_tex_debug_with_prompt():
    """Test debugging with a custom prompt message."""
    stdout, stderr, returncode = run_command(
        "tex 'I believe this can be solved by changing the environment variable' --debug"
    )
    assert returncode == 0, f"Debug command with prompt failed: {stderr}"
    assert stdout, "Debug output is empty"
