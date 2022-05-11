import io
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import torch
from PIL import Image
from torchvision import transforms
import torchvision.models as models

# model = torch.hub.load('pytorch_vision_v0.10.0/', 'resnet50', pretrained=True, source='local')
# model = torch.hub.load('pytorch_vision_v0.10.0/', 'resnet50', source='local', force_reload=True)

model = models.resnet50()
ckpt = torch.load('checkpoints/resnet50-0676ba61.pth')
model.load_state_dict(ckpt)
model.eval()

def validate(input_image):
    # input_image = Image.open(filename).convert('RGB')
    preprocess = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)  # create a mini-batch as expected by the model

    with torch.no_grad():
        output = model(input_batch)
    probabilities = torch.nn.functional.softmax(output[0], dim=0)

    # Read the categories
    with open("imagenet_classes.txt", "r") as f:
        categories = [s.strip() for s in f.readlines()]
    # Show top categories per image
    top5_prob, top5_catid = torch.topk(probabilities, 1)
    for i in range(top5_prob.size(0)):
        # print(categories[top5_catid[i]], top5_prob[i].item())
        temp = [str(categories[top5_catid[i]]), str(top5_prob[i].item())]
        return temp

def handle(req: bytes) -> str:
    # input_image = Image.frombytes(req).convert('RGB')
    input_image = Image.open(io.BytesIO(req)).convert('RGB')
    return validate(input_image)[0]

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     import PIL.Image as Image
#     pil_im = Image.open("temp/temp_img").convert('RGB')
#     b = io.BytesIO()
#     pil_im.save(b, 'jpeg')
#     im_bytes = b.getvalue()
#     print(handle(im_bytes))


