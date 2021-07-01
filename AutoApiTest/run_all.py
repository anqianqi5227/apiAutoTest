import pytest# 默认运行的是当前目录及子目录的所有文件夹的测试用例
pytest.main(['-k','tests','-s'])