import PyInstaller.__main__
import os

def build_client():
    # Define paths
    project_dir = os.path.dirname(os.path.abspath(__file__))  # Inside client/src/
    client_dir = os.path.dirname(project_dir)  # Parent directory (client/)
    env_file = os.path.join(client_dir, ".env")
    output_dir = os.path.join(project_dir, "dist")  # Output to client/src/dist/

    # PyInstaller command
    PyInstaller.__main__.run([
        os.path.join(client_dir, "main.py"),  # Reference main.py in client/
        "--onefile",
        "--name=client",
        "--windowed",  # Suppress console for GUI
        f"--add-data={env_file}{os.pathsep}.env",  # Include .env
        f"--distpath={os.path.join(project_dir, 'dist')}",  # Output to client/src/dist/
        f"--workpath={os.path.join(project_dir, 'build')}",  # Build in client/src/build/
        f"--specpath={os.path.join(project_dir, 'spec')}",   # Spec in client/src/spec/
        "--noconfirm"
    ])

    print(f"Client built successfully in {output_dir}/client.exe")

if __name__ == "__main__":
    build_client()