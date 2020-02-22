from selenium.webdriver.common.by import By


class TopMenu:
    # CURRENCIES
    currency_dropdown = (By.CSS_SELECTOR, ".btn.btn-link.dropdown-toggle")
    euro = (By.CSS_SELECTOR, '[name="EUR"]')
    gbp = (By.CSS_SELECTOR, '[name="GBP"]')
    usd = (By.CSS_SELECTOR, '[name="USD"]')
    # ACCOUNT
    account_menu = (By.CSS_SELECTOR, ".dropdown .fa")
    account_register = (By.CSS_SELECTOR, ".dropdown-menu.dropdown-menu-right li:nth-child(1) a")
    account_login = (By.CSS_SELECTOR, ".dropdown-menu.dropdown-menu-right li:nth-child(2) a")
    # HEADER
    contact_us = (By.CSS_SELECTOR, ".fa.fa-phone")

    wishlist = (By.CSS_SELECTOR, '[id="wishlist-total"]')
    shopping_cart = (By.CSS_SELECTOR, ".list-inline .fa.fa-shopping-cart")
    checkout = (By.CSS_SELECTOR, ".list-inline .fa.fa-share")

    homepage_link = (By.CSS_SELECTOR, "header #logo")
    search = (By.CSS_SELECTOR, 'header [name="search"]')
    search_results = (By.CSS_SELECTOR, "header .input-group-btn")
    cart = (By.CSS_SELECTOR, "header #cart button")
    # MAIN MENU

    # DESKTOPS
    desktops = "#menu .dropdown:nth-child(1)"
    desktops_list = (By.CSS_SELECTOR, f"{desktops}")
    pc = (By.CSS_SELECTOR, f"{desktops} .dropdown-inner li:nth-child(1)")
    mac = (By.CSS_SELECTOR, f"{desktops}.dropdown-inner li:nth-child(2)")
    desktops_all = (By.CSS_SELECTOR, f"{desktops}.see-all")

    # LAPTOPS
    laptops = "#menu  .dropdown:nth-child(2)"
    laptops_list = (By.CSS_SELECTOR, f"{laptops}")
    macs = (By.CSS_SELECTOR, f"{laptops} .dropdown-inner li:nth-child(1)")
    windows = (By.CSS_SELECTOR, f"{laptops} .dropdown-inner li:nth-child(2)")
    laptops_all = (By.CSS_SELECTOR, f"{laptops} .see-all")

    # COMPONENTS
    components = "#menu .dropdown:nth-child(3)"
    components_list = (By.CSS_SELECTOR, f"{components}")
    mice_and_trackballs = (By.CSS_SELECTOR, f"{components} .dropdown-inner li:nth-child(1)")
    monitors = (By.CSS_SELECTOR, f"{components} .dropdown-inner li:nth-child(2)")
    printers = (By.CSS_SELECTOR, f"{components} .dropdown-inner li:nth-child(3)")
    scanners = (By.CSS_SELECTOR, f"{components} .dropdown-inner li:nth-child(4)")
    web_cameras = (By.CSS_SELECTOR, f"{components} .dropdown-inner li:nth-child(5)")
    components_all = (By.CSS_SELECTOR, f"{components} .see-all")

    # TABLETS
    tablets = (By.CSS_SELECTOR, "#menu .nav.navbar-nav > li:nth-child(4)")

    # SOFTWARE
    software = (By.CSS_SELECTOR, "#menu .nav.navbar-nav > li:nth-child(5)")

    # PHONES
    phones = (By.CSS_SELECTOR, "#menu .nav.navbar-nav > li:nth-child(6)")

    # CAMERAS
    cameras = (By.CSS_SELECTOR, "#menu .nav.navbar-nav > li:nth-child(7)")

    # MP3
    mp3_players = "#menu .dropdown:nth-child(8)"
    mp3_players_list = (By.CSS_SELECTOR, f"{mp3_players}")
    # table1
    table1 = f"{mp3_players} .list-unstyled:nth-child(1) li:nth-child"
    mp3_1_11 = (By.CSS_SELECTOR, f"{table1}(1)")
    mp3_1_12 = (By.CSS_SELECTOR, f"{table1}(2)")
    mp3_1_15 = (By.CSS_SELECTOR, f"{table1}(3)")
    mp3_1_16 = (By.CSS_SELECTOR, f"{table1}(4)")
    mp3_1_17 = (By.CSS_SELECTOR, f"{table1}(5)")
    # table2
    table2 = f"{mp3_players} .list-unstyled:nth-child(2) li:nth-child"
    mp3_2_18 = (By.CSS_SELECTOR, f"{table2}(1)")
    mp3_2_19 = (By.CSS_SELECTOR, f"{table2}(2)")
    mp3_2_20 = (By.CSS_SELECTOR, f"{table2}(3)")
    mp3_2_21 = (By.CSS_SELECTOR, f"{table2}(4)")
    mp3_2_22 = (By.CSS_SELECTOR, f"{table2}(5)")
    # table3
    table3 = f"{mp3_players} .list-unstyled:nth-child(3) li:nth-child"
    mp3_3_23 = ((By.CSS_SELECTOR, f"{table3}(1)"))
    mp3_3_24 = ((By.CSS_SELECTOR, f"{table3}(2)"))
    mp3_3_4 = ((By.CSS_SELECTOR, f"{table3}(3)"))
    mp3_3_5 = ((By.CSS_SELECTOR, f"{table3}(4)"))
    mp3_3_6 = ((By.CSS_SELECTOR, f"{table3}(5)"))
    # table4
    table4 = f"{mp3_players} .list-unstyled:nth-child(4) li:nth-child"
    mp3_4_7 = ((By.CSS_SELECTOR, f"{table4}(1)"))
    mp3_4_8 = ((By.CSS_SELECTOR, f"{table4}(2)"))
    mp3_4_9 = ((By.CSS_SELECTOR, f"{table4}(3)"))

    mp3_all = (By.CSS_SELECTOR, f"{mp3_players} .see-all")
