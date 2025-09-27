class Evaluator:
    def __init__(self):
        self.step_penalty=-0.05; self.subgoal_reward=0.2; self.success_reward=1.0
    def score(self,steps,achieved,total):
        return steps*self.step_penalty+achieved*self.subgoal_reward+(self.success_reward if achieved==total else 0)
    def safety_check(self,action,constraints):
        for bad in constraints:
            if bad.lower() in str(action).lower():
                return False,f"Violation: {bad}"
        return True,None
