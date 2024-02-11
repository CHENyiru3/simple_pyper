from typing import NewType

数字 = NewType('数字', float)
文件路径 = NewType('文件路径', str)
def plus(A,B):
    c = A+B
    return c

def main(inputas_A:数字,inputas_B:数字,outputas_C:文件路径):
    inputas_A = float(inputas_A)
    inputas_B = float(inputas_B)
    result = plus(inputas_A,inputas_B)
    with open(outputas_C, "w") as file:
        file.write(str(result))

if __name__ == "__main__":
    import sys
    main(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3])
