from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time, json

text_files = []
DicData = {}
ErrDic = {}
input_data = "txt"
file_path = []
full_file_path = []

def GenLink(topic_search: str) -> str:
    """
    Generates a link for a given topic search.

    Args:
        topic_search (str): The topic to search for.

    Returns:
        str: The generated link.

    Example usage:
        link = GenLink("machine learning")
        print(link)
    """
    topic_search = topic_search.replace(' ', '+')

    chrome_options = Options()

    service = Service('chromedriver.exe')

    browser = webdriver.Chrome(service=service, options=chrome_options)

    for i in range(1):  
        url = f"https://www.shiksha.com/search?q={topic_search}&start={i * 10}"
        browser.get(url)

        time.sleep(3)

        div_elements = browser.find_elements(By.CSS_SELECTOR, 'div.c8ff')

        for div in div_elements:
            
            link = div.find_element(By.TAG_NAME, 'a')
            
            widget_label = link.get_attribute('widgetspecificlabel')
            href_url = link.get_attribute('href')
    time.sleep(10) 
    browser.quit()
    return href_url



import os
current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)

relative_path = os.path.join(current_directory, '..', '..', 'TabExractions', 'TabSupport', 'data', 'InputData')
target_directory = os.path.abspath(relative_path)

print(relative_path, target_directory)

if os.path.exists(target_directory) and os.path.isdir(target_directory):
    text_files = [f for f in os.listdir(target_directory) if f.endswith('.txt')]
    if text_files:
        print("List of .txt files with their full paths:")
        for file in text_files:
            full_file_path.append(os.path.join(target_directory, file))
    else:
        print("No .txt files found in the directory.")
else:
    print("Target directory does not exist.")

count = 0

def run(path):
    if input_data == "csv":
        with open('Colleges_Dataset_last-till4000.csv', 'r') as fs:
            data = fs.readlines()
            for j, i in enumerate(data):
                clean_data = i.strip().replace('"', '')
                print(clean_data)
                try:
                    Urls = GenLink(clean_data)
                    DicData[i.replace("\n", "")] = Urls
                    print(DicData)
                    with open('DicData_last-till4000.json', 'w') as json_file:
                        json.dump(DicData, json_file, indent=4)
                except:
                    print("Error occurred while generating link for", clean_data)
                    ErrDic[j] = i
                    with open('ErrDic_last-till4000.json', 'w') as json_file:
                        json.dump(ErrDic, json_file, indent=4)
    else:
        with open(path, 'r') as fs:
            directory_path = os.path.dirname(path)
            parent_directory = os.path.abspath(os.path.join(directory_path, '..', '..'))
            output_directory = os.path.join(parent_directory, 'Output')
            os.makedirs(output_directory, exist_ok=True)
            base_name = os.path.basename(path)
            clg_names = fs.read()
            
            for j, i in enumerate(clg_names.split("\n")):
                clean_data = i.strip().replace('"', '')
                print(clean_data)
                try:
                    Urls = GenLink(clean_data)
                    DicData[i.replace("\n", "")] = Urls
                    print(DicData)
                    with open(os.path.join(output_directory, "Output"+base_name), 'w') as json_file:
                        json.dump(DicData, json_file, indent=4)
                except Exception as e:
                    print("Error occurred while generating link for", clean_data, e)
                    ErrDic[j] = i
                    with open(os.path.join(output_directory, "ErrOutput"+base_name), 'w') as json_file:
                        json.dump(ErrDic, json_file, indent=4)
        
if text_files:
    for i in full_file_path:
        DicData = []
        print("Running on file: ", i)
        run(i)
        count=+1
else:
    print("No .txt files found in the directory.")


