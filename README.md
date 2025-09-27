# iOS World Agents

End-to-end framework for evaluating LLM agents on simulated iOS tasks.

## Features
- OpenAI GPT-4o-mini agent
- HuggingFace agent (Mistral, LLaMA etc.)
- Reward evaluation (-0.05 per step, +0.2 per subgoal, +1.0 success)
- Safety constraints check
- TextGrad optimization for failed steps
- Batch analysis and report

## Run Example

```bash
export OPENAI_API_KEY="sk-xxxx"

python src/main.py tasks/wifi_toggle.json openai gpt-4o-mini
python src/main.py tasks/wifi_toggle.json hf mistralai/Mistral-7B-Instruct-v0.3
python src/batch_analysis.py
```
