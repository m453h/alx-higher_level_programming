$('document').ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?';
  $('INPUT#btn_translate').click(function () {
    const languageCode = $('INPUT#language_code').val();
    $.get(url, { lang: languageCode }, function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
