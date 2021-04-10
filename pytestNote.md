pip install pytest-xdist 多线程，缩短执行时间
pip install pytest-rerunfailures 失败用例重跑
pip install pytest-html 测试报告
pip install allure-pytest 测试allure报告
pip install pytest-ordering 用例执行顺序

打印出用例中print内容
pytest -s test_pytest.py

出现n次失败用例中止
pytest.main(['--maxfail=2','test_pytest.py'])

出现失败用例后中止
pytest.main(['-x', 'test_pytest.py'])

失败用例重跑
pytest test_pytest.py --reruns NUM(数量)

运行上次失败的用例
pytest test_pytest.py --lf

运行所有用例，但优先运行上次失败的用例
pytest test_pytest.py --ff

顺序执行用例
@pytest.mark.run(order=n) n表示数字

多线程运行
pytest test_pytest.py -n 3

配置文件（pytest.ini）设置
[pytest]
addopts = -s -q --html= report.html  (命令行设置）
markers = bvt: bvt测试用例 (标记）
@pytest.mark.bvt
pytest -m bvt


allure生成报告 注意点
1.pycharm安装插件 pip install allure-pytest
2.allure插件安装包需配置环境变量 allure-2.13.8/bin
4.allure+open/sever+“文件目录” #设置一个bat文件快捷打开
5.生成xml格式报告并指定目录 pytest -ff test_pytest.py --alluredir ./allure-results --clean-alluredir（清除之前的数据）
6.将xml格式报告转换为html报告 allure generate allure-results -o allure_report/html --clean（清除之前的数据）

范围执行
1.执行文件中‘标记的等级’用例的时候加上 --allure-serverities blocker
2.执行文件中‘标记的层级’用例的时候加上 --allure-feature = '功能模块'
