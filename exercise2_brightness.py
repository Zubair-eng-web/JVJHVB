import numpy as np


def adjust_brightness_contrast(image_array, alpha=1.0, beta=0):
    adjusted = image_array.astype(np.float32) * alpha + beta
    return np.clip(adjusted, 0, 255).astype(np.uint8)


gray_example = np.array([[100, 150], [200, 50]], dtype=np.uint8)
result = adjust_brightness_contrast(gray_example, alpha=1.5, beta=-20)

print('Original array:')
print(gray_example)
print('\nAdjusted array:')
print(result)
