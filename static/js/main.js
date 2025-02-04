// add hovered class to selected list item
let list = document.querySelectorAll(".navigation li");

function activeLink() {
  list.forEach((item) => {
    item.classList.remove("hovered");
  });
  this.classList.add("hovered");
}

list.forEach((item) => item.addEventListener("mouseover", activeLink));

// Menu Toggle
let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");

toggle.onclick = function () {
  navigation.classList.toggle("active");
  main.classList.toggle("active");
};

// Toggle dropdowns on click
document.querySelectorAll(".dropdown > a").forEach(dropdownToggle => {
  dropdownToggle.addEventListener("click", function(event) {
      event.preventDefault(); // Prevent default link behavior

      // Close other open dropdowns
      document.querySelectorAll(".dropdown.open").forEach(openDropdown => {
          if (openDropdown !== this.parentElement) {
              openDropdown.classList.remove("open");
          }
      });

      // Toggle the clicked dropdown
      this.parentElement.classList.toggle("open");
  });
});



