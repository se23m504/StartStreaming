from dotenv import dotenv_values

from config import (
    count_servers,
    generate_docker_compose,
    generate_mediamtx_files,
    generate_start_bat,
)


def main():
    env_vars = dotenv_values(".env")

    num_servers = count_servers(env_vars)

    generate_docker_compose(env_vars, num_servers)
    generate_mediamtx_files(env_vars, num_servers)
    generate_start_bat(num_servers)


if __name__ == "__main__":
    main()
