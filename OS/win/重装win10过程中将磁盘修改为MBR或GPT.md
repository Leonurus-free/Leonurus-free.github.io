# 重装win10过程中将磁盘修改为MBR或GPT

重装过程中提示，磁盘格式为MBR，不支持，步骤如下：

按下shift+F10（打开powershell），依次输入：

* diskpart   回车  //显示所有磁盘信息，其中最后一列带*表示格式为GPT，不带*则为MBR

* list disk  回车  //显示所有磁盘信息，其中最后一列带*表示格式为GPT，不带*则为MBR

* select disk 1   //我是要按照到磁盘序列号为1的磁盘上，选择自己需要的

* clean    //清空该磁盘

* convert to GPT   //将磁盘格式转为GPT，convert to MBR ,则将其转为MBR