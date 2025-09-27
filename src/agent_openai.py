class OpenAIAgent:
    def __init__(self, model):
        self.model = model
    def decide_action(self, task, ui_elements=None, memory=""):
        return {"action_type": "tap", "target": task["goal"]}
