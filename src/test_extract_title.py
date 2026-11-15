import unittest
from extract_title import extract_title


class TestExctractTitle(unittest.TestCase):
    def test_no_title(self):
        md = """
        ```
        This is text that _should_ remain
        the **same** even with inline stuff
        ```
        """
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertEqual(str(context.exception), "No title found")

    def test_title1(self):
        md = """
  # Hello! Here's the title
  Bla-bla-bla
"""
        self.assertEqual(extract_title(md), "Hello! Here's the title")

    def test_title2(self):
        md = """
        Bla-bla-bla
      #### Hello! Here's another title
      # WoW!
      Bla-bla-bla
    """
        self.assertEqual(extract_title(md), "WoW!")
