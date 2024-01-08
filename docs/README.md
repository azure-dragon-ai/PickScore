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

wget https://testing.ai-space.net/PickScore/yuvalkirstain/PickScore_v1/model.safetensors
wget https://testing.ai-space.net/PickScore/yuvalkirstain/PickScore_v1/pytorch_model.bin

GIT_LFS_SKIP_SMUDGE=1 git clone https://hf-mirror.com/laion/CLIP-ViT-H-14-laion2B-s32B-b79K
wget "https://hf-mirror.com/laion/CLIP-ViT-H-14-laion2B-s32B-b79K/resolve/main/open_clip_pytorch_model.bin?download=true"
wget "https://hf-mirror.com/laion/CLIP-ViT-H-14-laion2B-s32B-b79K/resolve/main/pytorch_model.bin?download=true"

wget https://testing.ai-space.net/PickScore/laion/CLIP-ViT-H-14-laion2B-s32B-b79K/open_clip_pytorch_model.bin
wget https://testing.ai-space.net/PickScore/laion/CLIP-ViT-H-14-laion2B-s32B-b79K/pytorch_model.bin

pip install virtualenv -i https://pypi.tuna.tsinghua.edu.cn/simple/
python -m venv venv
virtualenv clip
virtualenv score
# virtualenv --python /usr/local/webserver/python3.6/bin/python3.6 clip
# virtualenv --system-site-packages clip
source clip/bin/activate
score\Scripts\activate
deactivate

mkdir ~/.pip
vim ~/.pip/pip.conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com

pip install torch==2.0.1 --index-url https://download.pytorch.org/whl/cu118
pip install torch==2.1.1 torchaudio --index-url https://download.pytorch.org/whl/cu118

conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
pip install torch==2.1.1 torchvision torchaudio -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install torch==2.1.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install -e .

set DS_BUILD_AIO=0
set DS_BUILD_SPARSE_ATTN=O

set DS_BUILD_AIO=0 & set DS_BUILD_SPARSE_ATTN=O & pip install -r requirements.txt

pip install torch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 --index-url https://download.pytorch.org/whl/cu118

pip install pydantic==1.10.13 -i https://pypi.douban.com/simple

# Make sure you have git-lfs installed (https://git-lfs.com)
git lfs install
git clone https://huggingface.co/yuvalkirstain/PickScore_v1

# if you want to clone without large files – just their pointers
# prepend your git clone with the following env var:
GIT_LFS_SKIP_SMUDGE=1
```