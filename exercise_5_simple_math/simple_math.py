"""
    example input:
    What is the first number: 10
    What is the second number: 5
    example output:

    10 + 5 = 15
    10 - 5 = 5
    10 * 5 = 50
    10 / 5 = 2
"""

from dataclasses import dataclass


@dataclass
class Inputs:
    first_number: float
    second_number: float


def get_inputs() -> Inputs:
    while True:
        try:
            first_number = float(input("What is the first number: "))
            second_number = float(input("What is the second number: "))
            return Inputs(
                first_number=float(first_number),
                second_number=float(second_number),
            )
        except ValueError:
            print("Invalid input. Please try again!")


def display_outputs(inputs: Inputs) -> None:
    print(
        f"{inputs.first_number} + {inputs.second_number} = {inputs.first_number+inputs.second_number}"
    )
    print(
        f"{inputs.first_number} - {inputs.second_number} = {inputs.first_number-inputs.second_number}"
    )
    print(
        f"{inputs.first_number} * {inputs.second_number} = {inputs.first_number*inputs.second_number}"
    )
    print(
        f"{inputs.first_number} / {inputs.second_number} = {inputs.first_number/inputs.second_number}"
    )


if __name__ == "__main__":
    inputs = get_inputs()
    display_outputs(inputs=inputs)
