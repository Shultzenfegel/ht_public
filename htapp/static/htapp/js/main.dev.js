"use strict";

;

(function ($) {
  var KEY_ESCAPE = 27;

  function initHeaderHandlers() {
    // Открывает/закрывает выпадающие списки в меню
    $('body').click(function (e) {
      var isOpened = $(e.target).closest('.b-nav__select').hasClass('b-nav__select_opened');
      $('.b-nav__select_opened').removeClass('b-nav__select_opened');

      if ($(e.target).hasClass('b-nav__sel-button')) {
        $(e.target).closest('.b-nav__select').toggleClass('b-nav__select_opened', !isOpened);
      }
    }); // Обрабатывает выбор элемента в выпадающем меню

    $('.b-nav__sel-option').click(function (e) {// TODO: Обработка выбора элемента в выпадающем списке
    }); // Открывает мобильное меню

    $('.b-nav__icon_burger').click(function (e) {
      $('.b-nav__menu').addClass('b-nav__menu_opened');
    }); // Закрывает мобильное меню

    $('.b-nav__close-button').click(function (e) {
      $('.b-nav__menu').removeClass('b-nav__menu_opened');
    }); // Открывает диалог авторизации

    $('.b-nav__button_signin, .b-nav__icon_signin').click(function (e) {
      $('.b-dialog_signin').addClass('b-dialog_opened');
    }); // Открывает диалог регистрации

    $('.b-nav__button_signup').click(function (e) {
      $('.b-dialog_signup').addClass('b-dialog_opened');
    });
  }

  function initDialogHandlers() {
    // Закрывает диалог при нажатии на оверлей
    $('.b-dialog').click(function (e) {
      if (e.target === e.currentTarget) {
        $(e.currentTarget).removeClass('b-dialog_opened');
      }
    }); // Закрывает все открытые диалоги

    function closeDialogs() {
      $('.b-dialog_opened').removeClass('b-dialog_opened');
    } // Закрывает диалоги при нажатии ESC


    $('body').keyup(function (e) {
      if (e.which == KEY_ESCAPE) {
        closeDialogs();
      }
    }); // Инициирует ссылки в диалогах

    function initSwitchDialogLink(dialog) {
      $('.b-dialog__link_' + dialog).click(function (e) {
        closeDialogs();
        $('.b-dialog_' + dialog).addClass('b-dialog_opened');
        e.preventDefault();
      });
    }

    initSwitchDialogLink('signin');
    initSwitchDialogLink('signup');
    initSwitchDialogLink('restore'); // Отображает текст ошибки в форме

    function showError(form$, error) {
      form$.find('.b-form__error').text(error).addClass('b-form__error_visible');
    } // Скрывает текст ошибки в форме


    function hideError(form$) {
      form$.find('.b-form__error').removeClass('b-form__error_visible');
    } // Инициализирует AJAX-форму


    function initDialogAjaxForm(formId) {
      $('#' + formId).submit(function (e) {
        var form$ = $(e.target);
        var method = form$.attr('method');
        var action = form$.attr('action');
        var params = form$.serializeArray();
        hideError(form$);
        $.ajax({
          url: action,
          method: method,
          data: params
        }).done(function (data, textStatus, jqXHR) {
          if (data.ok) {
            document.location.reload();
          } else {
            showError(form$, data.message);
          }
        }).fail(function (jqXHR, textStatus, errorThrown) {
          showError(form$, 'Во время запроса возникла ошибка!');
          console.error('AJAX error!', jqXHR, textStatus, errorThrown);
        });
        e.preventDefault();
      });
    }

    initDialogAjaxForm('signInForm');
    initDialogAjaxForm('signUpForm');
    $('.b-nav__button_signout, .b-nav__icon_signout').click(function (e) {
      $.ajax({
        url: '/user/logout',
        method: 'get'
      }).done(function (data, textStatus, jqXHR) {
        if (data.ok) {
          document.location.reload();
        }
      }).fail(function (jqXHR, textStatus, errorThrown) {
        console.error('AJAX error!', jqXHR, textStatus, errorThrown);
      });
    });
  }

  function initMainFormHandlers() {
    // Открывает/закрывает выпадающие списки в форме поиска
    $('body').click(function (e) {
      var isOpened = $(e.target).closest('.b-main-select').hasClass('b-main-select_opened');
      $('.b-main-select_opened').removeClass('b-main-select_opened');

      if ($(e.target).hasClass('b-main-select__button')) {
        $(e.target).closest('.b-main-select').toggleClass('b-main-select_opened', !isOpened);
      }
    }); // Обрабатывает выбор варианта в выпадающем списке

    $('.b-main-select__option').click(function (e) {
      var value = $(e.target).data('value');
      var name = $(e.target).text();
      $(e.target).closest('.b-main-select').find('.b-main-select__input').val(value);
      $(e.target).closest('.b-main-select').find('.b-main-select__button').text(name);
    }); // Обрабатывает нажатие кнопки поиска

    $('.b-main-button').click(function (e) {
      var hobby = $('#hobby').val();
      var country = $('#country').val();

      if (!hobby || !country) {
        return false;
      }

      window.location = "/".concat(hobby, "/search/").concat(country);
    });
  }

  $(function () {
    initHeaderHandlers();
    initDialogHandlers();
    initMainFormHandlers();
  });
})(jQuery);