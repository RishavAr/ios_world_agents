from fastapi import FastAPI, Query
from pathlib import Path
from typing import Optional
import subprocess, sys

app = FastAPI(title="iOS Agents Orchestrator")

@app.get("/")
def home():
    return {
        "status": "ok",
        "msg": "Use /run_task?task=SafariSearch.json&agent=openai&model=gpt-4o",
        "examples": ["/run_task?task=NotesEntry.json", "/run_task?task=ToggleWiFi.json"]
    }

def _proj_root() -> Path:
    return Path(__file__).resolve().parent.parent

@app.get("/run_task")
def run_task(
    task: str = Query(..., description="JSON file name under tasks/ or repo root"),
    agent: str = Query("openai"),
    model: str = Query("gpt-4o"),
    textgrad: bool = Query(True)
):
    root = _proj_root()
    candidates = list((root / "tasks").glob("**/*.json")) + list(root.glob("*.json"))
    sel: Optional[Path] = None
    tl = task.lower()
    for c in candidates:
        if c.name.lower() == tl:
            sel = c
            break
    if not sel:
        return {"ok": False, "error": f"Task '{task}' not found in tasks/ or root."}

    cmd = [sys.executable, "-m", "src.main", str(sel), agent, model]
    if textgrad:
        cmd.append("--textgrad")
    cmd.append("--exec")

    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        return {"ok": True, "ran": " ".join(cmd), "output": out}
    except subprocess.CalledProcessError as e:
        return {
            "ok": False,
            "ran": " ".join(cmd),
            "returncode": e.returncode,
            "output": e.output,
        }
