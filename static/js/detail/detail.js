var dropdown = document.getElementsByClassName("crop");
for (var i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function () {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.classList === "active") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}
function loadDoc(link) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = () => {
    document.getElementById("demo").innerHTML = this.responseText;
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", link, true);
  xhttp.send();
}