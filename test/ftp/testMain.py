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
    def test_main_with_argv(self, mock_input):
        """!
        @fn         test_main_with_argv
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
    

    @patch('builtins.input', side_effect=['192.168.100.20', 'cju', 'security', '4'])
    def test_main_with_input(self, mock_input):
        """!
        @fn         test_main_with_input
        @brief      입력 기반 메인 함수 테스트
        @details    사용자 입력으로 host, id, password를 받아 main() 함수 테스트

        @param      mock_input   입력 모의 객체 (host, id, pw, 메뉴선택)
        @return     None 

        @author     남수만(sumannam@gmail.com)
            @date       2025.02.07
        """
        result = main()
        mock_input.assert_called()
        self.assertEqual(mock_input.call_count, 4)  # 입력 4번 호출 확인
        self.assertIsNone(result)