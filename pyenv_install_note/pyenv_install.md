## Step 1 install lib
###  Make sure to follow this guidance for your platform before any troubleshooting.

Ubuntu/Debian:

```shell

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

```

Alternative of libreadline-dev:

```shell

sudo apt install libedit-dev

```

[follow link](https://github.com/pyenv/pyenv/wiki/Common-build-problems)

## step 2

 
install 

```shell 

curl https://pyenv.run | bash
```
chú ý cần thêm đoạn code sau vào trong file bên dưới 
# Load pyenv automatically by adding
# the following to ```~/.bashrc```:
```
export PATH="/home/sonnh/.pyenv/bin:$PATH"
eval "$(pyenv init -)"1
eval "$(pyenv virtualenv-init -)"
```

```shell
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```


