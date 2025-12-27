/**
 * Manages toast notifications for success and error messages using ToastManager.
 * Supports internationalization with gettext.
 * @class
 */
class NotificationManager {
    constructor() {
        this.toastManager = window.toastManager;
    }

    /**
     * Shows a success notification.
     * @param {string} message - The success message to display.
     */
    showSuccess(message) {
        this.toastManager.buildToast()
            .setMessage(message)
            .setType('success')
            .setPosition('top-right')
            .setDuration(4000)
            .show();
    }

    /**
     * Shows an error notification.
     * @param {string} message - The error message to display.
     */
    showError(message) {
        this.toastManager.buildToast()
            .setMessage(message)
            .setType('error')
            .setPosition('top-right')
            .setDuration(4000)
            .show();
    }
}

// Export a singleton instance
const notificationManager = new NotificationManager();
window.notificationManager = notificationManager;