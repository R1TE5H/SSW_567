from scripts.main import HelloWorld


def test_print_output(capsys):
    HelloWorld()
    captured = capsys.readouterr()
    print("Capsys captured:", captured.out)
    assert "Hello World" in captured.out
