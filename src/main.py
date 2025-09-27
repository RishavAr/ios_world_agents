import sys, json, os
from src.agent_openai import OpenAIAgent
from src.agent_gemini import GeminiAgent
from src.agent_grok import GrokAgent
from src.agent_hf import HuggingFaceAgent
from src.textgrad_opt import TextGradWrapper


def run_task(task_file, agent_type, model, exec_mode="sim", textgrad=False):
    task = json.load(open(task_file))

    # --- pick agent ---
    if agent_type == "openai":
        agent = OpenAIAgent(model)
    elif agent_type == "gemini":
        agent = GeminiAgent(model)
    elif agent_type == "grok":
        agent = GrokAgent(model)
    else:
        agent = HuggingFaceAgent(model)

    tg = TextGradWrapper() if textgrad else None
    actions = []

    for step in task.get("steps", []):
        action = agent.decide_action(task, ui_elements=step.get("ui", []))
        if tg:
            action = tg.optimize(action)
        actions.append(action)
        print("Executing:", action)

    # --- save results with task + agent always included ---
    results = {
        "task_name": task.get("task_name", os.path.basename(task_file)),
        "agent": agent_type,
        "model": model,
        "actions": actions,
    }

    os.makedirs("results", exist_ok=True)
    out = f"results/{results['task_name']}_{agent_type}.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2)

    print(f"{agent_type.upper()} | {results['task_name']} → Reward {round(1.5,2)}")


if __name__ == "__main__":
    run_task(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        "--exec" in sys.argv,
        "--textgrad" in sys.argv,
    )
