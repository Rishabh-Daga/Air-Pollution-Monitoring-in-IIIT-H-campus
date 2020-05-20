function render_line() {
    var parameter = document.getElementById("myform").elements[0].value;
    var node_number = document.getElementById("myform").elements[1].value;
    var period = document.getElementById("myform").elements[2].value;
    if (period === "daily") {
      var date = document.getElementById("myform").elements[3].value;
      document.getElementById("image").innerHTML="<img src=\"../img/line/"+parameter+"_"+node_number+"_day_"+date+".png\" class=\"center\">";
    }
    else {
      document.getElementById("image").innerHTML="<img src=\"../img/line/"+parameter+"_"+node_number+"_week.png\" class=\"center\">";
    } 
}

function show_date() {
  var node_number = document.getElementById("myform").elements[1].value;
  var period = document.getElementById("myform").elements[2].value;
  if (period === "daily") {
    document.getElementById("date").style.visibility="visible";
  }
  else {
    document.getElementById("date").style.visibility="hidden";
  }
}

// for line1
var expanded = false;
function showCheckboxes() {
  var checkboxes = document.getElementById("checkboxes");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}
// for line 1 ^

  window.onscroll = function() {myFunction()};
  var navbar = document.getElementById("navbar");
  var sticky = navbar.offsetTop;
  
  function myFunction() {
    if (window.pageYOffset >= sticky) {
      navbar.classList.add("sticky")
    } else {
      navbar.classList.remove("sticky");
    }
  }