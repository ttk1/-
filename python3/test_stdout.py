from unittest import TestCase
from unittest.mock import patch, call


class Hoge():
    def __init__(self, name):
        self.name = name

    def hoge(self):
        print(self.name)


class TestHoge(TestCase):
    @patch('test_stdout.print')
    def test_hoge1(self, _print):
        hoge = Hoge('hoge')
        hoge.hoge()

        expected = call('hoge')
        actual = _print.call_args
        self.assertEqual(expected, actual)

    @patch('sys.stdout')
    def test_hoge2(self, _stdout):
        hoge = Hoge('hoge')
        hoge.hoge()

        expected = [
            call('hoge'),
            call('\n')
        ]
        actual = _stdout.write.call_args_list
        self.assertEqual(expected, actual)
