from selenium.webdriver.common.by import By


class HomePage:
    class swiper:
        slideshow = (By.CSS_SELECTOR, "#slideshow0")

        swiper_button_next = (By.CSS_SELECTOR, ".swiper-viewport:nth-child(1) .swiper-button-next")
        swiper_button_prev = (By.CSS_SELECTOR, ".swiper-viewport:nth-child(1) .swiper-button-prev")

        iphone6_img = (By.CSS_SELECTOR, ".swiper-slide-active")

        bullet = (By.CSS_SELECTOR, "#content > div:nth-child(1) > div >span:nth-child(2)")
        bullet_active = (By.CSS_SELECTOR, "#content > div:nth-child(1) .swiper-pagination-bullet-active")

    class featured:
        class macbook:
            macbook = ".row > .product-layout:nth-child(1)"
            img_link = (By.CSS_SELECTOR, f"{macbook} .image")
            name_link = (By.CSS_SELECTOR, f"{macbook} .caption a")
            description = (By.CSS_SELECTOR, f"{macbook} .caption p")
            price = (By.CSS_SELECTOR, f"{macbook} .caption .price")
            add_to_shoping_card = (By.CSS_SELECTOR, f"{macbook} .button-group button:nth-child(1) ")
            add_to_wishlist = (By.CSS_SELECTOR, f"{macbook}) .button-group button:nth-child(2) ")
            add_to_compare = (By.CSS_SELECTOR, f"{macbook} .button-group button:nth-child(3) ")

        class iphone:
            iphone = ".row > .product-layout:nth-child(2)"
            img_link = (By.CSS_SELECTOR, f"{iphone} .image")
            name_link = (By.CSS_SELECTOR, f"{iphone} .caption a")
            description = (By.CSS_SELECTOR, f"{iphone} .caption p")
            price = (By.CSS_SELECTOR, f"{iphone} .caption .price")
            add_to_shoping_card = (By.CSS_SELECTOR, f"{iphone} .button-group button:nth-child(1) ")
            add_to_wishlist = (By.CSS_SELECTOR, f"{iphone}) .button-group button:nth-child(2) ")
            add_to_compare = (By.CSS_SELECTOR, f"{iphone} .button-group button:nth-child(3) ")

        class apple_cinema:
            apple_cinema = ".row > .product-layout:nth-child(3)"
            img_link = (By.CSS_SELECTOR, f"{apple_cinema} .image")
            name_link = (By.CSS_SELECTOR, f"{apple_cinema} .caption a")
            description = (By.CSS_SELECTOR, f"{apple_cinema} .caption p")
            price = (By.CSS_SELECTOR, f"{apple_cinema} .caption .price")
            add_to_shoping_card = (By.CSS_SELECTOR, f"{apple_cinema} .button-group button:nth-child(1) ")
            add_to_wishlist = (By.CSS_SELECTOR, f"{apple_cinema}) .button-group button:nth-child(2) ")
            add_to_compare = (By.CSS_SELECTOR, f"{apple_cinema} .button-group button:nth-child(3) ")

        class cannon_5d:
            cannon_5d = ".row > .product-layout:nth-child(4)"
            img_link = (By.CSS_SELECTOR, f"{cannon_5d} .image")
            name_link = (By.CSS_SELECTOR, f"{cannon_5d} .caption a")
            description = (By.CSS_SELECTOR, f"{cannon_5d} .caption p")
            price = (By.CSS_SELECTOR, f"{cannon_5d} .caption .price")
            add_to_shoping_card = (By.CSS_SELECTOR, f"{cannon_5d} .button-group button:nth-child(1) ")
            add_to_wishlist = (By.CSS_SELECTOR, f"{cannon_5d}) .button-group button:nth-child(2) ")
            add_to_compare = (By.CSS_SELECTOR, f"{cannon_5d} .button-group button:nth-child(3) ")

        # BOTTOM_SWIPER
        bottom_swiper_button_next = (By.CSS_SELECTOR, "div:nth-child(5) div.swiper-button-next")
        bottom_swiper_button_prev = (By.CSS_SELECTOR, "div:nth-child(5) div.swiper-button-prev")

        # BULLET
        bullet = "#content > div:nth-child(5) > div > span:nth-child"
        bullet_nfl = (By.CSS_SELECTOR, f"{bullet}(1)")
        bullet_redbull = (By.CSS_SELECTOR, f"{bullet}(2)")
        bullet_sony = (By.CSS_SELECTOR, f"{bullet}(3)")
        bullet_cola = (By.CSS_SELECTOR, f"{bullet}(4)")
        bullet_bk = (By.CSS_SELECTOR, f"{bullet}(5)")
        bullet_cannon = (By.CSS_SELECTOR, f"{bullet}(6)")
        bullet_harley = (By.CSS_SELECTOR, f"{bullet}(7)")
        bullet_dell = (By.CSS_SELECTOR, f"{bullet}(8)")
        bullet_disney = (By.CSS_SELECTOR, f"{bullet}(9)")
        bullet_starbucks = (By.CSS_SELECTOR, f"{bullet}(10)")
        bullet_nintendo = (By.CSS_SELECTOR, f"{bullet}(11)")
