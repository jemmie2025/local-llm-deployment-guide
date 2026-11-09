import unittest
from scripts.hardware_sizing import (
    BITS, MODELS, weight_gib, planning_gib
)


class HardwareSizingTests(unittest.TestCase):

    def test_positive_weight_estimate(self):
        self.assertGreater(weight_gib(8, BITS["Q4_K_M"]), 0)

    def test_quantization_order(self):
        values = [weight_gib(8, bits) for bits in BITS.values()]
        self.assertEqual(values, sorted(values))

    def test_parameter_scaling(self):
        self.assertGreater(
            weight_gib(13, BITS["Q4_K_M"]),
            weight_gib(7, BITS["Q4_K_M"])
        )

    def test_planning_headroom(self):
        self.assertGreater(planning_gib(5), 5)

    def test_configuration_count(self):
        self.assertEqual(len(MODELS) * len(BITS), 20)


if __name__ == "__main__":
    unittest.main()
