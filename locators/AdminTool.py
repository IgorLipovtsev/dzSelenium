from selenium.webdriver.common.by import By


class AdminTool:
    # login to admin tool
    username = (By.CSS_SELECTOR, 'input[name="username"]')
    password = (By.CSS_SELECTOR, 'input[name="password"]')
    forgot_password = (By.CSS_SELECTOR, '.help-block a')
    login = (By.CSS_SELECTOR, '.text-right button')
    # NAVIGATION
    # CATALOG
    catalog = (By.CSS_SELECTOR, "#menu-catalog a[href='#collapse1']")
    products = (By.CSS_SELECTOR, "#collapse1 li:nth-child(2)")

    list_of_products = (By.CSS_SELECTOR, ".table-responsive tr")
    newly_added_product = (By.XPATH, "//*[contains(text(), )]")

    add_new_product = (By.CSS_SELECTOR, "[data-original-title='Add New']")
    copy_product = (By.CSS_SELECTOR, "[data-original-title='Copy']")
    delete_product = (By.CSS_SELECTOR, "[data-original-title='Delete']")

    save_product = (By.CSS_SELECTOR, "[data-original-title='Save']")
    alert_success = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
    alert_success_close = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible button")

    add_checkbox_to_product = (By.XPATH, "//input[@type='checkbox']")
    # creation of product
    # general
    general = (By.CSS_SELECTOR, ".nav.nav-tabs li:nth-child(1)")
    product_name = (By.CSS_SELECTOR, "#input-name1")
    description = (By.CSS_SELECTOR, ".note-editable.panel-body")
    meta_tag_title = (By.CSS_SELECTOR, "#input-meta-title1")
    # data
    data = (By.CSS_SELECTOR, ".nav.nav-tabs li:nth-child(2)")
    # image
    image = (By.CSS_SELECTOR, ".nav.nav-tabs li:nth-child(9)")
    default_image = (By.CSS_SELECTOR, ".table a")
    image_manager = (By.CSS_SELECTOR, "#button-image")
    image_upload = (By.CSS_SELECTOR, ".fa.fa-upload")
    file_upload = (By.CSS_SELECTOR, "input[type='file']")
    close_image_manager = (By.CSS_SELECTOR, "#filemanager .close")
    new_avatar = (By.CSS_SELECTOR, "[title^='Spider.jpg']")

    model = (By.CSS_SELECTOR, "#input-model")
