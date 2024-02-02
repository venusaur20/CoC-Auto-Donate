import dxcam
from PIL import Image

camera = dxcam.create()
frame = camera.grab()
Image.fromarray(frame).show()