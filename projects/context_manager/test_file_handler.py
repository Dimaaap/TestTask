import pytest
from unittest.mock import mock_open, patch
from file_handler import FileContext


class TestFileContext:

    @patch('builtins.open', new_callable=mock_open)
    def test_write_to_file(self, mock_file):
        with FileContext('test.txt', 'w') as f:
            f.write('Line 1\n')
            f.write('Line 2\n')
            f.write('Line 3\n')

        mock_file.assert_called_with('test.txt', 'w')

        mock_file().write.assert_any_call('Line 1\n')
        mock_file().write.assert_any_call('Line 2\n')
        mock_file().write.assert_any_call('Line 3\n')

    @patch('builtins.open', new_callable=mock_open)
    def test_file_close(self, mock_file):
        with FileContext('test.txt', 'w') as f:
            f.write('Line 1')

        mock_file().close.assert_called_once()

    @patch('builtins.open', new_callable=mock_open)
    def test_handle_exception_in_exit(self, mock_file):
        with pytest.raises(ValueError):
            with FileContext('test.txt', 'w') as f:
                f.write('Line 1')
                raise ValueError('Some error')

        mock_file().close.assert_called_once()

    @patch('builtins.open', new_callable=mock_open)
    def test_read_mode(self, mock_file):
        mock_file.return_value.read.return_value = 'File content'

        with FileContext('test.txt', 'r') as f:
            content = f.read()

        mock_file.assert_called_with('test.txt', 'r')
        assert content == 'File content'
