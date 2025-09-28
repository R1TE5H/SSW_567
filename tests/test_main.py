"""Tests for the main Hello World functionality."""

from scripts.main import hello_world


def test_print_output(capsys):
    """Test that hello_world function prints the expected output."""
    hello_world()
    captured = capsys.readouterr()
    print("Capsys captured:", captured.out)
    assert "Hello World" in captured.out
