"use strict";

;

(function ($) {
  function initFixedButtons() {
    $(window).scroll(function (e) {
      var isFixed = $(window).scrollTop() > $('.b-nav').height();
      $('.b-hotel__actions-wrapper').toggleClass('b-hotel__actions-wrapper_fixed', isFixed);
    });
  }

  $(function () {
    initFixedButtons();
  });
})(jQuery);