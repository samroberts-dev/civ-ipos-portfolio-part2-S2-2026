import unittest
from unittest.mock import patch
from io import StringIO

from src.task import Task
from src.task_manager import list_tasks


class TestRichDisplay(unittest.TestCase):

    def setUp(self):
        self.tasks = [
            Task("Homework", "Finish python", "12-10-2026"),
            Task("Shopping", "Buy a t-shirt", "14-10-2026")
        ]

    def test_table_headers(self):
        with patch("sys.stdout", new_callable=StringIO) as output:
            list_tasks(self.tasks)

        result = output.getvalue()

        self.assertIn("Title", result)
        self.assertIn("Description", result)
        self.assertIn("Due Date", result)
        self.assertIn("Status", result)

    def test_table_borders(self):
        with patch("sys.stdout", new_callable=StringIO) as output:
            list_tasks(self.tasks)

        result = output.getvalue()

        self.assertIn("┏", result)
        self.assertIn("┓", result)

    def test_table_information(self):
        with patch("sys.stdout", new_callable=StringIO) as output:
            list_tasks(self.tasks)

        result = output.getvalue()

        self.assertIn("Homework", result)
        self.assertIn("Shopping", result)
        self.assertIn("12-10-2026", result)

    def test_empty_task_list(self):
        with patch("sys.stdout", new_callable=StringIO) as output:
            list_tasks([])

        self.assertIn("No tasks found.", output.getvalue())

    def test_status_filtering(self):
        self.tasks[1].status = "completed"

        with patch("sys.stdout", new_callable=StringIO) as output:
            list_tasks(self.tasks, status="completed")

        result = output.getvalue()

        self.assertIn("Shopping", result)
        self.assertNotIn("Homework", result)


if __name__ == '__main__':
    unittest.main()
