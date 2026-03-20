def reverse_line(line: str) -> list[str]:
    line_split = line.split()
    line_split_reversed = line_split[::-1]
    return line_split_reversed


def main():
    line = input()
    line_reversed = reverse_line(line)
    print(*line_reversed)

if __name__ == '__main__':
    main()