
# 보안 요구사항

- [Brute-force Attack](../manual/Brute-force%20Attack.md) 발생 위험 높음
<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://embed.figma.com/board/3pR3DysZvHNqRyTTlz9q6K/FTP-Brute-force-Attack?node-id=0-1&embed-host=share" allowfullscreen></iframe>

## 보안 문제점

- 아래 명령어 활용하여 로그인이 가능하다. 
```
python main.py --host 192.168.100.20 --user cju --password security
```
![](attachments/Pasted%20image%2020250320215558.png)
		
- ID와 PW를 조합하여 명령어를 만들 경우, [Brute-force Attack](../manual/Brute-force%20Attack.md)이 가능하다.
```
python main.py --host 192.168.100.20 --user cju --password aaaaaaaa
python main.py --host 192.168.100.20 --user cju --password aaaaaaab
python main.py --host 192.168.100.20 --user cju --password aaaaaaac
python main.py --host 192.168.100.20 --user cju --password aaaaaaad
...
python main.py --host 192.168.100.20 --user cju --password security
```

## 공격 시도

### 공격 명령어 작성
```
python ftp_attack.py -H 192.168.100.20 -U short_users.txt -P short_passwords.txt
```

- 명령어 설명
	- `short_users.txt` : 사용자 아이디 집합
	- `short_passwords.txt` : 사용자 패스워드 집합

### 공격 알고리즘 개발

1. **시작 및 초기화**
	- 메인 함수 실행 및 배너 출력
	- 명령줄 인자 파싱 (`parse_arguments`)
2. **입력 처리**:
	- 사용자 이름 처리: 단일 사용자(`-u`), 사용자 리스트(`-U`), 또는 기본값(`cju`)
	- 비밀번호 처리: 단일 비밀번호(`-p`), 비밀번호 리스트(`-P`), 또는 기본값(`security`)
3. **브루트포스 공격 설정**:
	- `FTPBruteforcer` 객체 생성
	- 공격 초기화 및 정보 출력
	- 자격 증명 큐 생성
4. **멀티스레드 실행**:
	- 작업자 스레드 생성 및 시작
	- 각 스레드에서 자격 증명 시도
	- 로그인 시도 및 진행 상황 업데이트
5. **결과 처리**:
	- 성공 시: 성공 메시지 출력 및 결과 파일에 저장
	- 실패 시: 실패 메시지 출력

### 실행 결과

![](attachments/Pasted%20image%2020250320222906.png)