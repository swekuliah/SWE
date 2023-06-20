function switchToEditMode() {
  // Enable input fields
  document.getElementById("display-name").disabled = false;
  document.getElementById("display-email").disabled = false;

  // Show the edit mode buttons
  document.getElementById("edit-mode-buttons").style.display = "block";

  // Hide the edit button
  document.getElementById("edit-btn").style.display = "none";

  // Show the edit profile picture button
  document.getElementById("edit-profile-btn").style.display = "block";
}

function saveChanges() {
  // Disable input fields
  document.getElementById("display-name").disabled = true;
  document.getElementById("display-email").disabled = true;

  // Hide the edit mode buttons
  document.getElementById("edit-mode-buttons").style.display = "none";

  // Show the edit button
  document.getElementById("edit-btn").style.display = "block";

  // Hide the edit profile picture button
  document.getElementById("edit-profile-btn").style.display = "none";

  // Perform additional save operations here
}

// Rest of the code remains the same


function changePassword() {
  // Implement change password functionality here
}

function editProfilePicture() {
  // Implement edit profile picture functionality here
}

function editName() {
  // Implement edit name functionality here
}

function editEmail() {
  // Implement edit email functionality here
}
