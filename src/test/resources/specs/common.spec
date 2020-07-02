@objects
    header                  xpath       /html/body/app-root/app-header/header
    header-logo             xpath       /html/body/app-root/app-header/header/a/app-icon[3]
    header-menu-btn         xpath       /html/body/app-root/app-header/header/button


= Header =
    @on desktop
        header:
            inside screen 0px top
            image file  images/headerMainPageDesktop.png, error 10%

    @on tablet
        header:
            inside screen 0px top
            width ~ 750px
            height ~ 93px

    @on mobile
        header:
            inside screen 0px top
            centered horizontally inside screen 1px
            image file  images/headerMainPageMobile.png, error 10%

        header-logo:
            width ~ 34px
            height ~ 34px

        header-menu-btn:
            image file  images/headerMainPageDesktop.png, error 10%