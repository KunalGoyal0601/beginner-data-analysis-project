import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    1: ("Project 1 - Weather", "weather.csv"),
    2: ("Project 2 - Cars", "car.csv"),
    3: ("Project 3 - Police", "police.csv"),
    4: ("Project 4 - Covid19", "covid.csv"),
    5: ("Project 5 - London housing", "london.csv"),
    6: ("Project 6 - Census", "census.csv"),
    7: ("Project 7 - Udemy", "udemy.csv"),
}

class NotebookRepositoryTests(unittest.TestCase):
    def test_all_eight_notebooks_are_valid_json_and_have_no_saved_outputs(self):
        notebooks = list(ROOT.glob("Project */*.ipynb"))
        self.assertEqual(8, len(notebooks))
        for path in notebooks:
            with self.subTest(notebook=path.relative_to(ROOT)):
                notebook = json.loads(path.read_text(encoding="utf-8"))
                for cell in notebook["cells"]:
                    if cell.get("cell_type") == "code":
                        self.assertIsNone(cell.get("execution_count"))
                        self.assertFalse(cell.get("outputs"))

    def test_projects_1_to_7_use_local_data_with_clear_missing_file_error(self):
        for project, (folder_name, filename) in EXPECTED.items():
            folders = list(ROOT.glob(f"{folder_name}"))
            self.assertEqual(1, len(folders))
            notebook_paths = list(folders[0].glob("*.ipynb"))
            self.assertEqual(1, len(notebook_paths))
            notebook = json.loads(notebook_paths[0].read_text(encoding="utf-8"))
            source = "\n".join(
                "".join(cell.get("source", []))
                for cell in notebook["cells"] if cell.get("cell_type") == "code"
            )
            with self.subTest(project=project):
                self.assertIn("load_local_csv", source)
                self.assertIn("FileNotFoundError", source)
                self.assertIn("reuse terms have not been verified", source)
                self.assertFalse((folders[0] / filename).exists())

    def test_netflix_missing_data_has_actionable_message(self):
        path = ROOT / "Project 8 - Netflix" / "project 8 - netflix.ipynb"
        notebook = json.loads(path.read_text(encoding="utf-8"))
        source = "\n".join(
            "".join(cell.get("source", []))
            for cell in notebook["cells"] if cell.get("cell_type") == "code"
        )
        self.assertIn("DATA_CANDIDATES", source)
        self.assertIn("FileNotFoundError", source)
        self.assertIn("redistributed here", source)
        self.assertFalse((ROOT / "Project 8 - Netflix" / "netflix.csv").exists())

if __name__ == "__main__":
    unittest.main()
