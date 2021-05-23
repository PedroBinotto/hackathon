[].forEach.call(document.getElementsByClassName('tags-input'), function (el) {
		let hiddenInput = document.createElement('input'),
				mainInput = document.createElement('input'),
				taglabel = document.getElementById('tags'),
				tags = [];

		hiddenInput.setAttribute('type', 'hidden');
		hiddenInput.setAttribute('name', el.getAttribute('data-name'));

		mainInput.setAttribute('type', 'text');

		mainInput.classList.add('form-control-lg');
		mainInput.classList.add('form-custom');
		mainInput.classList.add('main-input');

		mainInput.addEventListener('input', function () {
				let enteredTags = mainInput.value.split(',');
				if (enteredTags.length > 1) {
						enteredTags.forEach(function (t) {
								let filteredTag = filterTag(t);
								if (filteredTag.length > 0)
										addTag(filteredTag);
						});
						mainInput.value = '';
				}
		});

		mainInput.addEventListener('keydown', function (e) {
				let keyCode = e.which || e.keyCode;
				if (keyCode === 8 && mainInput.value.length === 0 && tags.length > 0) {
						removeTag(tags.length - 1);
				}
		});

		el.appendChild(mainInput);
		el.appendChild(hiddenInput);

		function addTag (text) {
				if (checkForDuplicates(text, tags)) {
						let tag = {
								text: text,
								element: document.createElement('span'),
						};

						tag.element.classList.add('tag-error');
						tag.element.textContent = tag.text;

						el.insertBefore(tag.element, mainInput);

						setTimeout(function(){
								el.removeChild(tag.element);
						}, 1300);

						refreshTags();
				}

				else if (tags.length >= 4) {
					mainInput.classList.add('tags-input-flasher');
					taglabel.classList.add('tags-input-flasher');
					setTimeout(function(){
						taglabel.classList.remove('tags-input-flasher');
							mainInput.classList.remove('tags-input-flasher');
					}, 400);

					refreshTags();
				}

				else {
						let tag = {
								text: text,
								element: document.createElement('span'),
						};

						tag.element.classList.add('tag');
						tag.element.textContent = tag.text;

						let closeBtn = document.createElement('span');
						closeBtn.classList.add('close');
						closeBtn.addEventListener('click', function () {
								removeTag(tags.indexOf(tag));
						});
						tag.element.appendChild(closeBtn);

						tags.push(tag);

						el.insertBefore(tag.element, mainInput);

						refreshTags();
				}
		}

		function removeTag (index) {
				let tag = tags[index];
				tags.splice(index, 1);
				el.removeChild(tag.element);
				refreshTags();
		}

		function refreshTags () {
				let tagsList = [];
				tags.forEach(function (t) {
						tagsList.push(t.text);	//Acessar lista de texto (tags)
				});
				hiddenInput.value = tagsList.join(',');	// Define valor (usado no backend)
		}

		function checkForDuplicates (tag, list) {
				let tagsList = [];
				tags.forEach(function (t) {
						tagsList.push(t.text);
				});

				for (i = 0; i < tagsList.length; i++) {
						if (tag.localeCompare(tagsList[i]) == 0) {
								return true;
						}
				}
				return false;
		}

		function filterTag (tag) {
				return tag.replace(/[^\w -]/g, '').trim().replace(/\W+/g, '-');
		}
});

function myFunction() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

function openPanel(evt, panelName) {
	var i, x, tablinks;
	x = document.getElementsByClassName("panel");
	for (i = 0; i < x.length; i++) {
		x[i].style.display = "none";
	}
	tablinks = document.getElementsByClassName("tablink");
	for (i = 0; i < x.length; i++) {
		tablinks[i].className = tablinks[i].className.replace(" tab-active", "");
	}
	document.getElementById(panelName).style.display = "block";
	evt.currentTarget.className += " tab-active";
}

$('.myIframe').css('height', (document.getElementsByClassName('myIframe')[0].clientWidth * 9)/16 +'px');






/*
$('.myIframe').css('height', $(window).height()/1.5+'px');

// Pin footer div to the bottom of the page when content is shorter than the viewport height
var footer = document.getElementById("footer");
var stickyBottom = window.innerHeight - footer.offsetTop;

window.onload = function() {myFooter()};

function myFooter() {
  if (stickyBottom > 0) {
    footer.classList.add("stickyBottom");
  }
  else {
    footer.classList.remove("stickyBottom");
  }
}
*/
