import tempfile
import textwrap
import unittest
from pathlib import Path

from tools.validate_design_md import validate_design_md


def write_file(path, content):
    path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")


class TestValidateDesignMd(unittest.TestCase):
    def test_missing_front_matter_fails(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "design.md"
            write_file(
                path,
                """
                # Design

                ## Overview

                Example overview.
                """,
            )

            errors = validate_design_md(path)

        self.assertIn("Missing YAML front matter fences", errors)

    def test_out_of_order_sections_fail(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "design.md"
            write_file(
                path,
                """
                ---
                title: Example Design
                ---

                ## Typography

                Example typography.

                ## Overview

                Example overview.
                """,
            )

            errors = validate_design_md(path)

        self.assertIn(
            "Section order violation: Overview appears after Typography",
            errors,
        )

    def test_valid_subset_in_correct_order_passes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "design.md"
            write_file(
                path,
                """
                ---
                title: Example Design
                ---

                ## Overview

                Example overview.

                ## Typography

                Example typography.
                """,
            )

            errors = validate_design_md(path)

        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
