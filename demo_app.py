import streamlit as st
import json, glob, os
import pandas as pd

st.set_page_config(page_title="iOS Agents Eval Dashboard", layout="wide")
st.title("📱 iOS Agent Evaluation – OpenAI vs Gemini vs Grok")

# Collect results
files = glob.glob("results/*.json")
if not files:
    st.info("⚡ Run `./run_all.sh` first to generate fresh results.")
    st.stop()

results = []
for file in files:
    with open(file) as f:
        data = json.load(f)
    task = data.get("task_name", os.path.basename(file).split("_")[0])
    agent = data.get("agent", os.path.basename(file).split("_")[1].split(".")[0])
    model = data.get("model", "")
    actions = data.get("actions", [])
    results.append({
        "Task": task,
        "Agent": agent,
        "Model": model,
        "Actions": "; ".join([str(a) for a in actions])
    })

df = pd.DataFrame(results)

# Group by task and show side-by-side comparison
for task, group in df.groupby("Task"):
    st.subheader(f"📌 Task: {task}")
    st.dataframe(
        group[["Agent", "Model", "Actions"]].set_index("Agent"),
        use_container_width=True
    )
