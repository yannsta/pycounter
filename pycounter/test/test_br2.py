from pycounter import pycounter
import unittest
import os

class ParseExample(unittest.TestCase):
    def setUp(self):
        self.report = pycounter.parse(os.path.join(os.path.dirname(__file__),
                                                             'data/simpleBR2.csv'))

    def test_reportname(self):
        self.assertEqual(self.report.report_type, u'BR2')
        self.assertEqual(self.report.report_version, 1)

    def test_year(self):
        self.assertEqual(self.report.year, 2012)

    def test_platform(self):
        for publication in self.report:
            self.assertEqual(publication.publisher, u"John Wiley and Sons")
            self.assertEqual(publication.platform, u"Wiley Online Library")

    def test_stats(self):
        publication = self.report.pubs[0]
        self.assertEqual(publication.monthdata, [0, 25, 0, 0, 0, 0, None, None, None, None, None, None])

class ParseCounter4Example(unittest.TestCase):
    def setUp(self):
        self.report = pycounter.parse(os.path.join(os.path.dirname(__file__),
                                                             'data/C4BR2.tsv'))

    def test_reportname(self):
        self.assertEqual(self.report.report_type, u'BR2')
        self.assertEqual(self.report.report_version, 4)

    def test_year(self):
        self.assertEqual(self.report.year, 2012)

    def test_platform(self):
        for publication in self.report:
            self.assertEqual(publication.publisher, u"John Wiley and Sons")
            self.assertEqual(publication.platform, u"Wiley Online Library")

    def test_stats(self):
        publication = self.report.pubs[0]
        self.assertEqual(publication.monthdata, [0, 25, 0, 0, 0, 0, None, None, None, None, None, None])
