import unittest

from mad_lib import MadLibInput, Response, make_mad_lib


class TestMadLib(unittest.TestCase):
    def test_make_mad_lib(self):
        test_cases = [
            (
                MadLibInput(
                    noun="cat", verb="sleeps", adjective="fluffy", adverb="happily"
                ),
                Response(output="So the fluffy cat sleeps happily,"),
            ),
            (
                MadLibInput(
                    noun="dog", verb="barks", adjective="loud", adverb="suddenly"
                ),
                Response(output="So the loud dog barks suddenly,"),
            ),
            (
                MadLibInput(
                    noun="bird", verb="sings", adjective="beautiful", adverb="sweetly"
                ),
                Response(output="So the beautiful bird sings sweetly,"),
            ),
        ]

        for input_data, expected_output in test_cases:
            with self.subTest(input_data=input_data):
                result = make_mad_lib(input_data)
                self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
