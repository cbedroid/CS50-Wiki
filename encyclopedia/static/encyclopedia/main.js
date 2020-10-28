$(document).ready(() => {

  /* Bootstrap Modal */
  $('#deletion_modal').modal('show')

  /* Bootstrap Alert */
  setTimeout(function () {
    // Close alert popup
    $("#alert_message").alert("close");
  }, 2500);
})