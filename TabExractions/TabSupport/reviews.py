from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tools.Tool import ( get_first_search_result_url, driver, fetch_menu_tabs, start_verbose, end_verbose, sleep)
import json

def extract_review_text(search_term, verbose):
    
    if verbose:
        start_verbose("extract_review_text", search_term)
    try:
        driver.get(get_first_search_result_url(search_term, verbose))
        
        sleep(0.5)
        
        review_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "selected-review"))
        )
        
        divs = review_container.find_elements(By.TAG_NAME, "div")
        
        content_list = []
        
        for div in divs:
            text = div.text.strip() 
            if text:
                content_list.append(text)
        
        if verbose:
            end_verbose(content_list)
        
        return content_list

    except Exception as e:
        print(f"Error: {e}")
        return None


with open(r'C:\Users\Admin\Downloads\Publisher-Portal-scrapping\Publisher-Portal-scrapping-c3f406f7401c74c8741a31781b0a23a10a2fcf9f\TabExractions\TabSupport\data\ClgNames.json', 'r') as data_file:
    college_data = json.load(data_file)

output_json = {}

for college_name, college_url in college_data.items():
    print(f"College Name: {college_name}, College URL: {college_url}")
    try:
        table_data = extract_review_text(college_name, verbose=True)
        output_json[college_url] = table_data
    except:
        output_json[college_url] = "No Reviews tab found"
        

with open(r"C:\Users\Admin\Downloads\Publisher-Portal-scrapping\Publisher-Portal-scrapping-c3f406f7401c74c8741a31781b0a23a10a2fcf9f\TabExractions\TabSupport\data\ReviewsOutput.json", 'w') as output_file:
    json.dump(output_json, output_file, indent=4)

driver.quit()


# chrome_driver_path = "chromedriver.exe"  
# url = "https://zollege.in/college/183263-coimbatore-institute-of-technology-cit-coimbatore/reviews"

# reviews = extract_review_text(url, chrome_driver_path)
