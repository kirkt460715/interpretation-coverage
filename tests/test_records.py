import unittest
from pathlib import Path

from src.records import load_records


class RecordInputTests(unittest.TestCase):
    def test_synthetic_service_data_are_readable(self):
        root = Path(__file__).resolve().parents[1]
        data = load_records(root / "data" / "service.json")
        self.assertEqual(data["format_version"], 1)
        self.assertGreater(len(data["requests"]), 0)


if __name__ == "__main__":
    unittest.main()
