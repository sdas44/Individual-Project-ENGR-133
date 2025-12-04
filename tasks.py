"""
Course Number: ENGR 13300
Semester: e.g. Fall 2025

Description:
    This code contains the task class used to create the task objects for the to do list.
    

Assignment Information:
    Assignment:     Individual Project
    Team ID:        LC05 Team 5
    Author:         Samarth Das
    Date:           12/3/2025

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [X] understand the assignment expectations without
        telling me how they will approach it.
    [X] understand different ways to think about a solution
        without helping me plan my solution.
    [X] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""
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