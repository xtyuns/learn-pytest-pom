## Use
1. 安装驱动
    ```bash
    playwright install --with-deps chromium
    ```

2. 运行测试
    ```bash
    pytest --credentials username password -m smoke
    ```

## Dev
1. 安装依赖
    ```bash
    poetry install
    ```
2. 检查代码
    ```bash
    flake8
    ```