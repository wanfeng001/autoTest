from common import configPath
filename = configPath.picture_path

def take_photo_as_file(self,driver):
    driver.save_screenshot(filename=filename)

def take_photo_as_base64(self,driver):
    driver.get_screenshot_as_png(filename=filename)