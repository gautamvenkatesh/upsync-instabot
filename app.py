from time import sleep
from selenium import webdriver
import csv
import sys

def main(argv):
    if len(argv) != 1:
        print("Incorrect number of arguments.")
        return
    list_of_sendee = read_csv(argv[0])
    if not list_of_sendee:
        return
    send_messages(list_of_sendee)
    print("Successfully sent messages. Check your DMs for responses!")


def read_csv(file_path):
    try:
        with open(file_path) as f:
            reader = csv.reader(f)
            return list(reader)
    except:
        print("Something went wrong when reading the file")
        return
            


def send_messages(sendee_list):
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get('https://www.instagram.com/')

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys("<username>")
    password_input.send_keys("<password>")

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

        create_message_button = browser.find_element_by_xpath("//button[contains(@class, 'wpO6b ZQScA ')]")
        create_message_button.click()

        sleep(2)

        search_for_person = browser.find_element_by_css_selector("input[name='queryBox']")
        search_for_person.send_keys(recipient[0]) #change to each influencer

        sleep(2)

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

    


if __name__ == "__main__":
    main(sys.argv[1:])