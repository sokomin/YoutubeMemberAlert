@echo off
FOR /F "usebackq delims== tokens=1,2" %%a IN ("config.txt") DO SET %%a=%%b
python member_alert_batch.py
rem 戻り値が1ならブラウザ起動
if %ERRORLEVEL% equ 1 (
    start "C:\Program Files\Google\Chrome\Application\chrome.exe" "https://www.youtube.com/channel/%USER_ID%/membership"
)
exit 0