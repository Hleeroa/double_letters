from decorators import time_wrapper


@ time_wrapper
def double_letters(string: str) -> str:
    stripped_str = list(string)
    for i in range(len(stripped_str)):
        stripped_str[i] = stripped_str[i]*2
    result = ''.join(stripped_str)
    return result


if __name__ == '__main__':
    double_letters('szxdcfvgbhn')
