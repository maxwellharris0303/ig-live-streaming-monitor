from selenium_driverless.sync import webdriver
from selenium_driverless.types.by import By
from time import sleep
import time
import quickstart



driver = webdriver.Chrome(max_ws_size=2**50)
# driver.maximize_window()

# USERNAME = "leveragestrategies.de"
# PASSWORD = "L$V$R@GE23"
USERNAME = "Marymdee77"
PASSWORD = "Ernesto21!"


url = "https://bc.game"
driver.get(url)
sleep(5)
try:
    allow_cookie_button = driver.find_element(By.CSS_SELECTOR, "button[class=\"_a9-- _ap36 _a9_0\"]")
    allow_cookie_button.click()
    sleep(5)
except:
    pass
try:
    username_input = driver.find_element(By.CSS_SELECTOR, "input[aria-label=\"Phone number, username, or email\"]")
    username_input.write(USERNAME)
    password_input = driver.find_element(By.CSS_SELECTOR, "input[aria-label=\"Password\"]")
    password_input.write(PASSWORD)

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]")
    login_button.click()
    sleep(10)
except:
    pass

driver.get(target_url, timeout=60, wait_load=True)
sleep(5)

tap_to_play_button = driver.find_element(By.CSS_SELECTOR, "button[class=\"_abgv\"]")
tap_to_play_button.click()
sleep(3)

while(True):
    try:
        live_video_end_element = driver.find_element(By.CSS_SELECTOR, "div[class=\"_aa1c\"]")
        if "Live Video Ended" in live_video_end_element.text:
            break
    except:
        pass
    quickstart.main()
    last_index = quickstart.getColumnCount()
    print(last_index)

    commenter_elements = driver.find_elements(By.CSS_SELECTOR, "div[class=\"_abha\"]")
    print(len(commenter_elements))
    commenter_elements = commenter_elements[last_index:]
    TAB_NAME = "Sheet1"
    for commenter_element in commenter_elements:
        commenter_id = commenter_element.find_element(By.CSS_SELECTOR, "span[class=\"_ap3a _aaco _aacw _aacx _aad7\"]").text
        comment = commenter_element.find_element(By.CSS_SELECTOR, "span[class=\"_ap3a _aaco _aacu _aacx _aad7 _aadf\"]").text
        print(f"Commenter ID: {commenter_id}")
        print(f"Comment: {comment}")

        quickstart.main()
        last_index = quickstart.getColumnCount()
        RANGE_NAME = f'{TAB_NAME}!A{last_index + 2}:J'
        data = [commenter_id, comment]
        quickstart.insertStatusInfo(RANGE_NAME, data)
    sleep(3)