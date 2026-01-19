import builtins


def _fake_input(responses: list[str]):
    iterator = iter(responses)

    def _input(_: str = "") -> str:
        return next(iterator)

    return _input


def test_main_exit_immediately(monkeypatch, capsys):
    from main import main

    monkeypatch.setattr(builtins, "input", _fake_input(["3"]))
    main()

    captured = capsys.readouterr()
    assert "Welcome to Todo List App" in captured.out
    assert "Goodbye!" in captured.out


def test_main_invalid_choice_then_exit(monkeypatch, capsys):
    from main import main

    monkeypatch.setattr(builtins, "input", _fake_input(["9", "3"]))
    main()

    captured = capsys.readouterr()
    assert "Invalid choice. Please try again." in captured.out
    assert "Goodbye!" in captured.out


def test_main_login_message_then_exit(monkeypatch, capsys):
    from main import main

    monkeypatch.setattr(builtins, "input", _fake_input(["1", "3"]))
    main()

    captured = capsys.readouterr()
    assert "Login functionality not implemented yet" in captured.out
    assert "Goodbye!" in captured.out


def test_main_signup_message_then_exit(monkeypatch, capsys):
    from main import main

    monkeypatch.setattr(builtins, "input", _fake_input(["2", "3"]))
    main()

    captured = capsys.readouterr()
    assert "Sign Up functionality not implemented yet" in captured.out
    assert "Goodbye!" in captured.out
