import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    # Chuyển đổi đầu vào thành NumPy array để tính toán vector hóa
    x_arr = np.asarray(x, dtype=float)
    
    # Sử dụng np.where: nếu x >= 0 thì giữ nguyên x, ngược lại thì nhân với alpha
    return np.where(x_arr >= 0, x_arr, alpha * x_arr)
    pass