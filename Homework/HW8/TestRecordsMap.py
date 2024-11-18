import unittest

from RecordsMap import LocalRecord, RecordsMap


class TestLocalRecord(unittest.TestCase):
    def test_init(self):
        """Test initialization of LocalRecord"""
        record = LocalRecord((41.806310, -72.248737))
        self.assertEqual(record.pos, (42.0, -72.0))
        self.assertIsNone(record.max)
        self.assertIsNone(record.min)

    def test_hash(self):
        """Test hash function of LocalRecord"""
        record1 = LocalRecord((41.806310, -72.248737))
        record2 = LocalRecord((41.906310, -72.348737))
        self.assertEqual(hash(record1), hash(record2))

    def test_eq(self):
        """Test equality of LocalRecord"""
        record1 = LocalRecord((41.806310, -72.248737))
        record2 = LocalRecord((41.804310, -72.247737))
        record3 = LocalRecord((41.506310, -72.848737))
        self.assertTrue(record1 == record2)
        self.assertFalse(record1 == record3)

    def test_add_report(self):
        """Test adding temperature reports to LocalRecord"""
        record = LocalRecord((41.806310, -72.248737))
        record.add_report(25)
        self.assertEqual(record.max, 25)
        self.assertEqual(record.min, 25)
        record.add_report(30)
        self.assertEqual(record.max, 30)
        self.assertEqual(record.min, 25)
        record.add_report(20)
        self.assertEqual(record.max, 30)
        self.assertEqual(record.min, 20)


class TestRecordsMap(unittest.TestCase):
    def test_add_one_report(self):
        """Test adding a single report to RecordsMap"""
        rm = RecordsMap()
        p1 = (41.806310, -72.248737)
        self.assertFalse(p1 in rm)
        rm.add_report(p1, 25)
        self.assertTrue(p1 in rm)
        self.assertEqual(len(rm), 1)
        self.assertEqual(rm[p1], (25, 25))

    def test_add_many_reports(self):
        """Test adding multiple reports to RecordsMap"""
        rm = RecordsMap()
        p1 = (41.806310, -72.248737)
        # rounds to the same as p1
        p2 = (41.804310, -72.247737)
        # rounds to different than p1
        p3 = (41.506310, -72.848737)
        rm.add_report(p1, 25)
        rm.add_report(p2, 30)
        rm.add_report(p3, 20)
        self.assertTrue(p1 in rm)
        self.assertTrue(p2 in rm)
        self.assertTrue(p3 in rm)
        self.assertEqual(len(rm), 2)
        self.assertEqual(rm[p1], (25, 30))
        self.assertEqual(rm[p3], (20, 20))


if __name__ == '__main__':
    unittest.main()
