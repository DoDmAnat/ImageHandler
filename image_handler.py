import cv2


def resize(image, size):
    return cv2.resize(image, size)


def adjust_brightness(image, alpha=1.0, beta=0.0):
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)


def binarize(image, threshold=128):
    _, image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return image


def invert(image):
    return cv2.bitwise_not(image)


def image_handler(image, pipeline):
    for operation in pipeline:
        if operation['name'] == 'resize':
            image = resize(image, operation['args']['size'])
        elif operation['name'] == 'adjust_brightness':
            image = adjust_brightness(image, alpha=operation['args']['alpha'], beta=operation['args']['beta'])
        elif operation['name'] == 'binarize':
            image = binarize(image, threshold=operation['args']['threshold'])
        elif operation['name'] == 'invert':
            image = invert(image)
        else:
            print(f"Unknown operation: {operation['name']}")
    return image
