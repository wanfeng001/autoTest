
## 自动化框架 Pytest + Selenium + allure
>   安装环境依赖 pip install -r requirements.txt






## pytest 插件安装
多线程

    pip install pytest-xdist

失败用例重跑

    pip install pytest-rerunfailures 

报告生成

    pip install pytest-html 

    pip install allure-pytest allure

用例执行顺序

    pip install pytest-ordering 

    用法:@pytest.mark.run(order=Num)

---

## pytest 参数

多线程运行 例如3线程（需安装插件）

    pytest test.py -n 3  

打印print的内容

    pytest test.py -s

出现失败用例中止

    pytest test.py -x

达到失败次数用例中止 

    pytest test.py --maxfail = Num

失败用例重跑3次（需安装插件）

    pytest test.py --reruns 3 

运行上次失败的用例 

    pytest test.py --lf

运行所有用例，但优先运行上次失败的用例

    pytest test.py --ff
   

## pytest.ini 配置

    [pytest]
    addopts = -s -q --html= report.html     # 命令行执行 默认带参
    markers = bvt: bvt测试用例              # 冒号写入标记说明
    
    # markes用法
    @pytest.mark.bvt    # 标记用例   
    pytest -m bvt       # 运行标记bvt
    
---

## allure 生成报告

1、安装插件 pip install allure-pytest

2、PATH路径配置环境变量 allure-2.13.8/bin

3、以管理员身份运行PyCharm

4、生成XML格式的内容并指定目录 

    pytest test_pytest.py --alluredir ./allure-results --clean-alluredir      

5、将XML格式的内容转为HTML格式的内容

    allure generate allure-results -o allure_report/html --clean

6、若需要指定某些级别、某些模块单独执行用例

    --allure-serverities blocker 指定[标记级别为“阻塞”]用例执行 

    --allure-feature = '登录模块' 指定[标记模块为“登录模块”]用例执行


