class tasks:
    def __init__(self, title, details, due_date):
        self.title = title
        self.details = details
        self.due_date = due_date
    
    def get_task_title(self):
        return self.title
    def get_task_details(self):
        return self.details
    def get_task_due_date(self):
        return self.due_date