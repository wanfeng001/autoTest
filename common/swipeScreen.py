def swipeDown(driver,t=500,n=1):
    l = driver.get_window_size()
    x1= l['width']* 0.5
    y1= l['height']* 0.25
    y2= l['height']* 0.8
    for i in range(n):
        driver.swipe(x1,y1,x1,y2,t)

def swipeUp(driver,t=500,n=1):
    l = driver.get_window_size()
    x1= l['width']* 0.5
    y1= l['height']* 0.75
    y2= l['height']* 0.25
    for i in range(n):
        driver.swipe(x1,y1,x1,y2,t)

def swipeRight(driver,t=500,n=1):
    l = driver.get_window_size()
    x1= l['width']* 0.5
    x2= l['width']* 0.75
    y1= l['height']* 0.5
    for i in range(n):
        driver.swipe(x1,y1,x2,y1,t)

def swipeLeft(driver,t=500,n=1):
    l = driver.get_window_size()
    x1= l['width']* 0.5
    x2= l['width']* 0.25
    y1= l['height']* 0.5
    for i in range(n):
        driver.swipe(x1,y1,x2,y1,t)


