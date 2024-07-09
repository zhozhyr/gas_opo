$(document).ready(function () {
    $('#editModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var url = button.data('url');
        var modal = $(this);

        $.get(url, function (data) {
            modal.find('#editFormContent').html(data.html);
            $('#editForm').attr('action', url);
        });
    });

    $('#deleteModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var url = button.data('url');
        var modal = $(this);
        $.get(url, function (data) {
            modal.find('#deleteForm').html(data.html);
        });
        $('#deleteForm').attr('action', url);
    });
});