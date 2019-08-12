// If all checkboxes with the same name are checked, and there is a label with a related class name, check
$(document).ready(function(){
  $(".checklist-completion-check").change(function(field){
    var sName = field.target.name;
    var checks = $('input[name="'+ sName +'"]');
    if (checks.length === checks.filter(":checked").length) {
      $("#"+sName+"-message").html('You are ready');
      $("#"+sName+"-label").removeClass('label-danger');
      $("#"+sName+"-label").addClass('label-success');
    } else {
      $("#"+sName+"-message").html('You need all of the above');
      $("#"+sName+"-label").removeClass('label-success');
      $("#"+sName+"-label").addClass('label-danger');
    }
  });
});
