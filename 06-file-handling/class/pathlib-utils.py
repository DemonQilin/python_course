from pathlib import Path, PureWindowsPath

main_path = Path("/Users/velez/OneDrive/Escritorio/study/rust/rust_total/file-handling/src/main.rs")
content = main_path.read_text()
print(content)

filename = main_path.name
print(f"filename is: {filename}")

suffix = main_path.suffix
print(f"suffix is: {suffix}")

stem = main_path.stem
print(f"stem is: {stem}")

windows_pure_path = PureWindowsPath(main_path)
print(f"path in windows: {windows_pure_path}")
