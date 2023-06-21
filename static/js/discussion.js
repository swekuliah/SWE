// Select the necessary elements
const forumContainer = document.getElementById('forum');
const postForm = document.getElementById('postForm');
const usernameInput = document.getElementById('username');
const messageInput = document.getElementById('message');
const replyForm = document.getElementById('replyForm');
const replyUsernameInput = document.getElementById('replyUsername');
const replyMessageInput = document.getElementById('replyMessage');
let selectedMessage = null;

// Handle form submission
postForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Get the input values
    const username = usernameInput.value;
    const message = messageInput.value;

    if (selectedMessage) {
        // Add reply message to the selected message
        const replyElement = createMessageElement(username, message);
        replyElement.classList.add('reply-message');

        const replyForm = selectedMessage.querySelector('.reply-form');
        if (replyForm) {
            selectedMessage.removeChild(replyForm);
        }

        selectedMessage.appendChild(replyElement);
        hideReplyForm();
    } else {
        // Create a new message element
        const messageElement = createMessageElement(username, message);

        // Append the new message to the forum container
        forumContainer.appendChild(messageElement);
    }

    // Clear the input fields
    usernameInput.value = '';
    messageInput.value = '';
});

// Create a new message element
function createMessageElement(username, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');

    const header = document.createElement('div');
    header.innerHTML = `<strong>${username}:</strong> ${message}`;
    messageElement.appendChild(header);

    const replyButton = document.createElement('button');
    replyButton.textContent = 'Reply';
    replyButton.addEventListener('click', function() {
        showReplyForm(messageElement);
    });
    messageElement.appendChild(replyButton);

    return messageElement;
}

// Show the reply form
function showReplyForm(messageElement) {
    selectedMessage = messageElement;

    // Hide the original comment section
    postForm.style.display = 'none';

    // Show the reply form
    replyForm.style.display = 'block';
    replyUsernameInput.value = '';
    replyMessageInput.value = '';
}

// Hide the reply form
function hideReplyForm() {
    selectedMessage = null;

    // Show the original comment section
    postForm.style.display = 'block';

    // Hide the reply form
    replyForm.style.display = 'none';
}

// Handle reply form submission
document.getElementById('replySubmit').addEventListener('click', function() {
    const username = replyUsernameInput.value;
    const message = replyMessageInput.value;

    if (selectedMessage && username && message) {
        const replyElement = createMessageElement(username, message);
        replyElement.classList.add('reply-message');

        const replyForm = selectedMessage.querySelector('.reply-form');
        if (replyForm) {
            selectedMessage.removeChild(replyForm);
        }

        selectedMessage.appendChild(replyElement);
        hideReplyForm();
    }
});

// Cancel reply form
document.getElementById('replyCancel').addEventListener('click', function() {
    hideReplyForm();
});

// Add event listener for page load
window.addEventListener('load', function() {
    const backButton = document.getElementById('backButton');
    setTimeout(function() {
        backButton.classList.add('visible');
    }, 1000); // Add delay to show the button with animation after 1 second
});

// Go back to the previous page
function goBack() {
    window.history.back();
}
