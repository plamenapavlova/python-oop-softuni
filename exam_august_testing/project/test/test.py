from project.wearable_device import WearableDevice

import unittest



class WearableDeviceInitTests(unittest.TestCase):
    def test_constructor_sets_all_provided_fields_correctly(self):
        device = WearableDevice(
            model ="Galaxy Watch",
            cost= 250.0,
            resolution = (450, 450),
            is_operating= False,
            battery_life =40,
        )

        self.assertEqual("Galaxy Watch", device.model)
        self.assertEqual(250.0, device.cost)
        self.assertEqual((450, 450), device.resolution)
        self.assertFalse(device.is_operating)
        self.assertEqual(40, device.battery_life)

    def test_constructor_default_is_operating_is_true(self):
        device = WearableDevice("Galaxy Watch", 250.0, (450, 450))

        self.assertTrue(device.is_operating)

    def test_constructor_default_battery_life_is_none(self):
        device = WearableDevice("Galaxy Watch", 250.0, (450, 450))

        self.assertIsNone(device.battery_life)

    def test_constructor_with_invalid_model_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            WearableDevice("", 250.0, (450, 450))

        self.assertEqual(
            "Model must be a non-empty string up to 40 characters!",
            str(context.exception),
        )

    def test_constructor_with_invalid_cost_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            WearableDevice("Galaxy Watch", 0.5, (450, 450))

        self.assertEqual("Cost must be at least 1.0!", str(context.exception))

    def test_constructor_with_invalid_resolution_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            WearableDevice("Galaxy Watch", 250.0, (450, 450, 10))

        self.assertEqual(
            "Resolution must be a tuple of (width, height)!",
            str(context.exception),
        )

    def test_constructor_with_invalid_battery_life_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            WearableDevice("Galaxy Watch", 250.0, (450, 450), battery_life=150)

        self.assertEqual(
            "Battery life must be between 0 and 100 hours!",
            str(context.exception),
        )


class WearableDeviceModelPropertyTests(unittest.TestCase):
    def setUp(self):
        self.device = WearableDevice("Galaxy Watch", 250.0, (450, 450))

    def test_set_valid_model(self):
        self.device.model = "Apple Watch"

        self.assertEqual("Apple Watch", self.device.model)

    def test_set_model_at_max_length_boundary_does_not_raise(self):
        model_at_boundary = "A" * 40

        self.device.model = model_at_boundary

        self.assertEqual(model_at_boundary, self.device.model)

    def test_set_model_over_max_length_raises_value_error(self):
        model_over_boundary = "A" * 41

        with self.assertRaises(ValueError) as context:
            self.device.model = model_over_boundary

        self.assertEqual(
            "Model must be a non-empty string up to 40 characters!",
            str(context.exception),
        )

    def test_set_empty_model_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.device.model = ""

    def test_set_whitespace_only_model_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.device.model = "     "

    def test_set_model_is_stored_unstripped(self):
        self.device.model = "  Pixel Watch  "

        self.assertEqual("  Pixel Watch  ", self.device.model)


class WearableDeviceCostPropertyTests(unittest.TestCase):
    def setUp(self):
        self.device = WearableDevice("Galaxy Watch", 250.0, (450, 450))

    def test_set_valid_cost(self):
        self.device.cost = 99.99

        self.assertEqual(99.99, self.device.cost)

    def test_set_cost_at_minimum_boundary_does_not_raise(self):
        self.device.cost = 1.0

        self.assertEqual(1.0, self.device.cost)

    def test_set_cost_below_minimum_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.device.cost = 0.99

        self.assertEqual("Cost must be at least 1.0!", str(context.exception))

    def test_set_negative_cost_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.device.cost = -20.0


class WearableDeviceResolutionPropertyTests(unittest.TestCase):
    def setUp(self):
        self.device = WearableDevice("Galaxy Watch", 250.0, (450, 450))

    def test_set_valid_resolution(self):
        self.device.resolution = (100, 200)

        self.assertEqual((100, 200), self.device.resolution)

    def test_set_resolution_with_too_few_elements_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.device.resolution = (100,)

        self.assertEqual(
            "Resolution must be a tuple of (width, height)!",
            str(context.exception),
        )

    def test_set_resolution_with_too_many_elements_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.device.resolution = (100, 200, 300)

    def test_set_resolution_with_zero_dimension_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.device.resolution = (0, 200)

        self.assertEqual(
            "Resolution dimensions must be positive integers!",
            str(context.exception),
        )

    def test_set_resolution_with_negative_dimension_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.device.resolution = (100, -200)

    def test_set_resolution_with_smallest_positive_dimensions_does_not_raise(self):
        self.device.resolution = (1, 1)

        self.assertEqual((1, 1), self.device.resolution)


class WearableDeviceBatteryLifePropertyTests(unittest.TestCase):
    def setUp(self):
        self.device = WearableDevice("Galaxy Watch", 250.0, (450, 450))

    def test_set_valid_battery_life(self):
        self.device.battery_life = 55

        self.assertEqual(55, self.device.battery_life)

    def test_set_battery_life_to_none_is_allowed(self):
        self.device.battery_life = None

        self.assertIsNone(self.device.battery_life)

    def test_set_battery_life_at_lower_boundary_does_not_raise(self):
        self.device.battery_life = 0

        self.assertEqual(0, self.device.battery_life)

    def test_set_battery_life_at_upper_boundary_does_not_raise(self):
        self.device.battery_life = 100

        self.assertEqual(100, self.device.battery_life)

    def test_set_battery_life_below_lower_boundary_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.device.battery_life = -1

        self.assertEqual(
            "Battery life must be between 0 and 100 hours!",
            str(context.exception),
        )

    def test_set_battery_life_above_upper_boundary_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.device.battery_life = 101


class WearableDeviceGetOperationalStatusTests(unittest.TestCase):
    def test_get_operational_status_when_operating(self):
        device = WearableDevice("Galaxy Watch", 250.0, (450, 450), is_operating=True)

        result = device.get_operational_status()

        self.assertEqual("Model: Galaxy Watch is currently operational.", result)

    def test_get_operational_status_when_not_operating(self):
        device = WearableDevice("Galaxy Watch", 250.0, (450, 450), is_operating=False)

        result = device.get_operational_status()

        self.assertEqual("Model: Galaxy Watch is currently not operational.", result)


class WearableDeviceGetInfoTests(unittest.TestCase):
    def test_get_info_with_known_battery_life(self):
        device = WearableDevice("Galaxy Watch", 250.0, (450, 400), battery_life=36)

        result = device.get_info()

        self.assertEqual(
            "Galaxy Watch display resolution: 450x400 pixels | Battery life: 36h",
            result,
        )

    def test_get_info_with_unknown_battery_life(self):
        device = WearableDevice("Galaxy Watch", 250.0, (450, 400), battery_life=None)

        result = device.get_info()

        self.assertEqual(
            "Galaxy Watch display resolution: 450x400 pixels | Battery life: unknown",
            result,
        )


if __name__ == "__main__":
    unittest.main()
