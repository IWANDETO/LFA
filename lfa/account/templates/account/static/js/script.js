var finger_enabled = $('.sign-in').data('finger');
$('.toggle-finger').on('click',function(e){
  e.preventDefault();
  finger_enabled = (finger_enabled === 'true') ? 'false' :'true';
  $('.sign-in').attr('data-finger',finger_enabled);
}); 