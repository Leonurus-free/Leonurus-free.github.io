# ubuntu中激活禁止conda

## 启用

永久禁用 conda 自动激活

~~~
conda config --set auto_activate_base true
~~~

## 禁止

重新打开终端时，conda 的 base 环境会自动激活

~~~
conda config --set auto_activate_base false
~~~

