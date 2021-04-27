from time import sleep
from selenium import webdriver
import csv
import sys

def main(argv):
    if len(argv) < 3:
        print("Incorrect number of arguments.")
        return
    if "-p" in argv:
        list_of_sendee = read_csv(argv[1])
        if not list_of_sendee:
            return
        send_message_with_image(list_of_sendee, argv[2], argv[3], argv[4])
    else:
        list_of_sendee = read_csv(argv[0])
        if not list_of_sendee:
            return
        send_messages(list_of_sendee, argv[1], argv[2])
    print("Successfully sent messages. Check your DMs for responses!")


def read_csv(file_path):
    try:
        with open(file_path) as f:
            reader = csv.reader(f)
            return list(reader)
    except:
        print("Something went wrong when reading the file")
        return
            


def send_messages(sendee_list, user, password):
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get('https://www.instagram.com/')

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(user)
    password_input.send_keys(password)

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    sleep(5)
    not_save_pass = browser.find_element_by_xpath("//button[contains(@class, 'sqdOP yWX7d    y3zKF     ')]")
    not_save_pass.click()

    sleep(2)

    not_now = browser.find_element_by_xpath("//button[contains(@class, 'aOOlW   HoLwm ')]")
    not_now.click()

    sleep(2)

    dm_button = browser.find_element_by_xpath("//a[@class='xWeGp']")
    dm_button.click()

    sleep(2)

    for recipient in sendee_list:
        try:
            create_message_button = browser.find_element_by_xpath("//button[contains(@class, 'wpO6b ZQScA ')]")
            create_message_button.click()

            sleep(1)

            search_for_person = browser.find_element_by_css_selector("input[name='queryBox']")
            search_for_person.send_keys(recipient[0]) #change to each influencer

            sleep(1)

            select_person = browser.find_element_by_xpath("//button[@class='dCJp8 ']")
            select_person.click()

            sleep(1)

            select_next = browser.find_element_by_xpath("//button[contains(@class, 'sqdOP yWX7d    y3zKF   cB_4K  ')]")
            select_next.click()

            sleep(1)

            message_type_area_div = browser.find_element_by_xpath("//div[contains(@class, '                     Igw0E     IwRSH      eGOV_        vwCYk                                        ItkAi                                                                       ')]")
            message_type_area = message_type_area_div.find_elements_by_xpath(".//*")[0]
            message_type_area.send_keys(recipient[1]) #change to personal message

            sleep(1)

            send_message = browser.find_element_by_xpath("//button[text()='Send']")
            send_message.click()

            sleep(1)
        except:
            print(f"Failed to send to {recipient[0]}")
            continue

    
def send_message_with_image(sendee_list, user, password, image):
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get('https://www.instagram.com/')

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(user)
    password_input.send_keys(password)

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    sleep(5)
    not_save_pass = browser.find_element_by_xpath("//button[contains(@class, 'sqdOP yWX7d    y3zKF     ')]")
    not_save_pass.click()

    sleep(1)

    not_now = browser.find_element_by_xpath("//button[contains(@class, 'aOOlW   HoLwm ')]")
    not_now.click()

    sleep(1)

    dm_button = browser.find_element_by_xpath("//a[@class='xWeGp']")
    dm_button.click()

    sleep(1)

    for recipient in sendee_list:
        try:
            create_message_button = browser.find_element_by_xpath("//button[contains(@class, 'wpO6b ZQScA ')]")
            create_message_button.click()

            sleep(1)

            search_for_person = browser.find_element_by_css_selector("input[name='queryBox']")
            search_for_person.send_keys(recipient[0]) #change to each influencer

            sleep(1)

            select_person = browser.find_element_by_xpath("//button[@class='dCJp8 ']")
            select_person.click()

            sleep(1)

            select_next = browser.find_element_by_xpath("//button[contains(@class, 'sqdOP yWX7d    y3zKF   cB_4K  ')]")
            select_next.click()

            sleep(1)

            select_image_thing = browser.find_element_by_css_selector("input[class='tb_sK']")
            select_image_thing.send_keys(image)

            sleep(1) 
            
            message_type_area_div = browser.find_element_by_xpath("//div[contains(@class, '                     Igw0E     IwRSH      eGOV_        vwCYk                                        ItkAi                                                                       ')]")
            message_type_area = message_type_area_div.find_elements_by_xpath(".//*")[0]
            message_type_area.send_keys(recipient[1]) #change to personal message

            sleep(1)

            send_message = browser.find_element_by_xpath("//button[text()='Send']")
            send_message.click()

        #sleep(1)
        except:
            print(f"Failed to send to {recipient[0]}")
            continue

if __name__ == "__main__":
    main(sys.argv[1:])