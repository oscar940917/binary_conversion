import sys
def main():
    try:
        input_data = sys.stdin.read()
        numbers = map(int, input_data.split())
        for number in numbers:
            print(bin(number)[2:])
    except Exception as e:
        print("發生錯誤：", e)
if __name__ == "__main__":
    main()
