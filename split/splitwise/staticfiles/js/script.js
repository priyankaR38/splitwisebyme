/* script.js */

// Add your custom JavaScript code here
console.log("Script loaded!");

// Example JavaScript functionality


// JavaScript code for your Django project

// Wait for the DOM to be ready
document.addEventListener("DOMContentLoaded", function() {
  // Get the add member form
  var addMemberForm = document.getElementById("add-member-form");

  if (addMemberForm) {
    // Add event listener for form submission
    addMemberForm.addEventListener("submit", function(event) {
      event.preventDefault(); // Prevent the default form submission

      // Get the member email input value
      var memberEmail = document.getElementById("member-email").value;

      // AJAX request to add the member to the group
      var xhr = new XMLHttpRequest();
      xhr.open("POST", addMemberForm.getAttribute("data-url"), true);
      xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
      xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
          // Redirect to the group details page
          window.location.href = xhr.responseURL;
        }
      };
      xhr.send("member_email=" + encodeURIComponent(memberEmail));
    });
  }
});
