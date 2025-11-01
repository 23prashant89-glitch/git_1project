"""Package exports for task_manager.

Expose the main functions so tests and external imports can do
``from task_manager import add_task, remove_tasks, load_tasks, list_tasks, TASKS_FILE``.
"""

from .task_manager import add_task, remove_tasks, load_tasks, list_tasks, TASKS_FILE

__all__ = [
	"add_task",
	"remove_tasks",
	"load_tasks",
	"list_tasks",
	"TASKS_FILE",
]
