import os
from pathlib import Path

cwd = os.getcwd()
print(cwd)

os.chdir("C:\\Users\\velez\\OneDrive\\Escritorio\\study\\rust\\rust_total")
cwd = os.getcwd()
print(cwd)

ruta = "C:\\Users\\velez\\OneDrive\\Escritorio\\study\\rust\\rust_total\\file-handling\\src\\main.rs"

dirname = os.path.dirname(ruta)
filename = os.path.basename(ruta)
print(f"dirname = {dirname}")
print(f"filename = {filename}")

dirname, filename = os.path.split(ruta)
print(f"dirname = {dirname}")
print(f"filename = {filename}")

ruta = Path("/Users/velez/OneDrive/Escritorio/study/rust/rust_total/file-handling/src")
file_path = ruta / "main.rs"
file = open(file_path)
print("\n===== Content File =====\n")
print(file.read())
file.close()
