$('document').ready(function () {
  function getTranslation () {
    const url = 'https://hellosalut.stefanbohacek.dev/?';
    const languageCode = $('INPUT#language_code').val();
    $.get(url, { lang: languageCode }, function (data) {
      $('DIV#hello').html(data.hello);
    });
  }

  $('INPUT#btn_translate').click(function () {
    getTranslation();
  });

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      getTranslation();
    }
  });
});
