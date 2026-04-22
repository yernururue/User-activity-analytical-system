from collections import Counter

class User:
    def __init__(self, user_id, actions):
        self.user_id = user_id
        self.actions = actions
    
    counter = Counter(actions)
    
    
    def add_action(self, action):
        self.actions.append(action)
    def get_actions_count(self):
        return len(self.actions)
    def get_most_common_action(self):
        most_common_action = counter.most_common(1)[0][0]
        return most_common_action