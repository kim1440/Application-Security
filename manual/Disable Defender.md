
1. Power Shell(관리자 모드)를 실행한다.
		![](attachments/Pasted%20image%2020250308225718.png)
	
2. 아래 스크립트를 복사한다.
```
New-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender" -Name "DisableRealtimeMonitoring" -Value 1 -PropertyType DWORD -Force

# 실시간 보호 끄기
Set-MpPreference -DisableRealtimeMonitoring $true

# 동작 모니터링 끄기
Set-MpPreference -DisableBehaviorMonitoring $true

# 스캔 기능 끄기
Set-MpPreference -DisableScanningNetworkFiles $true
Set-MpPreference -DisableScanningMappedNetworkDrivesForFullScan $true

# 클라우드 보호 기능 끄기
Set-MpPreference -MAPSReporting Disabled
Set-MpPreference -SubmitSamplesConsent NeverSend

# 랜섬웨어 보호 끄기
Set-MpPreference -EnableControlledFolderAccess Disabled

# 침입 방지 보호 끄기
Set-MpPreference -DisableIntrusionPreventionSystem $true

# 네트워크 보호 끄기
Set-MpPreference -DisableIOAVProtection $true

# 자동 샘플 제출 끄기
Set-MpPreference -SubmitSamplesConsent 2

# 탐지된 위협에 대한 자동 조치 비활성화
Set-MpPreference -LowThreatDefaultAction NoAction
Set-MpPreference -ModerateThreatDefaultAction NoAction
Set-MpPreference -HighThreatDefaultAction NoAction
```

3. Power Shell에서 붙여놓기 한 후 실행한다.
		![](attachments/Pasted%20image%2020250308225918.png)
