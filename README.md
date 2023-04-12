# autoTest

自动化框架Demo [ pytest + selenium + allure ]

框架结构 - 待说明

安装环境依赖 pip install -r requirements.txt

### pytest 插件安装

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
### pytest 部分参数说明（部分命令需安装插件）

    多线程运行 -n Num    
    打印print内容 -s
    运行时出现失败用例中止 -x
    控制N次失败用例中止 --maxfail = Num
    失败用例重跑 --reruns Num 
    运行上次失败的用例 --lf
    运行所有用例，但优先运行上次失败的用例 --ff
   

### pytest.ini 配置

    [pytest]
    addopts = -s -q --html= report.html  命令行执行默认带参
    markers = bvt: bvt测试用例 
    @pytest.mark.bvt
    pytest -m bvt 运行标记bvt
---
### allure 生成报告

    1、安装插件 pip install allure-pytest
 
    2、PATH路径配置环境变量 allure-2.13.8/bin
 
    3、管理员身份运行pycharm
 
    4、生成XML格式的内容并指定目录 pytest test_pytest.py --alluredir ./allure-results --clean-alluredir
        参数说明:
        --alluredir             指定目录位置
        --clean-alluredir       清空目录文件
 
    5.将XML格式的内容转为HTML格式的内容 allure generate allure-results -o allure_report/html --clean
        参数说明:
        -o                  指定目录位置
        --clean-alluredir   清空目录文件
 
    6.若需要指定某些级别、某些模块单独执行用例则如下：
 
    --allure-serverities blocker 指定[标记级别为“阻塞”]用例执行
 
    --allure-feature = '登录模块' 指定[标记模块为“登录模块”]用例执行
