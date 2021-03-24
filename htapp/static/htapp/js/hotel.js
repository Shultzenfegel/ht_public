;
(($) => {
    function initFixedButtons() {
        $(window).scroll((e) => {
            let isFixed = $(window).scrollTop() > $('.b-nav').height();
            $('.b-hotel__actions-wrapper').toggleClass('b-hotel__actions-wrapper_fixed', isFixed);
        });
    }

    $(() => {
        initFixedButtons();
    });
})(jQuery);