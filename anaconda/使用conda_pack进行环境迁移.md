# 使用conda pack进行环境迁移

### 第一步先下载conda pack

```bash
pip install conda-pack
```

如图conda-pack下载成功
![在这里插入图片描述](./使用conda_pack进行环境迁移/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5bCP6IifJQ==,size_20,color_FFFFFF,t_70,g_se,x_16.png)

### 第二步“打包原环境”

这有两个自己创建的虚拟环境，我对attnGAN进行环境迁移打包。
![在这里插入图片描述](./使用conda_pack进行环境迁移/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5bCP6IifJQ==,size_20,color_FFFFFF,t_70,g_se,x_16-1717736060788-3.png)

```bash
conda pack -n attnGAN
```

如下图，正在对环境进行打包，还是很快的。最后打包成·后缀为.tar.gz的压缩文件。
![在这里插入图片描述](./使用conda_pack进行环境迁移/a9f6249dfd844536bbf49f7c29f1b84d.png)

### 第三步“还原环境”

现在已经attnGAN.tar.gz上传到无网的服务器了，现在将attnGAN.tar.gz解压到/home/conggaoxiang/anaconda3/envs下
![在这里插入图片描述](./使用conda_pack进行环境迁移/d95cde9a8d2c498cb451d0439877d023.png)
1)先创建个文件夹

```bash
mkdir attnGAN
```

![在这里插入图片描述](./使用conda_pack进行环境迁移/ee8417842bac4baba4ffc75188964fe7.png)

2）解压

```bash
tar -xzvf attnGAN.tar.gz -C /home/conggaoxiang/anaconda3/envs/attnGAN
```

### 第四步查看结果

```bash
conda info -e
```

虚拟环境已迁移完毕
![在这里插入图片描述](./使用conda_pack进行环境迁移/5c4739c396d241ab85fb153158080602.png)
进入虚拟环境，就可以使用了