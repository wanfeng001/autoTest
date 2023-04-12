# autoTest
自动化框架Demo [pytest + selenium + allure]
框架结构 - 待说明

安装环境依赖 pip install -r requirements.txt

#### pytest 插件安装
    多线程:
    pip install pytest-xdist
    
    失败用例重跑:
    pip install pytest-rerunfailures 
    
    报告生成:
    pip install pytest-html 
    pip install allure-pytest allure
    
    用例执行顺序:
    pip install pytest-ordering 
    用法：@pytest.mark.run(order=Num)

---
#### pytest 参数说明

 - 打印出用例中print内容 -s
 - 出现n次失败用例中止 --maxfail = Num
 - 出现失败用例后中止 -x
 - 失败用例重跑 --reruns Num
 - 运行上次失败的用例 --lf
 - 运行所有用例，但优先运行上次失败的用例 --ff
 - 多线程运行 -n Num

#### pytest.ini 配置

    [pytest]
    addopts = -s -q --html= report.html  (命令行快捷）
    markers = bvt: bvt测试用例 
    @pytest.mark.bvt
    pytest -m bvt 运行标记bvt
---
#### allure 生成报告

 - pycharm安装插件 pip install allure-pytest
 - allure插件安装包需配置环境变量 allure-2.13.8/bin
 - 管理员身份运行pycharm
 - 生成xml格式报告并指定目录 pytest -ff test_pytest.py --alluredir ./allure-results --clean-alluredir
 - 将xml格式报告转换为html报告 allure generate allure-results -o allure_report/html --clean
 
 --allure-serverities blocker 指定[标记级别为“阻塞”]用例执行
 --allure-feature = '登录模块' 指定[标记模块为“登录模块”]用例执行
