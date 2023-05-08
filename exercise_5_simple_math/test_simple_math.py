from simple_math import Inputs, display_outputs


def test_display_outputs(capsys):
    inputs = Inputs(first_number=10.0, second_number=5.0)
    expected_output = (
        "10.0 + 5.0 = 15.0\n"
        "10.0 - 5.0 = 5.0\n"
        "10.0 * 5.0 = 50.0\n"
        "10.0 / 5.0 = 2.0\n"
    )
    display_outputs(inputs)
    captured = capsys.readouterr()
    assert captured.out == expected_output
