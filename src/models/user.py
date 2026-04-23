from collections import Counter

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    def get_actions_count(self):
        counts = {}
        for action in self.actions:
            counts[action] = counts.get(action,0)+1
        return counts

    def get_most_common_action(self):
        if not self.actions:
            return None
        counts = Counter(actions)
        return counts.most_common(1)[0]


        
       