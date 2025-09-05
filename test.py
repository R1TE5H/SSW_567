print("Hello World")


def test_print_output(capsys):
    print("Hello World from test.py")
    captured = capsys.readouterr()
    assert "Hello World" in captured.out
