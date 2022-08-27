https://github.com/robbyrussell/oh-my-zsh
cai
https://github.com/robbyrussell/oh-my-zsh/wiki/Installing-ZSH
```
sudo apt install zsh
```
Tiep theo cai dat
```
curl -Lo install.sh https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh
sh install.sh
```
config zsh pyenv 
https://github.com/pyenv/pyenv-virtualenv/issues/233

I changed my ```~/.zshrc``` from:

```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
