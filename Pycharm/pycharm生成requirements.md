# pycharm生成requirements

第一种 适用于 单虚拟环境的情况： 

代码语言：javascript

复制

```javascript
pip freeze > requirements.txt
```

在这种方式，会将环境中的所有依赖包全都加入，如果使用的全局环境，则下载的所有包都会在里面，不管是不时当前项目依赖的。

第二种 (推荐) 使用 第三方库：`pipreqs` ，github地址为：https://github.com/bndr/pipreqs

代码语言：javascript

复制

```javascript
# 安装
pip install pipreqs
# 在当前目录生成
pipreqs . --encoding=utf8 --force
```

注意 

`--encoding=utf8` 为使用utf8编码，不然可能会报UnicodeDecodeError: 'gbk' codec can't decode byte 0xae in position 406: illegal multibyte sequence 的错误。

`--force` 强制执行，当 生成目录下的requirements.txt存在时覆盖。

方法二有问题暂未解决