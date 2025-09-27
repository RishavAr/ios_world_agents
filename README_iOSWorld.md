# iOSWorld I3A (iOS-to-Action) Agent Evaluation Framework

A next-generation evaluation framework for iOS automation that extends the Text-to-Action paradigm to the iOS ecosystem.  
**I3A (iOS-to-Action)** combines multiple reasoning agents, FastAPI-based orchestration, TextGrad optimization, and direct iOS simulator integration to evaluate multimodal agent performance in controlled Apple environments.

---

## 🚀 Features

### 🧠 Intelligent Multi-Agent System
- Supports **OpenAI**, **Gemini**, and **HuggingFace** backends  
- Unified interface for different LLM reasoning styles  
- Seamless switching between agents for side-by-side benchmarking

### 📱 iOS Simulator Orchestration
- Automatically detects available simulators (`xcrun simctl list devices`)  
- Launches target device (e.g. *iPhone 17 Pro*) via Xcode runtime  
- Executes UI actions and task scripts directly in the simulator  
- Compatible with macOS 14 + Xcode 15+

### ⚙️ FastAPI-Based Orchestrator
- Launches a local REST API for task management and live monitoring  
- Swagger UI at [`http://localhost:8000/docs`](http://localhost:8000/docs)  
- Routes:
  - `/run_task?task=SafariSearch.json`
  - `/run_task?task=NotesEntry.json`
  - `/run_task?task=ToggleWiFi.json`

### 🎯 Reward Evaluation System
Integrated performance scoring via `src/evaluator.py`:
- −0.05 per step → efficiency penalty  
+ 0.20 per subgoal → progress reward  
+ 1.00 completion bonus → task success  

### 🧩 TextGrad Optimization
- Gradient-based optimization for improved reasoning consistency  
- Applies to any LLM backend with the `--textgrad` flag

### 🧪 Real-Time Observation
- Live execution visible in the iOS Simulator  
- Logs and rewards recorded automatically under `/results/`

---

## 🛠️ Installation

### Prerequisites
- macOS with Xcode ≥ 15.0  
- Command-line tools installed:  
  ```bash
  xcode-select --install
  ```
- Python ≥ 3.11  
- Virtual environment recommended.

### Setup
```bash
git clone https://github.com/RishavAr/ios_world_agents.git
cd ios_world_agents
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ⚙️ Launching the Framework

### 1️⃣ Boot the iOS Simulator
Open Xcode → Developer Tools → Simulator  
or run:
```bash
open -a Simulator
```
Verify that **iPhone 17 Pro** (or your device) is booted.

### 2️⃣ Start the FastAPI Server
```bash
uvicorn src.api:app --host 0.0.0.0 --port 8000 --reload
```
Then visit [http://localhost:8000/docs](http://localhost:8000/docs).

### 3️⃣ Execute All Tasks
```bash
chmod +x run_all.sh
./run_all.sh
```
This runs every JSON task under `tasks/` using all agents.

---

## 🧩 Example Tasks

| Task File | Description | Example Result |
|------------|--------------|----------------|
| `SafariSearch.json` | Opens Safari and searches a query | ✅ Reward 1.5 |
| `NotesEntry.json` | Opens Notes and creates a new note | ✅ Reward 1.5 |
| `ToggleWiFi.json` | Toggles Wi-Fi ON/OFF | ✅ Reward 1.5 |

---

## 📂 Project Structure
```
ios_world_agents/
├── README.md
├── requirements.txt
├── run_all.sh
├── server.log
├── logs/
├── results/
│   ├── NotesEntry_openai.json
│   ├── SafariSearch_gemini.json
│   └── ToggleWiFi_grok.json
├── src/
│   ├── agent_openai.py
│   ├── agent_gemini.py
│   ├── agent_hf.py
│   ├── ios_simulator.py
│   ├── textgrad_opt.py
│   ├── evaluator.py
│   ├── api.py
│   ├── main.py
│   └── batch_analysis.py
└── tasks/
    ├── SafariSearch.json
    ├── NotesEntry.json
    └── ToggleWiFi.json
```

---

## 🧠 API Usage Example
Open your browser at **`http://localhost:8000/docs`**  
and execute:

```
GET /run_task
task=SafariSearch.json
agent=openai
model=gpt-4o-mini
textgrad=true
```

Expected Response (JSON):
```json
{
  "task": "SafariSearch.json",
  "agent": "openai",
  "reward": 1.5,
  "status": "completed"
}
```

---

## 📊 Reward Evaluation

Evaluate previously generated results:
```bash
python src/evaluator.py results/NotesEntry_openai.json
```

Batch evaluation:
```bash
python src/batch_analysis.py
```

---

## 🧪 Development Notes

- Developed & tested on **macOS Sequoia 14 + Python 3.13**  
- Uses FastAPI, Uvicorn, and Xcode simctl APIs  
- Supports both **command-line** and **Swagger UI** task execution  
- Designed for extension to multi-agent research on iOS platforms  

---

## 🐞 Troubleshooting

| Issue | Fix |
|-------|-----|
| `ModuleNotFoundError: No module named 'src'` | Run all commands from project root (`ios_world_agents/`). |
| `Address already in use` | Kill previous Uvicorn process: `lsof -i :8000` → `kill <PID>` |
| `Safari can’t open localhost:8000` | Ensure FastAPI server is running and reachable on `0.0.0.0`. |
| iOS Simulator not detected | Run `xcrun simctl list devices` and verify booted device. |

---

## 🧾 Citation
```
@misc{ios_world_agents_aryan2025,
  title={iOSWorld I3A (iOS-to-Action) Agent Evaluation Framework},
  author={Rishav Aryan},
  year={2025},
  url={https://github.com/RishavAr/ios_world_agents}
}
```

---

## 🧩 License
This project extends the AndroidWorld evaluation paradigm and follows the same open-source licensing terms.
