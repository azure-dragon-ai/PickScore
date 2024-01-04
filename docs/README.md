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

# Make sure you have git-lfs installed (https://git-lfs.com)
git lfs install
git clone https://huggingface.co/yuvalkirstain/PickScore_v1

# if you want to clone without large files – just their pointers
# prepend your git clone with the following env var:
GIT_LFS_SKIP_SMUDGE=1
```