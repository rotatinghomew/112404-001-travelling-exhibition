from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from museum_workbench.inputs import read_table


class MaterialTests(unittest.TestCase):
    def test_tables_have_rows_and_uniform_record_fields(self):
        paths = sorted((ROOT / 'data').glob('*.csv'))
        self.assertGreaterEqual(len(paths), 3)
        for path in paths:
            with self.subTest(table=path.name):
                rows = read_table(path)
                self.assertTrue(rows)
                self.assertTrue(all(all(isinstance(v, str) for v in row.values()) for row in rows))
                self.assertEqual(set(rows[0]), set(rows[-1]))
                self.assertTrue(all(any(value.strip() for value in row.values()) for row in rows))

    def test_scenario_materials_have_resolvable_business_references(self):
        venues = read_table(ROOT / "data/venues.csv")
        works = read_table(ROOT / "data/works.csv")
        loans = read_table(ROOT / "data/loan_windows.csv")
        attendance = read_table(ROOT / "data/attendance_history.csv")
        self.assertTrue({row["venue_id"] for row in attendance} <= {row["venue_id"] for row in venues})
        self.assertTrue({row["work_id"] for row in loans} <= {row["work_id"] for row in works})
        self.assertTrue(any(row["approval_state"] != "approved" for row in loans))

    def test_dates_and_identifiers_remain_strings(self):
        for path in (ROOT / 'data').glob('*.csv'):
            rows = read_table(path)
            self.assertTrue(all(isinstance(value, str) for row in rows for value in row.values()))


if __name__ == '__main__':
    unittest.main()
