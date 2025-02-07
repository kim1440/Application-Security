import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ftp.main import print_menu, main


class testMain(unittest.TestCase):  # 클래스 이름을 PEP 8 스타일로 변경
    def test_print_menu(self):
        """메뉴 출력 함수 테스트"""
        result = print_menu()  # main. 접두어 제거
        self.assertIsInstance(result, str)  # 문자열 반환 확인
        self.assertTrue(len(result) > 0)  # 빈 문자열이 아닌지 확인

    def test_main(self):
        """메인 함수 테스트"""
        # 기본값으로 실행
        result = main()  # main. 접두어 제거
        self.assertIsNone(result)  # main 함수는 None을 반환