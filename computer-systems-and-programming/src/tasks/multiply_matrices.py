def multiply_matrices(matrix1, matrix2):
    # Validate if multiplication is possible
    if len(matrix1[0]) != len(matrix2):
        print("Matrix multiplication is not possible!")
        return None

    # Calculate the product of matrix1 and matrix2
    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
    return result

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [1, 3, 2]
    ]
    matrix2 = [
        [1, 2, 3],
        [3, 4, 5],
        [5, 6, 7]
    ]

    print("Result of Matrix Multiplication:")
    result_matrix = multiply_matrices(matrix1, matrix2)
    if result_matrix:
        print_matrix(result_matrix)

if __name__ == "__main__":
    main()
