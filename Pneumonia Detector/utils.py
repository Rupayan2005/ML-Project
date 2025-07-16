from PIL import ImageOps, Image
import numpy as np


def classify(image, model, class_names):
    # Convert Image to (224, 224)
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)

    # Convert Image to Numpy Array
    image_array = np.asarray(image)

    # Normalize Image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Set Model Input
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    # Make Prediction
    prediction = model.predict(data)
    #index = np.argmax(prediction)
    index = 0 if prediction[0][0] > 0.95 else 1
    class_name = class_names[index]
    confidence_score = float(prediction[0][index])

    return class_name, confidence_score