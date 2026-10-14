
import unittest
from contextlib import contextmanager
from unittest.mock import patch

from loguru import logger

from src.task import Task
from src.task_manager import add_task, delete_task


@contextmanager
def capture_logs(level="INFO"):
    """Capture Loguru messages for testing."""
    output = []
    handler_id = logger.add(
        lambda message: output.append(str(message).strip()),
        level=level,
        format="{level} | {message}"
    )
    try:
        yield output
    finally:
        logger.remove(handler_id)


class TestTaskLogging(unittest.TestCase):
    def setUp(self):
        self.tasks = []

    @patch("src.task_manager.save_tasks")
    def test_add_task_success_logging(self, mock_save):
        with capture_logs() as logs:
            result = add_task(
                self.tasks,
                "Homework",
                "Finish Python assessment",
                "20-10-2026"
            )

        self.assertTrue(result)
        self.assertIn("INFO | Task added: Homework", logs)
        mock_save.assert_called_once()

    @patch("src.task_manager.save_tasks")
    def test_duplicate_task_logging(self, mock_save):
        self.tasks.append(Task("Homework", "Existing", "20-10-2026"))

        with capture_logs() as logs:
            result = add_task(
                self.tasks,
                "Homework",
                "Duplicate task",
                "21-10-2026"
            )

        self.assertFalse(result)
        self.assertIn("WARNING | Duplicate task: Homework", logs)
        mock_save.assert_not_called()

    @patch("src.task_manager.save_tasks")
    def test_delete_task_success_logging(self, mock_save):
        self.tasks.append(Task("Homework", "Existing", "20-10-2026"))

        with capture_logs() as logs:
            result = delete_task(self.tasks, "Homework")

        self.assertTrue(result)
        self.assertIn("INFO | Task deleted: Homework", logs)
        mock_save.assert_called_once()

    @patch("src.task_manager.save_tasks")
    def test_delete_missing_task_logging(self, mock_save):
        with capture_logs() as logs:
            result = delete_task(self.tasks, "Missing")

        self.assertFalse(result)
        self.assertIn("WARNING | Task not found: Missing", logs)
        mock_save.assert_not_called()


if __name__ == "__main__":
    unittest.main()
