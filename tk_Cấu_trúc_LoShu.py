def is_lo_shu(matrix):
    """Kiểm tra xem một danh sách 2 chiều có phải là ma trận Lo Shu hay không.

    Args:
        matrix: Danh sách 2 chiều biểu diễn ma trận.

    Returns:
        True nếu là ma trận Lo Shu, False nếu không.
    """

    # Kiểm tra kích thước
    if len(matrix) != 3 or len(matrix[0]) != 3:
        return False

    # Tính tổng mục tiêu (lấy tổng hàng đầu tiên)
    target_sum = sum(matrix[0])

    # Kiểm tra các số từ 1 đến 9
    numbers = set(sum(matrix, []))
    if numbers != set(range(1, 10)):
        return False

    # Kiểm tra tổng các hàng, cột và đường chéo
    for row in matrix:
        if sum(row) != target_sum:
            return False
    for col in zip(*matrix):  # Chuyển vị ma trận để kiểm tra cột
        if sum(col) != target_sum:
            return False
    # Kiểm tra đường chéo chính
    if sum(matrix[i][i] for i in range(3)) != target_sum:
        return False
    # Kiểm tra đường chéo phụ
    if sum(matrix[i][2-i] for i in range(3)) != target_sum:
        return False

    return True

# Ví dụ sử dụng
matrix = [[4, 9, 2],
          [3, 5, 7],
          [8, 1, 6]]

if is_lo_shu(matrix):
    print("Đây là ma trận Lo Shu")
else:
    print("Đây không phải là ma trận Lo Shu")