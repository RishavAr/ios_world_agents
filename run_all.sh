#!/bin/bash
# =========================================
# iOS Agents Live Runner (v3)
# =========================================
set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_DIR"

# ---- 1. Environment setup ----
export PYTHONPATH="$PROJECT_DIR"
if [ -d "venv" ]; then
  source venv/bin/activate
else
  echo "⚠️ No venv found. Please run: python3 -m venv venv && source venv/bin/activate"
  exit 1
fi

# ---- 2. Kill existing FastAPI servers ----
echo "🧹 Cleaning any existing FastAPI processes..."
kill $(lsof -t -i:8000) >/dev/null 2>&1 || true

# ---- 3. Start FastAPI in background ----
echo "🚀 Starting FastAPI backend..."
nohup uvicorn src.api:app --host 0.0.0.0 --port 8000 --reload > server.log 2>&1 &

# ---- 4. Wait for API readiness ----
echo "⌛ Waiting for FastAPI to start..."
until curl -s http://localhost:8000/docs >/dev/null; do
  sleep 1
done
echo "✅ FastAPI is live at http://localhost:8000/docs"

# ---- 5. Auto-run first task ----
SIM_NAME="iPhone 17 Pro"
echo "📱 Checking simulator..."
xcrun simctl bootstatus "$SIM_NAME" || {
  echo "⚠️ Booting simulator $SIM_NAME..."
  xcrun simctl boot "$SIM_NAME"
  sleep 5
}
echo "🧠 Running first agent task..."
curl -G "http://localhost:8000/run_task" \
  --data-urlencode "task=SafariSearch.json" \
  --data-urlencode "agent=openai" \
  --data-urlencode "model=gpt-4o" \
  --data-urlencode "textgrad=true"

# ---- 6. Open Safari ----
echo "🌐 Opening Safari to FastAPI Docs..."
open -a "Safari" "http://localhost:8000/docs"

echo "✅ All systems running. Logs: tail -f server.log"

