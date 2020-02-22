from selenium.webdriver.common.by import By


class HomePage:
    class swiper:
        slideshow = (By.CSS_SELECTOR, "#slideshow0")

        swiper_button_next = (
            By.CSS_SELECTOR,
            ".swiper-viewport:nth-child(1) .swiper-button-next",
        )
        swiper_button_prev = (
            By.CSS_SELECTOR,
            ".swiper-viewport:nth-child(1) .swiper-button-prev",
        )

        iphone6_img = (By.CSS_SELECTOR, ".swiper-slide-active")

        bullet = (
            By.CSS_SELECTOR,
            "#content > div:nth-child(1) > div >span:nth-child(2)",
        )
        bullet_active = (
            By.CSS_SELECTOR,
            "#content > div:nth-child(1) .swiper-pagination-bullet-active",
        )

    class featured:
        class macbook:
            img_link = (By.CSS_SELECTOR, ".row > .product-layout:nth-child(1) .image")
            name_link = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(1) .caption a",
            )
            description = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(1) .caption p",
            )
            price = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(1) .caption .price",
            )
            add_to_shoping_card = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(1) .button-group button:nth-child(1) ",
            )
            add_to_wishlist = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(1) .button-group button:nth-child(2) ",
            )
            add_to_compare = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(1) .button-group button:nth-child(3) ",
            )

        class iphone:
            img_link = (By.CSS_SELECTOR, ".row > .product-layout:nth-child(2) .image")
            name_link = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(2) .caption a",
            )
            description = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(2) .caption p",
            )
            price = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(2) .caption .price",
            )
            add_to_shoping_card = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(2) .button-group button:nth-child(1) ",
            )
            add_to_wishlist = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(2) .button-group button:nth-child(2) ",
            )
            add_to_compare = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(2) .button-group button:nth-child(3) ",
            )

        class apple_cinema:
            img_link = (By.CSS_SELECTOR, ".row > .product-layout:nth-child(3) .image")
            name_link = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(3) .caption a",
            )
            description = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(3) .caption p",
            )
            price = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(3) .caption .price",
            )
            add_to_shoping_card = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(3) .button-group button:nth-child(1) ",
            )
            add_to_wishlist = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(3) .button-group button:nth-child(2) ",
            )
            add_to_compare = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(3) .button-group button:nth-child(3) ",
            )

        class cannon_5d:
            img_link = (By.CSS_SELECTOR, ".row > .product-layout:nth-child(4) .image")
            name_link = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(4) .caption a",
            )
            description = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(4) .caption p",
            )
            price = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(4) .caption .price",
            )
            add_to_shoping_card = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(4) .button-group button:nth-child(1) ",
            )
            add_to_wishlist = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(4) .button-group button:nth-child(2) ",
            )
            add_to_compare = (
                By.CSS_SELECTOR,
                ".row > .product-layout:nth-child(4) .button-group button:nth-child(3) ",
            )

        # BOTTOM_SWIPER
        bottom_swiper_button_next = (
            By.CSS_SELECTOR,
            "div:nth-child(5) div.swiper-button-next",
        )
        bottom_swiper_button_prev = (
            By.CSS_SELECTOR,
            "div:nth-child(5) div.swiper-button-prev",
        )

        bullet_nfl = (
            By.CSS_SELECTOR,
            "#content > div:nth-child(5) > div > span:nth-child(1)",
        )
        bullet_redbull = (
            By.CSS_SELECTOR,
            "#content > div:nth-child(5) > div > span:nth-child(2)",
        )
        bullet_sony = (
            By.CSS_SELECTOR,
            "#content > div:nth-child(5) > div > span:nth-child(3)",
        )
        bullet_cola = (
            By.CSS_SELECTOR,
            "#content > div:nth-child(5) > div > span:nth-child(4)",
        )
        bullet_bk = (
            By.CSS_SELECTOR,
            "#content > div:nth-child(5) > div > span:nth-child(5)",
        )
        bullet_cannon = (
            By.CSS_SELECTOR,
            "#content > div:nth-child(5) > div > span:nth-child(6)",
        )
        bullet_harley = (
            By.CSS_SELECTOR,
            "#content > div:nth-child(5) > div > span:nth-child(7)",
        )
        bullet_dell = (
            By.CSS_SELECTOR,
            "#content > div:nth-child(5) > div > span:nth-child(8)",
        )
        bullet_disney = (
            By.CSS_SELECTOR,
            "#content > div:nth-child(5) > div > span:nth-child(9)",
        )
        bullet_starbucks = (
            By.CSS_SELECTOR,
            "#content > div:nth-child(5) > div > span:nth-child(10)",
        )
        bullet_nintendo = (
            By.CSS_SELECTOR,
            "#content > div:nth-child(5) > div > span:nth-child(11)",
        )
