// Function to close a single message container
function closeMessageContainer(container) {
    container.style.opacity = '0';
    setTimeout(function() {
        container.style.display = 'none';
    }, 500);
}

// Close all message containers after 5 seconds
setTimeout(function() {
    var messageContainers = document.querySelectorAll('.message-container');
    messageContainers.forEach(function(container) {
        closeMessageContainer(container);
    });
}, 5000);

console.log("hello World");