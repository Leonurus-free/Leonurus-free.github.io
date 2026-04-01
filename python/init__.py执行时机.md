# `__init__.py`执行时机

在 Python 项目中，文件夹中的 `__init__.py` 文件的执行时机与模块导入密切相关。以下是具体的执行场景和时机：

------

### **1. 导入包含 `__init__.py` 的模块时执行**

当 Python 解释器第一次导入一个包含 `__init__.py` 文件的模块或包时，`__init__.py` 会被执行一次。

**触发条件：**

- 使用 

  ```
  import
  ```

   导入包或模块时，例如：

  ```
  python
  
  
  复制代码
  import my_package
  ```

  或

  ```
  python
  
  
  复制代码
  from my_package import module
  ```

**执行顺序：**

- Python 会查找 `my_package` 目录中的 `__init__.py` 文件，并执行其中的代码。
- 如果导入的是子模块，则在执行 `__init__.py` 后，加载目标子模块。

------

### **2. 作为模块初始化的一部分**

`__init__.py` 的主要作用是初始化包，并控制包的导入行为：

- 定义包的初始化逻辑，比如设置全局变量、注册组件、或执行一些包级别的配置。

- 指定导入时包的默认行为，例如通过设置 

  ```
  __all__
  ```

   变量来控制 

  ```
  from package import *
  ```

   的导入内容：

  ```
  python
  
  
  复制代码
  __all__ = ['module1', 'module2']
  ```

------

### **3. 间接调用时执行**

即使没有显式导入整个包，但导入包中模块时，`__init__.py` 仍会被执行。例如：

```
python


复制代码
from my_package.module import some_function
```

即使只导入了 `module`，`my_package` 目录中的 `__init__.py` 仍会先执行，之后才导入 `module`。

------

### **4. 动态导入时执行**

如果使用动态导入（如 `importlib` 或 `__import__` 函数），`__init__.py` 也会在导入过程中被执行。例如：

```
python复制代码import importlib
package = importlib.import_module('my_package')
```

在这段代码中，`my_package/__init__.py` 会被执行。

------

### **5. 直接运行包时执行**

如果使用 `python -m package_name` 命令运行一个包，`__init__.py` 也是入口文件：

```
bash


复制代码
python -m my_package
```

此时，`__init__.py` 会作为脚本被执行。

------

### **6. 不会自动执行的场景**

- 如果没有导入包含 `__init__.py` 的包或模块，该文件不会被执行。
- 如果文件夹中没有 `__init__.py` 文件，Python 会将其视为普通目录，而不是包。在这种情况下，即使导入子模块，也不会执行不存在的 `__init__.py`。

------

### **总结**

- **首次导入**：无论直接导入包还是通过子模块间接导入，只要涉及包，`__init__.py` 都会执行。
- **初始化逻辑**：`__init__.py` 是包的入口文件，适合放置包级别的初始化逻辑。
- **控制行为**：通过 `__all__` 或其他逻辑，决定导入包时的行为。

