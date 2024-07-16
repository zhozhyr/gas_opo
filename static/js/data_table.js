$(document).ready(function () {
            var table = $('#dataTable').DataTable({
                "pageLength": -1,
                "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "Все"]],
                "paging": true,
                "lengthChange": true,
                "searching": true,
                "ordering": true,
                "info": true,
                "language": {
                    "sProcessing": "Обработка...",
                    "sLengthMenu": "Показать _MENU_ ТУ",
                    "sZeroRecords": "Записи не найдены",
                    "sInfo": "Показаны записи с _START_ по _END_ из _TOTAL_ записей",
                    "sInfoEmpty": "Показаны записи с 0 по 0 из 0 записей",
                    "sInfoFiltered": "(отфильтровано из _MAX_ записей)",
                    "sSearch": "Поиск: ",
                    "oPaginate": {
                        "sFirst": "Первая",
                        "sPrevious": "Предыдущая",
                        "sNext": "Следующая",
                        "sLast": "Последняя"
                    },
                    "oAria": {
                        "sSortAscending": ": активировать для сортировки столбца по возрастанию",
                        "sSortDescending": ": активировать для сортировки столбца по убыванию"
                    }
                },
                'dom': '<"top"lf>rt<"bottom"ip><"clear">',
            });

            // Переместить элемент поиска в контейнер filter_panel
            $('#dataTable_filter').detach().appendTo('#table-search-container');
            $('#dataTable_length').detach().appendTo('#table-search-container');

            // Применить фильтры при нажатии на кнопку
            $('#applyFilters').on('click', function () {
                var column1 = parseInt($('#column1').val()) + 1;
                var operator1 = $('#operator1').val();
                var value1 = $('#value1').val();
                var logic = $('#logic').val();
                var column2 = parseInt($('#column2').val()) + 1;
                var operator2 = $('#operator2').val();
                var value2 = $('#value2').val();

                // Удалить существующие фильтры
                $.fn.dataTable.ext.search = [];

                // Добавить новый фильтр
                $.fn.dataTable.ext.search.push(function (settings, data, dataIndex) {
                    var col1 = data[column1]; // Значение в столбце 1
                    var col2 = data[column2]; // Значение в столбце 2

                    console.log(col1);
                    console.log(col2);

                    var pass1 = applyFilter(col1, operator1, value1);
                    var pass2 = applyFilter(col2, operator2, value2);

                    console.log(pass1);
                    console.log(pass2);

                    if (logic === 'and') {
                        return pass1 && pass2;
                    } else {
                        return pass1 || pass2;
                    }
                });

                table.draw();
            });

            function applyFilter(value, operator, filterValue) {
                switch (operator) {
                    case '=':
                        return value == filterValue;
                    case '>':
                        return parseFloat(value) > parseFloat(filterValue);
                    case '<':
                        return parseFloat(value) < parseFloat(filterValue);
                    case 'includes':
                        return value.includes(filterValue);
                    default:
                        return false;
                }
            }

            $('#filterButton').on('click', function () {
                $('#filterPanel').toggleClass('active');
            });

            $('#closeFilters').on('click', function () {
                $('#filterPanel').removeClass('active');
            });

        });