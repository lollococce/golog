import .log as log


def test_print_magenta():
    log.print_magenta("magenta")
    captured = capsys.readouterr()
    assert captured.out == "magenta"
