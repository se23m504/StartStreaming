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
    - `PORT_X` is the WebRTC HTTP listener port, which can be used for WHIP and WHEP.
    - `LISTENER_PORT_X` is the WebRTC ICE/UDP port.

3. Set up the necessary OBS profiles and scene collections:

    Let `N` be the number of instances you want to create (i.e., the maximum number of `PORT_X` defined in the `.env` file).

    Repeat for each profile from `X=1` to `X=N`:

    - Create a scene collection called `ProfileX`.
    - Add scenes and configure the input source (e.g., an HDMI card).
    - Create a profile called `ProfileX`.
    - Go to `Settings` -> `Stream`, set the `Service` to WHIP, and enter the endpoint for the respective MediaMTX server: `http://{{IP}}:{{PORT_X}}/mystream/whip`. You may need to tweak as well the streaming settings.


## Run

The Docker image will automatically generate the necessary configurations for you. After finishing with the prerequisites, simply run the following command from the root repository:

```
docker run --rm -v ${PWD}:/app/data se23m504/startstreaming
```

Then, run the powershell auto-generated script:

```
./start.bat
```

## Build

The image is already available on DockerHub, but if you need to build it again for any reason, run the following command from the root directory:

```
docker build -t se23m504/startstreaming ./src -f ./docker/Dockerfile
```
