# autoTest
自动化框架Demo
### pytest 插件安装
    pip install pytest-xdist 多线程，缩短执行时间
    
    pip install pytest-rerunfailures 失败用例重跑
    
    pip install pytest-html 测试报告
    
    pip install allure-pytest 测试allure报告
    
    pip install pytest-ordering 用例执行顺序

---
### pytest 参数意义

    打印出用例中print内容 -s
    
    出现n次失败用例中止 --maxfail=Num
    
    出现失败用例后中止 -x
    
    失败用例重跑 --reruns Num
    
    运行上次失败的用例 --lf
    
    运行所有用例，但优先运行上次失败的用例 --ff
    
    顺序执行用例 @pytest.mark.run(order=Num)
    
    多线程运行 -n Num

### pytest.ini 用法

    [pytest]
    addopts = -s -q --html= report.html  (命令行设置）
    markers = bvt: bvt测试用例 
    @pytest.mark.bvt
    pytest -m bvt 运行标记bvt
---
###allure 生成报告注意点
    1.pycharm安装插件 pip install allure-pytest
    2.allure插件安装包需配置环境变量 allure-2.13.8/bin
    4.allure+open/sever+“文件目录” #设置一个bat文件快捷打开
    5.生成xml格式报告并指定目录 pytest -ff test_pytest.py --alluredir ./allure-results --clean-alluredir（清除之前的数据）
    6.将xml格式报告转换为html报告 allure generate allure-results -o allure_report/html --clean（清除之前的数据）

    范围执行
    1.执行文件中‘标记的等级’用例的时候加上 --allure-serverities blocker
    2.执行文件中‘标记的层级’用例的时候加上 --allure-feature = '功能模块'