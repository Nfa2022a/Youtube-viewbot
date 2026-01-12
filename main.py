import os, random, time, json, itertools
from selenium import webdriver
import undetected_chromedriver as uc
from fake_useragent import UserAgent
from colorama import Fore

class Viewbot:
    def __init__(self):
        self.config = json.load(open('./data/config.json', 'r+'))
        
        # Check proxies file
        proxies_file = './data/proxies.txt'
        if not os.path.exists(proxies_file) or os.path.getsize(proxies_file) == 0:
            raise ValueError(f"{proxies_file} is missing or empty. Run proxy generator first.")
        
        self.proxies = itertools.cycle(open(proxies_file).read().splitlines())
        self.ua = UserAgent()

    def ui(self):
        os.system('cls && title Youtube Viewbot ^| github.com/Plasmonix' if os.name == "nt" else 'clear') 
        print(f"""{Fore.RED}                                                           
         __ __         _       _          _____ _           _       _     
        |  |  |___ _ _| |_ _ _| |_ ___   |  |  | |___ _ _ _| |_ ___| |_   
        |_   _| . | | |  _| | | . | -_|  |  |  | | -_| | | | . | . |  _|  
          |_| |___|___|_| |___|___|___|   \___/|_|___|_____|___|___|_|    
        {Fore.RESET}""")

    def open_url(self, ua, sleep_time, proxy):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--incognito")
        self.options.add_argument('--start-maximized')
        self.options.add_argument('user-agent=%s' % ua.random)
        self.options.add_argument("--proxy-server=%s" % proxy)
        self.options.headless = True

        self.browser = uc.Chrome(options=self.options)
        
        self.browser.get(self.config["url"])
        time.sleep(sleep_time)
        self.browser.quit()

    def main(self):
        self.ui()
        proxy_iter = iter(self.proxies)
        for i in range(self.config["views"]):
            try:
                proxy = next(proxy_iter)
                print(f"View {i+1}/{self.config['views']} using proxy {proxy}")
            except StopIteration:
                print("No more proxies available. Stopping.")
                break
            
            self.sleeptime = random.randint(self.config["min_watch"], self.config["max_watch"])
            self.open_url(self.ua, self.sleeptime, proxy)

if __name__ == "__main__":
    bot = Viewbot()
    bot.main()
