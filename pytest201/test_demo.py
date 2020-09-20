import demo
import pytest

class TestAdd:

    def test_basics(self):
        assert True

    def test_add(self):
        assert demo.add(1, 2) == 3
 
    def test_err(self):
        with pytest.raises(demo.MysteryError):
            demo.add(99, 1)
 
    @pytest.mark.parametrize(
        'a, b, expected', [
            (1, 1, 2),
            (2, 1, 3),
            (3, 1, 4),
        ]
    )
    def test_with_param(self, a, b, expected):
        assert demo.add(a,  b) == expected


def test_fixture(my_fixture):
    assert my_fixture == 42


def test_capsys(capsys):
    '''capsys fixture intercepts system stdout stderr'''
    print('hello')
    print("bye")
    out, err = capsys.readouterr()
    assert "hello\nbye\n" == out

# there is also caplog


def test_monkeypatch(monkeypatch):
    def fake_add(a, b):
        return 42
    monkeypatch.setattr(demo, 'add', fake_add)
    assert demo.add(3, 4) == 42


def test_tmpdir(tmpdir):
    somefile = tmpdir.join("something.txt")
    somefile.write('{"hello":"world"}')

    result = demo.read_json(str(somefile))
    assert result['hello'] == "world"


def test_fixture_with_fixtures(capsys, captured_print):
    print("more")
    out, err = capsys.readouterr()
    assert  out == "hello\nmore\n"
