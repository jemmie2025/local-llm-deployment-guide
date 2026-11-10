import unittest

from scripts.throughput_estimates import (
    estimate_range, VRAM_BUDGET_GIB
)
from scripts.hardware_sizing import (
    weight_gib, planning_gib
)


class ThroughputEstimateTests(unittest.TestCase):

    def test_positive_range(self):
        low, high = estimate_range(5)
        self.assertGreater(low, 0)
        self.assertGreater(high, low)

    def test_larger_models_are_slower_in_model(self):
        small = estimate_range(4)
        large = estimate_range(8)
        self.assertGreater(small[0], large[0])

    def test_precision_affects_estimate(self):
        q4 = estimate_range(weight_gib(8, 4.8944))
        q8 = estimate_range(weight_gib(8, 8.5008))
        self.assertGreater(q4[0], q8[0])

    def test_oversized_configuration(self):
        weights = weight_gib(32, 8.5008)
        self.assertGreater(
            planning_gib(weights), VRAM_BUDGET_GIB
        )


if __name__ == "__main__":
    unittest.main()
