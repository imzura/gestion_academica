$(document).ready(function () {
    // Detecta el número de opciones en el select
    var optionsCount = $('input[type="checkbox"]').length;

    // Si hay más de tres opciones, aplica el desplazamiento
    if (optionsCount > 3) {
        $('.form-select-lg').addClass('scrollable-select');
    }
});