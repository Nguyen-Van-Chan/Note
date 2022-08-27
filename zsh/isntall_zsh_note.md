## step 1

```shell
	sudo apt-get install zsh
```

## step 2

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```


## isue zsh with pyenv 
I have the same issue.
My ~/.zshenv file:

https://github.com/pyenv/pyenv-virtualenv/issues/233

```shell
export PYENV_ROOT="$HOME"/.pyenv
export PATH="$PYENV_ROOT"/bin:"$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
eval "$(pyenv virtualenv-init -)"

```
