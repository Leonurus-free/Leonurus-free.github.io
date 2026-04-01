# pnpm_add和install的区别

在 pnpm 中，`pnpm add` 和 `pnpm install` 都是用于安装依赖的命令，但它们的用途和行为有一些区别：

### 1. **`pnpm install`**

- **主要用途**：用于安装项目 `package.json` 中列出的所有依赖项（包括 `dependencies` 和 `devDependencies`）。

- **常见场景**：

  - 克隆项目后首次安装所有依赖。
  - 需要重新安装 `node_modules`（如手动修改了 `package.json` 或切换分支后）。

- **特点**：

  - 如果 `pnpm-lock.yaml` 存在，会按照锁文件精确安装。
  - 如果没有 `node_modules`，会创建它；如果已存在，会检查并补充缺失的依赖。

- **示例**：

  ```
  pnpm install
  ```

### 2. **`pnpm add`**

- **主要用途**：用于**新增**一个或多个依赖包，并自动更新 `package.json` 和 `pnpm-lock.yaml`。

- **常见场景**：

  - 主动添加一个新包（如 `pnpm add lodash`）。
  - 通过 `-D`、`-P` 或 `-O` 指定依赖类型（开发依赖、生产依赖、可选依赖）。

- **特点**：

  - 是 `pnpm install <pkg>` 的别名，但更直观（类似 `npm install <pkg>` 和 `yarn add <pkg>`）。
  - 会修改 `package.json`，而 `pnpm install` 默认不会修改它。

- **示例**：

  ```
  pnpm add lodash          # 添加到生产依赖
  pnpm add eslint -D       # 添加到开发依赖
  pnpm add axios@latest    # 安装指定版本
  ```

------

### 关键区别总结：

| 命令             | 作用                          | 是否修改 `package.json` | 典型场景             |
| :--------------- | :---------------------------- | :---------------------- | :------------------- |
| `pnpm install`   | 安装所有现有依赖              | 否                      | 项目初始化或恢复依赖 |
| `pnpm add <pkg>` | 新增依赖并更新 `package.json` | 是                      | 主动添加新包         |

------

### 其他注意事项：

- 如果直接运行 `pnpm install <pkg>`，效果和 `pnpm add <pkg>` 相同，但推荐使用 `add` 以保持一致性（类似 Yarn 的设计）。
- 两者都会更新 `pnpm-lock.yaml`，确保依赖版本一致性。