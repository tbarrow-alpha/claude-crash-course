from pathlib import Path
from datetime import datetime

def main():
    name = input("What is your name? ").strip()
    if not name:
        name = "friend"

    out_dir = Path("outputs")
    out_dir.mkdir(exist_ok=True)

    msg = f"Hello, {name}. Time is {datetime.now()}.\n"
    out_file = out_dir / "hello.txt"
    out_file.write_text(msg)

    print(msg)
    print(f"Wrote a file here: {out_file}")

if __name__ == "__main__":
    main()