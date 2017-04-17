$(document).ready(function(){

	var textInput = $('#newFriend');
	var submitButton = $('#submitButton');
	var friendsList = $('#friendsList');


	submitButton.on('click', function(e){
		e.preventDefault();
		var newName = textInput.val();
		$.ajax(
			{
				url: "http://127.0.0.1:3000/addfriend/" + newName,
				method:"GET",
				success: function(result){
				var newLi = $('<li> ' + newName + ' </li>');
				friendsList.append(newLi);
				}


			}
		);
		




	});








});