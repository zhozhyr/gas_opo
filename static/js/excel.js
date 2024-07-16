function exportTableToExcel(tableId, filename) {
    var table = document.getElementById(tableId);
    var wb = XLSX.utils.table_to_book(table, {sheet: "1"});

    // Применение стилей
    var ws = wb.Sheets["1"];
    var range = XLSX.utils.decode_range(ws['!ref']);


    var wbout = XLSX.write(wb, {bookType: 'xlsx', type: 'binary'});

    function s2ab(s) {
        var buf = new ArrayBuffer(s.length);
        var view = new Uint8Array(buf);
        for (var i = 0; i < s.length; i++) {
            view[i] = s.charCodeAt(i) & 0xFF;
        }
        return buf;
    }

    var blob = new Blob([s2ab(wbout)], {type: "application/octet-stream"});
    var link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}