(function() {
  'use strict';
	window['date'] = Date().toLocaleString();
  var snackbarContainer = document.querySelector('#notice-toast');
  var showToastButton = document.querySelector('#notice-toast-show');
  showToastButton.addEventListener('click', function() {
    'use strict';
    var data = {message: date + ' 시 기준 새로운 공지를 가져왔어요~ 뿅!' };
    snackbarContainer.MaterialSnackbar.showSnackbar(data);
		var refresh = document.getElementById('do-refresh-notice');
		refresh.click();
  });
}());
