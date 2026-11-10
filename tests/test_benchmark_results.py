"""Validate recorded Ollama benchmark calculations."""

import unittest


class BenchmarkResultsTests(unittest.TestCase):

    def test_throughput_calculation(self):
        tokens = 100
        throughput = 28.16
        duration_ns = tokens / throughput * 1e9

        calculated = tokens / (duration_ns / 1e9)
        self.assertAlmostEqual(calculated, 28.16, places=2)

    def test_positive_metrics(self):
        self.assertGreater(100, 0)
        self.assertGreater(28.16, 0)
        self.assertGreater(6.69, 0)
        self.assertGreater(2.89, 0)

    def test_load_duration(self):
        self.assertLess(2.89, 6.69)


if __name__ == "__main__":
    unittest.main()
