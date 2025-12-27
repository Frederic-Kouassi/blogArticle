/**
 * Handles Django messages and converts them to toast notifications
 * This script should be included after the toast_manager.js
 */
document.addEventListener('DOMContentLoaded', function() {
    // Check if toastManager is available
    if (typeof window.toastManager === 'undefined') {
        console.warn('ToastManager not found. Make sure toast_manager.js is loaded first.');
        return;
    }

    // Get all Django messages from the template
    const messages = document.querySelectorAll('.messages .message, .alert, .django-messages .message');
    
    messages.forEach(function(messageElement) {
        const messageText = messageElement.textContent.trim();
        const messageType = getMessageType(messageElement);
        
        // Use the toast manager directly
        window.toastManager.buildToast()
            .setMessage(messageText)
            .setType(messageType)
            .setPosition('top-right')
            .setDuration(4000)
            .show();
        
        // Remove the original message element
        messageElement.remove();
    });
    
    // Also check for messages in the Django messages framework
    const djangoMessages = document.querySelectorAll('.messages li, .messages .alert');
    djangoMessages.forEach(function(messageElement) {
        const messageText = messageElement.textContent.trim();
        const messageType = getMessageType(messageElement);
        
        // Use the toast manager directly
        window.toastManager.buildToast()
            .setMessage(messageText)
            .setType(messageType)
            .setPosition('top-right')
            .setDuration(4000)
            .show();
        
        // Remove the original message element
        messageElement.remove();
    });
});

/**
 * Determines the message type based on CSS classes
 * @param {HTMLElement} element - The message element
 * @returns {string} - The message type (success, error, warning, info)
 */
function getMessageType(element) {
    const classList = element.classList;
    
    if (classList.contains('success') || classList.contains('alert-success')) {
        return 'success';
    } else if (classList.contains('error') || classList.contains('alert-danger') || classList.contains('alert-error')) {
        return 'error';
    } else if (classList.contains('warning') || classList.contains('alert-warning')) {
        return 'warning';
    } else if (classList.contains('info') || classList.contains('alert-info')) {
        return 'info';
    }
    
    // Default to success if no specific type is found
    return 'success';
}
