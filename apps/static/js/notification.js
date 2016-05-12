var timer;
function notification (title, classname) {
  window.clearTimeout(timer);
  $('#notification').hide();
  $('#notification').removeClass();
  $('#notification').addClass(classname)
  $('#notification_text').text(title);
  $('#notification').fadeIn('fast');
  timer = setTimeout(function(){ $('#notification').fadeOut('fast'); }, 3000);
}


function modal(title, button, classname, confirmCallback, cancelCallback) {
  $('#notification_modal #modal_text').text(title);
  $('#notification_modal #modal_action').text(button);
  $('#notification_modal #modal_action').addClass(classname);
  $('#overlay').show();
  $('#notification_modal').css('display', 'block');
  
  // unbind previous clicks
  $('.modal_confirm, .modal_delete, .modal_cancel').off();
  
  $('.modal_confirm, .modal_delete').on('click', function() {
      confirmCallback();
      $('#notification_modal').css('display', 'none');;
      $('#overlay').hide();
  });
  $('.modal_cancel').on('click', function() {
      cancelCallback();
      $('#notification_modal').css('display', 'none');;
      $('#overlay').hide();
  });
}


$(document).ready(function() {
  
  $('#overlay, #notification_modal #modal_close').on('click', function() {
    $('#notification_modal').css('display', 'none');;
    $('#overlay').css('display', 'none');
  });
  
  $('#notification #notification_close, #notification_modal #modal_close').on('click', function(){
    $parent = $(this).parent();
    $parent.fadeOut(150, function() { 
      $parent.removeClass(); 
    });
  });
  
});