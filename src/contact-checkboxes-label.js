// If all checkboxes with the same name are checked, and there is a label with a related class name, check
$(document).ready(function(){
  $("#checklist-completion-check").change(function(field){
    var sName = field.target.name;
    var checks = $('input[name="'+ sName +'"]');
    if (checks.length === checks.filter(":checked").length) {
      document.getElementById(sName+'-message').innerHTML = '<label class="label label-success">You are ready to call</label>';
    } else {
      document.getElementById(sName+'-message').innerHTML = '<label class="label label-danger">You need all of the above to call</label>';
    }
  });
});
