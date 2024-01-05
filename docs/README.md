```shell
# https://huggingface.co/yuvalkirstain/PickScore_v1
git lfs install
git clone https://huggingface.co/yuvalkirstain/PickScore_v1

ssh -T git@hf.co

sudo yum install git-lfs

git lfs install
git clone git@hf.co:yuvalkirstain/PickScore_v1
GIT_LFS_SKIP_SMUDGE=1 git clone git@hf.co:yuvalkirstain/PickScore_v1
git lfs fetch

https://huggingface.co/yuvalkirstain/PickScore_v1
https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K

git clone https://hf-mirror.com/yuvalkirstain/PickScore_v1
https://hf-mirror.com/yuvalkirstain/PickScore_v1

GIT_LFS_SKIP_SMUDGE=1 git clone https://hf-mirror.com/yuvalkirstain/PickScore_v1
# git lfs fetch
wget "https://hf-mirror.com/yuvalkirstain/PickScore_v1/resolve/main/model.safetensors?download=true"
wget "https://hf-mirror.com/yuvalkirstain/PickScore_v1/resolve/main/pytorch_model.bin?download=true"

GIT_LFS_SKIP_SMUDGE=1 git clone https://hf-mirror.com/laion/CLIP-ViT-H-14-laion2B-s32B-b79K
wget "https://hf-mirror.com/laion/CLIP-ViT-H-14-laion2B-s32B-b79K/resolve/main/open_clip_pytorch_model.bin?download=true"
wget "https://hf-mirror.com/laion/CLIP-ViT-H-14-laion2B-s32B-b79K/resolve/main/pytorch_model.bin?download=true"

pip install virtualenv -i https://pypi.tuna.tsinghua.edu.cn/simple/
virtualenv clip
# virtualenv --python /usr/local/webserver/python3.6/bin/python3.6 clip
# virtualenv --system-site-packages clip
source clip/bin/activate
deactivate

mkdir ~/.pip
vim ~/.pip/pip.conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com

pip install torch torchvision torchaudio -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install -e .

# Make sure you have git-lfs installed (https://git-lfs.com)
git lfs install
git clone https://huggingface.co/yuvalkirstain/PickScore_v1

# if you want to clone without large files – just their pointers
# prepend your git clone with the following env var:
GIT_LFS_SKIP_SMUDGE=1
```