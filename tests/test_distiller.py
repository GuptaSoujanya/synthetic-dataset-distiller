import unittest
from distiller.mutators import PromptMutator
from distiller.filters import QualityFilter

class TestDistiller(unittest.TestCase):
    def test_mutator(self):
        m = PromptMutator()
        self.assertIn("mathematical induction", m.deepen("Sort an array"))
    def test_filter(self):
        qf = QualityFilter()
        self.assertTrue(qf.evaluate("This is a clean, diverse sentence for testing distillation filters successfully.")["passed"])

if __name__ == "__main__":
    unittest.main()
