import onnx
import torch
from onnx2torch import convert

# Path to ONNX model
#onnx_model_path = "//NAS65A682/SD-Share/models/ESRGAN/4xNomos8kSCHAT-L.onnx"
onnx_model_path = "./4xNomos8kSCHAT-L.onnx"
# You can pass the path to the onnx model to convert it or...
torch_model_1 = convert(onnx_model_path)

# Or you can load a regular onnx model and pass it to the converter
#onnx_model = onnx.load(onnx_model_path)
#torch_model_2 = convert(onnx_model)