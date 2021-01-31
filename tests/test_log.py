from golog.log import (
    print_magenta, print_blue,
    label_format, label_print
)


def test_print_magenta(capsys):
    print_magenta("magenta")
    captured = capsys.readouterr()
    assert "magenta" in captured.out and "\x1b[35m" in captured.out

def test_print_blue(capsys):
    print_blue("blue")
    captured = capsys.readouterr()
    assert "blue" in captured.out and "\x1b[34m" in captured.out

def test_label_format():
    lb = label_format(
        "TEST", num_of_new_lines=1, num_of_tabs=1,
        label="LABEL: ", timestamp=True,
        exception=None
    )           
    assert "TEST" in lb and "LABEL" in lb and '\n' in lb and '\t' in lb

def test_label_print(capsys):
    lb = label_format(
        "TEST", num_of_new_lines=1, num_of_tabs=1,
        label="LABEL: ", timestamp=True,
        exception=None
    )
    captured = capsys.readouterr()
    out = captured.out()
    assert "TEST" in out and "LABEL" in out and '\n' in out and '\t' in out

