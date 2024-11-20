import os
from config import *

def main():
    env_vars = load_env(".env")
    num_servers = count_servers(env_vars)
    
    generate_docker_compose(env_vars, num_servers)
    generate_mediamtx_files(env_vars, num_servers)
    generate_start_bat(num_servers)

if __name__ == "__main__":
    main()
