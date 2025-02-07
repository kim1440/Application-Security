import os
import sys
import unittest

from unittest.mock import patch
from io import StringIO

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ftp.main import print_menu, main


class testMain(unittest.TestCase):
    @patch('sys.argv', new=['main.py', '-H', '192.168.100.20', '-u', 'cju', '-p', 'security'])
    @patch('builtins.input', side_effect=['4'])
    def test_main(self, mock_input):
        """!
        @fn         test_main
        @brief      FTP 클라이언트 메인 함수 테스트
        @details    FTP 클라이언트 접속 후 메뉴를 출력하고 종료하는지 확인

        @param      mock_input   입력 모의 객체
        @return     None

        @author     남수만(sumannam@gmail.com)
        @date       2025.02.07
        """
        result = main()
        mock_input.assert_called()
        self.assertIsNone(result)