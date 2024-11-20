@echo off

echo Enabling mobile hotspot
powershell -NoProfile -ExecutionPolicy Bypass -File ".\mhotspot.ps1"

echo Starting docker desktop
start /MIN "DockerDesktop" "C:\Program Files\Docker\Docker\Docker Desktop.exe"

:waitForDocker
tasklist | find /i "Docker Desktop.exe" >nul
if errorlevel 1 (
    timeout /t 1 >nul
    goto waitForDocker
)

:waitForDaemon
docker info >nul 2>&1
if errorlevel 1 (
    timeout /t 1 >nul
    goto waitForDaemon
)

echo Starting docker compose
cd ".\mediamtx"
docker compose up -d

{{OBS_INSTANCES}}

pause
