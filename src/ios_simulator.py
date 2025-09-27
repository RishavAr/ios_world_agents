import os

class IOSSimulator:
    def execute(self, action):
        if action["action_type"] == "tap":
            if "Safari" in action["target"]:
                os.system("xcrun simctl launch booted com.apple.mobilesafari")
            elif "Notes" in action["target"]:
                os.system("xcrun simctl launch booted com.apple.mobilenotes")
            elif "Settings" in action["target"]:
                os.system("xcrun simctl launch booted com.apple.Preferences")
        elif action["action_type"] == "type":
            text = action.get("content", "")
            os.system(f"xcrun simctl io booted keyboard text '{text}'")
        elif action["action_type"] == "create_note":
            os.system("xcrun simctl launch booted com.apple.mobilenotes")
            text = action.get("content", "Agent-created note")
            os.system(f"xcrun simctl io booted keyboard text '{text}'")
        else:
            print(f"[Simulator] Unknown action: {action}")
