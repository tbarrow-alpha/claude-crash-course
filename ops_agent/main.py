from pathlib import Path
from datetime import datetime

INPUTS = Path("ops_agent/inputs")
OUTPUTS = Path("ops_agent/outputs")

def read_all_text_files(folder: Path):
    files = []
    for p in sorted(folder.glob("**/*.txt")):
        files.append((p, p.read_text()))
    return files

def main():
    INPUTS.mkdir(parents=True, exist_ok=True)
    OUTPUTS.mkdir(parents=True, exist_ok=True)

    goal = input("Type your goal (example: 'Summarize notes and list action items'): ").strip()
    if not goal:
        print("No goal entered. Exiting.")
        return

    files = read_all_text_files(INPUTS)
    if len(files) == 0:
        print(f"No .txt files found in {INPUTS}.")
        print("Create a file like ops_agent/inputs/notes.txt and try again.")
        return

    lines = []
    lines.append("# Agent Report")
    lines.append(f"- Goal: {goal}")
    lines.append(f"- Run time: {datetime.now().isoformat(timespec='seconds')}")
    lines.append("")
    lines.append("## Files processed")
    for path, text in files:
        lines.append(f"- {path} ({len(text)} characters)")
    lines.append("")
    lines.append("## Placeholder action items")
    lines.append("- [ ] Review notes and identify owners")
    lines.append("- [ ] Extract due dates")
    lines.append("")
    lines.append("## Notes (raw)")
    for path, text in files:
        lines.append("")
        lines.append(f"### {path}")
        lines.append(text.strip())

    out_path = OUTPUTS / "report.md"
    out_path.write_text("\n".join(lines))
    print(f"Created report: {out_path}")

if __name__ == "__main__":
    main()