import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT / "Project 8 - Netflix"
NETFLIX_NOTEBOOK = PROJECT_ROOT / "project 8 - netflix.ipynb"

class NotebookRepositoryTests(unittest.TestCase):
    def test_all_eight_notebooks_are_valid_json(self):
        notebooks = list(ROOT.glob("Project */*.ipynb"))
        self.assertEqual(8, len(notebooks))
        for path in notebooks:
            with self.subTest(notebook=path.relative_to(ROOT)):
                json.loads(path.read_text(encoding="utf-8"))

    def test_project_1_to_7_csv_inputs_exist(self):
        for project_number in range(1, 8):
            folders = list(ROOT.glob(f"Project {project_number} -*"))
            self.assertEqual(1, len(folders))
            notebook_paths = list(folders[0].glob("*.ipynb"))
            self.assertEqual(1, len(notebook_paths))
            notebook = json.loads(notebook_paths[0].read_text(encoding="utf-8"))
            source = "\n".join(
                "".join(cell.get("source", []))
                for cell in notebook["cells"] if cell.get("cell_type") == "code"
            )
            refs = re.findall(r"read_csv\(\s*['\"]([^'\"]+\.csv)['\"]", source)
            for ref in refs:
                with self.subTest(project=project_number, csv=ref):
                    self.assertTrue((folders[0] / ref).is_file(), f"Missing CSV: {ref}")

    def test_netflix_missing_data_has_actionable_message(self):
        notebook = json.loads(NETFLIX_NOTEBOOK.read_text(encoding="utf-8"))
        source = "\n".join(
            "".join(cell.get("source", []))
            for cell in notebook["cells"] if cell.get("cell_type") == "code"
        )
        self.assertIn("DATA_CANDIDATES", source)
        self.assertIn("FileNotFoundError", source)
        self.assertIn("redistributed here", source)
        self.assertFalse((PROJECT_ROOT / "netflix.csv").exists())

if __name__ == "__main__":
    unittest.main()
