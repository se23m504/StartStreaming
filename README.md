# StartStreaming

## Prerequisites

1. Install:

    - Docker Desktop
    - OBS Studio

2. Prepare the `.env` file

    Copy `.env.dev` to `.env` and update with your environment-specific values.

    ```bash
    cp .env.dev .env
    ```

    In the `.env` file:

    - `IP` is the IP address to which the WebRTC server will be bound.
    - `PORT_1` is the WebRTC HTTP listener port, which can be used for WHIP and WHEP.
    - `LISTENER_PORT_1` is the WebRTC ICE/UDP port.

3. Set up the necessary OBS profiles and scene collections:

    - Let `N` be the number of instances you want to create (i.e., the maximum number of `PORT_X` defined in the `.env` file).
    - Create a scene collection and a profile for each instance (e.g., `Profile1`, `Profile2`, ... `ProfileN`).
    - Add scenes and configure the input sources (e.g., HDMI cards) for each scene collection.
    - Go to `Settings` -> `Stream`, set the `Service` to WHIP, and enter the endpoint for each MediaMTX server: `http://{{IP}}:{{PORT_X}}/mystream/whip`.

    Repeat for each profile from `X=1` to `X=N`.

## Run

The Docker image will automatically generate the necessary configurations for you. After finishing with the prerequisites, simply run the following command from the root repository:

```
docker run --rm -v ${PWD}:/app/data se23m504/startstreaming
```

## Build

The image is already available on DockerHub, but if you need to build it again for any reason, run the following command from the root directory:

```
docker build -t se23m504/startstreaming .\src -f .\docker\Dockerfile
```
