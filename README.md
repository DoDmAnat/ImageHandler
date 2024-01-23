# ImageHandler

## Пример использования

```python
import cv2
# импортировать обработчик
from image_handler import image_handler

image: np.ndarray = {изображение в формате np.ndarray}

# Пример пайплайна предобработки
sample_pipeline = [
    {'name': 'resize', 'args': {'size': (500, 100)}},
    {'name': 'adjust_brightness', 'args': {'alpha': 1.5, 'beta': 10}},
    {'name': 'binarize', 'args': {'threshold': 70, 'type': cv2.THRESH_BINARY}},
    {'name': 'invert'}
]
# Если нужны не все операции
sample_pipeline = [
    {'name': 'resize', 'args': {'size': (500, 100)}},
    {'name': 'invert'}
]

# Вернется обработанное изображение в формате np.ndarray
processed_real_image = image_handler(image, sample_pipeline)

```
