from user import User
from activity import Activity

class AnalyticsSystem:
    def __init__(self, users, activities):
        self.users = users
        self.activities = activities

    def add_user(self, user_id, User):
        users[user_id] = User
    def add_activity(self, action):
        activities.append(action)
    
    def get_user_activity_count(user_id):
        user_activiy = {}

