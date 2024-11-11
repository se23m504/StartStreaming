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

echo Launching OBS instances
start /MIN "OBS1" /D "C:\Program Files\obs-studio\bin\64bit" "obs64.exe" --profile "Profile1" --collection "Profile1" --multi --startstreaming
timeout /t 1 >nul
start /MIN "OBS2" /D "C:\Program Files\obs-studio\bin\64bit" "obs64.exe" --profile "Profile2" --collection "Profile2" --multi --startstreaming

pause
