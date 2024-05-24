from pathlib import Path

files = []

for filepath in files:
    filepath = Path(filepath)
    filedir = filepath.parent
    filedir.mkdir(parents=True, exist_ok=True)
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()