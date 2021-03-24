;
(($) => {
    const SEARCH_DELAY = 1000;

    // Инициализирует поля фильтров
    function initFilters() {
        $('.b-filter_datepicker').datepicker({
            autoClose: true,
            format: 'dd.mm.yyyy',
            minDate: new Date(),
            i18n: {
                cancel: 'Отмена',
                clear: 'Очистить',
                done: 'Ok',
                previousMonth: '‹',
                nextMonth: '›',
                months: [
                    'Январь',
                    'Февраль',
                    'Март',
                    'Апрель',
                    'Май',
                    'Июнь',
                    'Июл',
                    'Август',
                    'Сентябрь',
                    'Октябрь',
                    'Ноябрь',
                    'Декабрь'
                ],                                
                monthsShort: [
                    'Янв',
                    'Фев',
                    'Мар',
                    'Апр',
                    'Май',
                    'Июн',
                    'Июл',
                    'Авг',
                    'Сен',
                    'Окт',
                    'Ноя',
                    'Дек'
                ],              
                weekdays: [
                    'Воскресенье',
                    'Понедельник',
                    'Вторник',
                    'Среда',
                    'Четверг',
                    'Пятница',
                    'Суббота'
                ],       
                weekdaysShort: [
                    'Вос',
                    'Пон',
                    'Втр',
                    'Срд',
                    'Чет',
                    'Пят',
                    'Суб'
                ],                                 
                weekdaysAbbrev:	['Вс','Пн','Вт','Ср','Чт','Пт','Сб']
            }
        });

        let numberFormat = new Intl.NumberFormat('ru-RU', { maximumSignificantDigits: 10 });
        
        $('.b-filter__range-input').each((i, slider) => {
            let slider$ = $(slider);
            let sliderMinValue = Number(slider$.data('min-value'));
            let sliderMaxValue = Number(slider$.data('max-value'));
            
            if (sliderMinValue == sliderMaxValue) {
                sliderMaxValue += 100;
            }
    
            noUiSlider.create(slider, {
                start: [sliderMinValue, sliderMaxValue],
                connect: true,
                range: {
                    'min': sliderMinValue,
                    'max': sliderMaxValue
                },
                step: 100,
            });
    
            slider.noUiSlider.on('update', function (values, handle) {
                let fromValue = values[0];
                let toValue = values[1];
                
                slider$.closest('.b-filter_range').find('.b-filter__range-from-value').text(numberFormat.format(fromValue));
                slider$.closest('.b-filter_range').find('.b-filter__range-to-value').text(numberFormat.format(toValue));
                slider$.closest('.b-filter_range').find('.b-filter__input-from').val(fromValue);
                slider$.closest('.b-filter_range').find('.b-filter__input-to').val(toValue);
            });
    
            slider.noUiSlider.on('change', function (values, handle) {
                search();
            });
        });

        $('.b-filter__checkbox').change((e) => {
            search();
        });
    }

    function showPreloader() {
        $('.b-results__preloader').addClass('b-results__preloader_active');
    }

    function hidePreloader() {
        $('.b-results__preloader').removeClass('b-results__preloader_active');
    }

    function clearResults() {
        $('.b-results__list').empty();
    }

    function fillResults(content) {
        $('.b-results__list').html(content);

        let resultsData = JSON.parse($('#resultsData').text());

        $('.b-results__count').text(resultsData.count !== undefined ? resultsData.count : '');
    }

    var searchTimer = null;

    // Выполняет поиск отелей с учетом заданных фильтров
    function search(skipTimeout = false) {
        if (searchTimer !== null) {
            clearTimeout(searchTimer);
        }

        searchTimer = setTimeout(
            () => {
                let form$ = $('#filtersForm');
                let method = form$.attr('method');
                let action = form$.attr('action');
                let params = form$.serializeArray();
                
                clearResults();
                showPreloader();

                $.ajax({
                    url: action,
                    method: method,
                    data: params
                })
                .done((data, textStatus, jqXHR) => {
                    fillResults(data);
                })
                .fail((jqXHR, textStatus, errorThrown) => {
                    fillResults('<p>К сожалению, во время поиска возникла ошибка</p>');
                    console.error('AJAX error!', jqXHR, textStatus, errorThrown);
                })
                .always(() => {
                    hidePreloader();
                });
            },
            skipTimeout ? 0 : SEARCH_DELAY 
        );
    }

    $(() => {
        initFilters();
        search(true);
    });
})(jQuery);