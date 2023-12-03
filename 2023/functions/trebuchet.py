from typing import Optional


def is_number(input_char: str) -> bool:
    return input_char.isdigit()


def calibrate(input_str: str):
    first_digit = find_first_digit(input_str)
    second_digit = find_first_digit(input_str[::-1])
    return int(first_digit + second_digit)


def find_first_digit(input_str: str) -> Optional[str]:
    for i in input_str:
        if is_number(i):
            return i
    return None


def get_calibration_value(file_name: str) -> int:
    calibration_value = 0
    with open(file_name, 'r') as file:
        for line in file:
            calibration_value += calibrate(line)
    return calibration_value


if __name__ == '__main__':
    file_name = "input"
    calibration = get_calibration_value(file_name)
    print(calibration)