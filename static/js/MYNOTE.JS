// // script.js
// document.getElementById('noteForm').addEventListener('submit', function(e) {
//     e.preventDefault();
//     const title = document.getElementById('title').value;
//     const content = document.getElementById('content').value;
//     const attachment = document.getElementById('attachment').files[0];

//     const formData = new FormData();
//     formData.append('title', title);
//     formData.append('content', content);
//     formData.append('attachment', attachment);

//     fetch('/api/notes', {
//         method: 'POST',
//         body: formData
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Note saved:', data);
//         // Reset form fields
//         document.getElementById('title').value = '';
//         document.getElementById('content').value = '';
//         document.getElementById('attachment').value = '';
//         // Refresh note list
//         fetchNotes();
//     })
//     .catch(error => console.error('Error saving note:', error));
// });

// function fetchNotes() {
//     fetch('/api/notes')
//     .then(response => response.json())
//     .then(data => {
//         const noteList = document.getElementById('noteList');
//         noteList.innerHTML = '';

//         data.forEach(note => {
//             const li = document.createElement('li');
//             li.textContent = note.title;
//             noteList.appendChild(li);
//         });
//     })
//     .catch(error => console.error('Error fetching notes:', error));
// }

// // Initial fetch to load existing notes
// fetchNotes();
