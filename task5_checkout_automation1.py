from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # Test 1: Open website and log in
    driver.get("https://www.saucedemo.com/")

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    print("PASS: Login successful")

    # Test 2: Add a product to the cart
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "cart_item")
        )
    )
    print("PASS: Product added to cart")

    # Test 3: Open checkout information
    driver.find_element(By.ID, "checkout").click()

    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )
    print("PASS: Checkout information page opened")

    # Test 4: Check required-field validation
    driver.find_element(By.ID, "continue").click()

    error = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert "First Name is required" in error.text
    print("PASS: Empty form validation works")

    # Test 5: Submit valid checkout information
    driver.find_element(By.ID, "first-name").send_keys("Rhythm")
    driver.find_element(By.ID, "last-name").send_keys("Shetty")
    driver.find_element(By.ID, "postal-code").send_keys("411001")
    driver.find_element(By.ID, "continue").click()

    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "finish")
        )
    )
    print("PASS: Checkout overview page opened")

    # Test 6: Complete order and verify confirmation
    driver.find_element(By.ID, "finish").click()

    confirmation = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")
        )
    )

    assert confirmation.text == "Thank you for your order!"
    print("PASS: Order confirmation verified")

    print("\nAll six test checks passed!")

except Exception as error:
    print("FAIL:", error)
    raise

finally:
    driver.quit()