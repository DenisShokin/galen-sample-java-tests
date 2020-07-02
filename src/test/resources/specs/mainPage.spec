@import common.spec

@objects
    main-intro-text             css         #main-page>app-main-intro>div>h2
    main-intro                  css         #main-page > app-main-intro
    company-description         css         #main-page>app-main-intro>div>div.description
    services-swiper-container   xpath       //*[@id="main-page"]/app-main-intro/div/div[2]
    projects-block              id          projects
    project-card_item-*         css         #projects>div>app-project-card a
    all-projects-button         xpath       //*[@id="projects"]/div/button
    clients                     id          clients
    technologies                id          tech
    contacts                    id          contacts
    callback-button             xpath       /html/body/app-root/app-feedback-button/button
    footer                      id          footer

@groups
    skeleton_elements   contacts,footer

@set
    contentMargin 20 to 25px

= Content =
 =Main section=
    @on *
        main-intro-text:
            text is "Мы создаем цифровые продукты"

        company-description:
            below main-intro-text
            text is "Глобальная цифровая трансформация бизнеса — особенность нашего времени. Технократия создает цифровые продукты, которые помогают большому бизнесу добиваться больших побед."
            height < 15 % of screen/height

        &skeleton_elements:
            width ~ 100 % of screen/width


    @on mobile
        services-swiper-container:
            below company-description ${contentMargin}

= Services section =
    @on mobile, on desktop
        services-swiper-container:
                aligned vertically centered main-intro

= Projects section =
    @on mobile, on desktop
        projects-block:
            below services-swiper-container




