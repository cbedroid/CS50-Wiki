$(document).ready(() => {

  /* Bootstrap Modal */
  $('#deletion_modal').modal('show')

  /* Bootstrap Alert */
  setTimeout(function () {
    // Close alert popup
    $("#alert_message").alert("close");
  }, 2500);

  /* Handler Base EntryScroll Event */
  const bes = $('#base_entry_content');
  if (bes !== undefined || bes !== "undefined") {
    const start = bes.offset().top;
    $('#base_entry_section').scroll(function () {
      const nb = $('#entry_navbar');
      if (bes.offset().top !== start) {
        $(nb).css({ "box-shadow": "0px 2px 10px rgba(0,0,0,.5)" });
      } else {
        $(nb).css({ "box-shadow": "none" });
      }
    })
  }

})