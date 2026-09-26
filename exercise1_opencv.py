import cv2
import numpy as np
from pathlib import Path

base_dir = Path(__file__).resolve().parent
image_dir = base_dir / 'images'
image_dir.mkdir(exist_ok=True)

input_path = image_dir / 'input.jpg'

if not input_path.exists():
    sample_image = np.zeros((220, 320, 3), dtype=np.uint8)
    sample_image[:] = 180
    cv2.rectangle(sample_image, (30, 30), (290, 180), (255, 255, 255), -1)
    cv2.circle(sample_image, (160, 100), 55, (0, 255, 0), -1)
    cv2.imwrite(str(input_path), sample_image)

image = cv2.imread(str(input_path))
if image is None:
    raise FileNotFoundError(f'Could not load image from {input_path}.')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_mask = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
blurred = cv2.blur(gray, (5, 5))

cv2.imwrite(str(image_dir / 'output_gray.jpg'), gray)
cv2.imwrite(str(image_dir / 'output_mask.jpg'), binary_mask)
cv2.imwrite(str(image_dir / 'output_blur.jpg'), blurred)

print('Image loaded and processed successfully.')
print(f'Saved: {image_dir / "output_mask.jpg"}')
