
from contextlib import contextmanager
import unittest
from loguru import logger

@contextmanager
def capture_logs(level="INFO", format="{level} | {message}"):
    """
    Capture loguru-based logs into a list.
    """
    output = []
    handler_id = logger.add(
        lambda msg: output.append(str(msg).strip()),
        level=level,
        format=format
    )
    try:
        yield output
    finally:
        logger.remove(handler_id)


def do_some_logging():
    logger.info('User added a task successfully.')
    logger.error('Failed to connect to list.')


class TestMyLogger(unittest.TestCase):
    def test_do_some_logging(self):
        with capture_logs(level="INFO") as logs:
            do_some_logging()

        self.assertIn("INFO | User added a task successfully.", logs)
        self.assertIn("ERROR | Failed to connect to list.", logs)


if __name__ == '__main__':
    unittest.main()
