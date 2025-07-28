from collections import defaultdict
from typing import List, Optional


class TaskTrackingSystem:
    def __init__(self):
        self.tasks = {}
        self.task_attributes = defaultdict(dict)
        # values are tasks that depend of key aka task
        self.dependent_tasks = {}
        # values tasks that key depends on
        self.reverse_dependencies = {}

    def add_task(self, task_id: str, title: str, description: str, status: str, priority: int) -> bool:
        if task_id in self.tasks:
            return False
        self.tasks[task_id] = True
        self.task_attributes[task_id] = {
            'title': title,
            'description': description,
            'status': status,
            'priority': priority
        }
        return True

    def update_task(self, task_id: str, title: Optional[str] = None, description: Optional[str] = None,
                    status: Optional[str] = None, priority: Optional[int] = None) -> bool:
        if task_id not in self.tasks:
            return False
        if title is not None:
            self.task_attributes[task_id]['title'] = title
        if description is not None:
            self.task_attributes[task_id]['description'] = description
        if status is not None:
            self.task_attributes[task_id]['status'] = status
        if priority is not None:
            self.task_attributes[task_id]['priority'] = priority
        return True

    def __update_dependency(self, task_id: str, status: str) -> None:
        if "Closed" == status and self.dependent_tasks.get(task_id) is not None:
            self.__update_dependency(task_id, status)
            for dependent_task_id in self.reverse_dependencies.get(task_id, []):
                self.update_task(dependent_task_id, status="Open")

    def remove_task(self, task_id: str) -> bool:
        if task_id in self.tasks:
            del self.tasks[task_id]
            del self.task_attributes[task_id]
            self.__remove_alldependencies(task_id)
            return True
        return False

    def __remove_alldependencies(self, task_id: str) -> None:
        if self.dependent_tasks.get(task_id) is not None:
            del self.dependent_tasks[task_id]
        for _, task_dependency in self.dependent_tasks:
            if task_id in task_dependency:
                task_dependency.remove(task_id)

    def get_tasks_by_status(self, status: str) -> List[str]:
        return sorted([task_id for task_id, attrs in self.task_attributes.items() if attrs['status'] == status])

    def get_tasks_by_priority(self, priority: int) -> List[str]:
        return sorted([task_id for task_id, attrs in self.task_attributes.items() if attrs['priority'] == priority])

    # task_id depends on dependency_task_id
    def add_dependency(self, task_id: str, dependency_task_id: str) -> bool:
        if self.dependent_tasks.get(dependency_task_id) is None:
            self.dependent_tasks[dependency_task_id] = []
        # avoid circular dependency
        if dependency_task_id in self.get_dependent_tasks(task_id):
            return False

        if self.reverse_dependencies.get(task_id) is None:
            self.reverse_dependencies[task_id] = []
        self.reverse_dependencies[task_id].append(dependency_task_id)
        self.dependent_tasks[dependency_task_id].append(task_id)
        return True

    def remove_dependency(self, task_id: str, dependency_task_id: str) -> bool:
        dependent_tasks = self.get_dependent_tasks(dependency_task_id)
        if dependent_tasks:
            del dependent_tasks[dependent_tasks.index(task_id)]
            self.reverse_dependencies.get(dependency_task_id, []).remove(task_id)
            return True
        else:
            return False

    def get_dependent_tasks(self, task_id: str) -> List[str]:
        return list(self.dependent_tasks.get(task_id, []))