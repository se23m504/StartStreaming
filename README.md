# StartStreaming

## Prerequisites

1. Docker Desktop
2. OBS Studio

## OBS configuration

- Create a scene collection named `Profile1` and a profile named `Profile1`.
- Create a scene collection named `Profile2` and a profile named `Profile2`.
- Add scenes and configure the input sources (e.g., HDMI cards) for each scene collection.
- For each profile, go to `Settings` -> `Stream`, set `Service` to WHIP, and enter the endpoint for each MediaMTX server:
    - Profile1: `http://localhost:8100/mystream/whip`
    - Profile2: `http://localhost:8200/mystream/whip`

## IP address configuration

The `docker-compose.yaml` is hardcoded to use the IP address `192.168.137.1`. You must update this to your specific network IP from the mobile hotspot configuration.