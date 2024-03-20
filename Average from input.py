#CS175L
#Kevin Gemian
#average from input
def main():
    num = 0
    lines = 0
    file = open('C:/Users/gemia/OneDrive/Desktop/CompSci saves/nums.txt', 'r')
    for line in file:
        num += float(line)
        lines += 1
        print(f'I read in {lines} number(s Current number is: {float(line):.2f} Total is: {num:.2f}')
        print(f'Average: {num/lines}')
if __name__ == '__main__':
    main()