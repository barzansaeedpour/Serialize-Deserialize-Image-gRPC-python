import cv2
import image_message_pb2  # Import the generated Python module
import numpy as np

# Function to serialize image data into Protocol Buffers message
def serialize_image(image):
    message = image_message_pb2.ImageMessage()
    # Convert image to bytes and assign to the message
    _, img_bytes = cv2.imencode('.jpg', image)
    message.image_data = img_bytes.tobytes()
    return message.SerializeToString()

# Function to deserialize Protocol Buffers message into image data
def deserialize_image(serialized_data):
    message = image_message_pb2.ImageMessage()
    message.ParseFromString(serialized_data)
    # Convert bytes back to image
    nparr = np.frombuffer(message.image_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

# Example usage
image = cv2.imread('image.jpg')  # Load example image
serialized_data = serialize_image(image)  # Serialize image
deserialized_image = deserialize_image(serialized_data)  # Deserialize image

# Display deserialized image
cv2.imshow('Deserialized Image', deserialized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
