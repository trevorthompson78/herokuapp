

// var formValues = JSON.parse(localStorage.getItem('formValues')) || {};
// var $checkboxes = $("#checkbox-container :checkbox");
// var $button = $("#checkbox-container button");

// function allChecked(){
//   return $checkboxes.length === $checkboxes.filter(":checked").length;
// }

// function updateButtonStatus(){
//   $button.text(allChecked()? "Uncheck all" : "Check all");
// }

// function handleButtonClick(){
//   $checkboxes.prop("checked", allChecked()? false : true)
// }

// function updateStorage(){
//   $checkboxes.each(function(){
//     formValues[this.id] = this.checked;
//   });

//   formValues["buttonText"] = $button.text();
//   localStorage.setItem("formValues", JSON.stringify(formValues));
// }

// $button.on("click", function() {
//   handleButtonClick();
//   updateButtonStatus();
//   updateStorage();
// });

// $checkboxes.on("change", function(){
//   updateButtonStatus();
//   updateStorage();
// });

var checkboxValues = JSON.parse(localStorage.getItem('checkboxValues')) || {},
    $checkboxes = $("#checkbox-container :checkbox");

$checkboxes.on("change", function(){
  $checkboxes.each(function(){
    checkboxValues[this.id] = this.checked;
  });
  
  localStorage.setItem("checkboxValues", JSON.stringify(checkboxValues));
});

// On page load
$.each(checkboxValues, function(key, value) {
  $("#" + key).prop('checked', value);
});


// // On page load
// $.each(formValues, function(key, value) {
//   $("#" + key).prop('checked', value);
// });

// $button.text(formValues["buttonText"]);

