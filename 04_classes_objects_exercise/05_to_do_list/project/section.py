from .task import Task

class Section:
    def __init__(self, name: str):
        self.name = name
        self.task: list[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.task:
            return f"Task is already in the section {self.name}"
        self.task.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name:str):
        t = next((t for t in self.task if t.name == task_name), None)
        if t:
            t.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        task_len = len(self.task)
        self.task = [t for t in self.task if t.completed == False]
        return f"Cleared {task_len - len(self.task)} tasks."

    def view_section(self):
        tasks_formatted = '\n'.join([t.details() for t in self.task])
        return f"Section {self.name}:\n{tasks_formatted}"
