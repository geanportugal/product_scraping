import os
import platform
import subprocess
import venv


def create_virtualenv(venv_path):
    venv.create(venv_path, with_pip=True)


def activate_virtualenv(venv_path):
    if platform.system() == 'Windows':
        activate_script = os.path.join(venv_path, 'Scripts', 'activate.bat')
    else:
        activate_script = os.path.join(venv_path, 'bin', 'activate')
    activate_cmd = f'source {activate_script}' if platform.system() != 'Windows' else activate_script
    subprocess.call(activate_cmd, shell=True)


def install_requirements(venv_path):
    requirements_file = 'requirements.txt'
    pip_cmd = os.path.join(venv_path, 'Scripts', 'pip.exe') if platform.system() == 'Windows' else os.path.join(venv_path, 'bin', 'pip')
    install_cmd = f'{pip_cmd} install -r {requirements_file}'
    subprocess.call(install_cmd, shell=True)


def main():
    venv_path = 'venv'  # Define o caminho para a virtualenv
    create_virtualenv(venv_path)  # Cria a virtualenv
    activate_virtualenv(venv_path)  # Ativa a virtualenv
    install_requirements(venv_path)  # Instala os requisitos


if __name__ == '__main__':
    main()
