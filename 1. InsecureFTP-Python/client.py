from ftplib import FTP
import os
from typing import List

class FTPClient:
    def __init__(self, host: str, user: str, passwd: str):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.ftp = None

    def connect(self) -> bool:
        """FTP 서버에 연결"""
        try:
            self.ftp = FTP(self.host)
            self.ftp.login(user=self.user, passwd=self.passwd)
            print(f"Connected to {self.host}")
            print(f"Welcome message: {self.ftp.getwelcome()}")
            return True
        except Exception as e:
            print(f"Connection failed: {str(e)}")
            return False

    def list_files(self, path: str = ".") -> List[str]:
        """현재 디렉토리의 파일 목록 조회"""
        try:
            files = []
            self.ftp.dir(path, files.append)
            return files
        except Exception as e:
            print(f"Error listing files: {str(e)}")
            return []

    def get_simple_file_list(self) -> List[str]:
        """파일 이름만 리스트로 반환 (폴더 제외)"""
        try:
            all_items = []
            self.ftp.dir(all_items.append)
            
            # 폴더를 제외하고 파일만 필터링 (첫 문자가 'd'인 경우 폴더)
            files = []
            for item in all_items:
                # FTP LIST 명령의 결과에서 첫 문자가 'd'가 아닌 경우만 파일
                if not item.startswith('d'):
                    # 파일명만 추출 (마지막 부분)
                    filename = item.split()[-1]
                    files.append(filename)
            
            return files
        except Exception as e:
            print(f"Error getting file list: {str(e)}")
            return []

    def upload_file(self, local_path: str, remote_path: str = None) -> bool:
        """파일 업로드"""
        try:
            if not os.path.exists(local_path):
                print(f"Local file {local_path} does not exist.")
                return False
                
            if remote_path is None:
                remote_path = os.path.basename(local_path)
                
            with open(local_path, 'rb') as file:
                self.ftp.storbinary(f'STOR {remote_path}', file)
            print(f"Successfully uploaded {local_path} to {remote_path}")
            return True
        except Exception as e:
            print(f"Upload failed: {str(e)}")
            return False

    def download_file(self, remote_path: str, local_path: str = None) -> bool:
        """파일 다운로드"""
        try:
            if local_path is None:
                local_path = os.path.basename(remote_path)
                
            with open(local_path, 'wb') as file:
                self.ftp.retrbinary(f'RETR {remote_path}', file.write)
            print(f"Successfully downloaded {remote_path} to {local_path}")
            return True
        except Exception as e:
            print(f"Download failed: {str(e)}")
            return False

    def disconnect(self):
        """FTP 연결 종료"""
        if self.ftp:
            self.ftp.quit()
            print("Disconnected from FTP server")

def print_menu():
    """메인 메뉴 출력"""
    print("\n=== FTP 클라이언트 메뉴 ===")
    print("1. 파일 목록 보기")
    print("2. 파일 업로드")
    print("3. 파일 다운로드")
    print("4. 종료")
    print("========================")
    return input("메뉴를 선택하세요 (1-4): ")

def show_file_list_menu(files: List[str]) -> int:
    """파일 목록을 보여주고 선택받기"""
    print("\n=== 다운로드할 파일을 선택하세요 ===")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    print("0. 취소")
    
    while True:
        try:
            choice = int(input("\n파일 번호를 선택하세요 (0-{0}): ".format(len(files))))
            if 0 <= choice <= len(files):
                return choice
            print("잘못된 선택입니다.")
        except ValueError:
            print("숫자를 입력해주세요.")

def main():
    # FTP 서버 접속 정보
    HOST = "192.168.100.20"
    USER = "cju"
    PASSWD = "security"

    # FTP 클라이언트 인스턴스 생성
    client = FTPClient(HOST, USER, PASSWD)

    # 서버 연결
    if not client.connect():
        print("프로그램을 종료합니다.")
        return

    try:
        while True:
            choice = print_menu()

            if choice == "1":
                print("\n=== 파일 목록 ===")
                files = client.list_files()
                if files:
                    for file in files:
                        print(file)
                else:
                    print("파일이 없거나 목록을 가져올 수 없습니다.")

            elif choice == "2":
                # 지정된 파일 업로드
                local_path = "D:\\Git\\Application-Security\\1. InsecureFTP-Python\\application_security.txt"
                if not os.path.exists(local_path):
                    print(f"\n{local_path} 파일이 존재하지 않습니다.")
                    continue
                    
                print(f"\n{local_path} 파일을 업로드합니다...")
                client.upload_file(local_path)

            elif choice == "3":
                # 파일 목록 가져오기
                files = client.get_simple_file_list()
                if not files:
                    print("\n다운로드할 수 있는 파일이 없습니다.")
                    continue

                # 파일 선택하기
                file_choice = show_file_list_menu(files)
                if file_choice == 0:
                    continue

                # 선택한 파일 다운로드
                remote_file = files[file_choice - 1]
                # d:\ 경로에 다운로드
                local_path = "d:\\" + remote_file
                print(f"\n{remote_file} 파일을 {local_path}로 다운로드합니다...")
                client.download_file(remote_file, local_path)

            elif choice == "4":
                print("\n프로그램을 종료합니다.")
                break

            else:
                print("\n잘못된 선택입니다. 다시 선택해주세요.")

    finally:
        client.disconnect()

if __name__ == "__main__":
    main()