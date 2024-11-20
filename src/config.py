import os
import re

def load_env(filename=".env"):
    env_vars = {}
    with open(filename) as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                env_vars[key] = value
    return env_vars

def count_servers(env_vars):
    server_keys = [key for key in env_vars if re.match(r"PORT_\d+", key)]
    return len(server_keys)

def generate_docker_compose(env_vars, num_servers):
    ip = env_vars.get("IP")
    services = []
    
    for i in range(1, num_servers + 1):
        port = env_vars.get(f"PORT_{i}")
        listener_port = env_vars.get(f"LISTENER_PORT_{i}")
        service = f"""
  mediamtx-{i}:
    container_name: mediamtx-{i}
    environment:
      - MTX_WEBRTCADDITIONALHOSTS={ip}
    image: bluenviron/mediamtx
    ports:
      - {port}:{port}
      - {listener_port}:{listener_port}/udp
    volumes:
      - ./mediamtx/mediamtx_{i}.yml:/mediamtx.yml
"""
        services.append(service)
    
    compose_content = f"""
name: streaming

services:
{''.join(services)}
"""
    
    with open("docker-compose.yml", "w") as f:
        f.write(compose_content)

def generate_mediamtx_files(env_vars, num_servers):
    # os.makedirs("mediamtx")
    mediamtx_dir = "mediamtx"
    if not os.path.exists(mediamtx_dir):
        os.makedirs(mediamtx_dir)
    
    with open("templates/mediamtx.yml", "r") as template_file:
        template_content = template_file.read()
    
    for i in range(1, num_servers + 1):
        port = env_vars.get(f"PORT_{i}")
        listener_port = env_vars.get(f"LISTENER_PORT_{i}")
        
        generated_content = template_content.replace("{{WEBRTC_PORT}}", port).replace("{{WEBRTC_LISTENER_PORT}}", listener_port)
        
        with open(f"mediamtx/mediamtx_{i}.yml", "w") as f:
            f.write(generated_content)

    existing_files = os.listdir("mediamtx")
    for file in existing_files:
        if file.startswith("mediamtx_"):
            file_num = int(file.split("_")[1].split(".")[0])
            if file_num > num_servers:
                os.remove(f"mediamtx/{file}")
                print(f"Removed extra file: {file}")

def generate_start_bat(num_servers):
    with open("templates/start.bat", "r") as template_file:
        bat_template = template_file.read()

    obs_instances = ""
    for i in range(1, num_servers + 1):
        obs_instance = f"""
echo Launching OBS instance {i}
start /MIN "OBS{i}" /D "C:\\Program Files\\obs-studio\\bin\\64bit" "obs64.exe" --profile "Profile{i}" --collection "Profile{i}" --multi --startstreaming
timeout /t 1 >nul
"""
        obs_instances += obs_instance
    
    bat_content = bat_template.replace("{{OBS_INSTANCES}}", obs_instances)
    
    with open("start.bat", "w") as f:
        f.write(bat_content)
