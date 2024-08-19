function openModal(scriptPath, title) {
    const modal = document.getElementById('modal');
    const terminalContainer = document.getElementById('terminal-container');
    const modalTitle = document.getElementById('modal-title'); // Get the modal title element

    terminalContainer.innerHTML = ''; // Clear any previous content
    modalTitle.textContent = title; // Set the modal title dynamically

    // Insert the PyScript terminal
    terminalContainer.innerHTML = `<script type="py" src="${scriptPath}" terminal worker id="py-terminal"></script>`;

    // Show the modal
    modal.style.display = "block";
    document.body.style.overflow = 'hidden'; // Disable scrolling on the body
}

function closeModal() {
    const modal = document.getElementById('modal');
    modal.style.display = "none";
    document.getElementById('terminal-container').innerHTML = ''; // Clear the script
    document.body.style.overflow = 'auto'; // Enable scrolling again
}

window.onclick = function(event) {
    const modal = document.getElementById('modal');
    if (event.target == modal) {
        closeModal();
    }
}
