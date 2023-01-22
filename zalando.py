from selenium import webdriver

# Initialize webdriver
driver = webdriver.Chrome()

# Login to Zalando-prive
username = "your_username"
password = "your_password"
login_to_zalando(driver,username,password)

# Navigate to Zalando-prive website
campaign_id = "12345"
driver.get("https://www.zalando-prive.fr/campaign/{}".format(campaign_id))

# Filter by price
filter_button = driver.find_element_by_xpath("//a[contains(text(),'Prix')]")
filter_button.click()

min_price = driver.find_element_by_name("minPrice")
min_price.send_keys("50")
max_price = driver.find_element_by_name("maxPrice")
max_price.send_keys("100")

# Filter by size
size_filter = driver.find_element_by_xpath("//a[contains(text(),'Taille')]")
size_filter.click()
size_select = driver.find_element_by_xpath("//label[contains(text(),'42')]")
size_select.click()

# Filter by type of clothing
clothing_filter = driver.find_element_by_xpath("//a[contains(text(),'Type de vêtement')]")
clothing_filter.click()
clothing_select = driver.find_element_by_xpath("//label[contains(text(),'T-Shirts')]")
clothing_select.click()

apply_filter_button = driver.find_element_by_xpath("//button[contains(text(),'Appliquer')]")
apply_filter_button.click()

# Select all filtered items
filtered_items = driver.find_elements_by_xpath("//div[contains(@class,'catalog-product-card')]")

# Add all filtered items to cart
for item in filtered_items:
    add_to_cart_button = item.find_element_by_xpath(".//button[contains(@class,'add-to-cart')]")
    add_to_cart_button.click()