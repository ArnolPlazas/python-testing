import unittest

class AllAssertsTest(unittest.TestCase):
    def test_assert_equal(self):
        self.assertEqual(10, 10)
        self.assertEqual("Hola", "Hola")
    

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)


    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int('I am not a number')
    

    def test_assert_in(self):
        self.assertIn(10, [2, 4, 5, 10])
        self.assertNotIn(5, [2, 4, 10])
    

    def test_assert_dicts(self):
        user = {'first_name': 'Luis', 'last_name': 'Martinez'}
        self.assertDictEqual(
            {'first_name': 'Luis', 'last_name': 'Martinez'},
            user
        )
    

    def test_assert_sets(self):
        set_1 = {1, 2, 3}
        set_2 = {1, 2, 3}
        self.assertSetEqual(
            set_1,
            set_2
        )