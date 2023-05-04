""
# Open URL
driver.get('https://www.amazon.com/ap/signin')

driver.find_element(By.XPATH, 'nav-search-submit-button')
#By XPATH
# Amazon Logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
#  Continue Button
driver.find_element(By.ID, 'continue')
# Need help?
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
# Conditions of Use
driver.find_element(By.XPATH, "//a[@class='a-link-normal']")
#Privacy Notice
driver.find_element(By.XPATH, "//a[@rel='noopener']")
# Create your Amazon account
driver.find_element(By.ID, 'createAccountsubmit')


