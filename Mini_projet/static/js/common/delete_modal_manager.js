class DeleteModalManager {
    constructor() {
        this.resolveCallback = null;
    }

    show(message = "Êtes-vous sûr de vouloir supprimer ?", confirmText = "Oui, supprimer", cancelText = "Annuler") {
        return new Promise((resolve) => {
            this.resolveCallback = resolve;

            const modalId = `delete-modal-${Date.now()}`;
            const modalHTML = `
                <div id="${modalId}" tabindex="-1" class="fixed inset-0 z-[9999] flex items-center justify-center bg-black bg-opacity-50">
                    <div class="relative w-full max-w-md p-4">
                        <div class="relative bg-white rounded-lg shadow">
                            <button type="button" class="absolute top-3 right-3 text-gray-400 hover:bg-gray-200 hover:text-gray-900 rounded-lg p-1.5" data-modal-hide="${modalId}">
                                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                            </button>
                            <div class="p-6 text-center">
                                <svg class="w-16 h-16 mx-auto text-red-600 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                                <h3 class="mb-6 text-lg font-medium text-gray-700">${message}</h3>
                                <div class="flex justify-center gap-4">
                                    <button id="confirm-btn-${modalId}" class="px-6 py-2.5 text-white bg-red-600 hover:bg-red-700 rounded-lg font-medium">
                                        ${confirmText}
                                    </button>
                                    <button id="cancel-btn-${modalId}" class="px-6 py-2.5 text-gray-700 bg-gray-200 hover:bg-gray-300 rounded-lg font-medium" data-modal-hide="${modalId}">
                                        ${cancelText}
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            `;

            document.body.insertAdjacentHTML('beforeend', modalHTML);
            const modalEl = document.getElementById(modalId);
            const modal = new Modal(modalEl, { placement: 'center' });

            const confirmBtn = document.getElementById(`confirm-btn-${modalId}`);
            const cancelBtn = document.getElementById(`cancel-btn-${modalId}`);

            const cleanup = () => {
                modal.hide();
                setTimeout(() => modalEl.remove(), 300);
            };

            confirmBtn.onclick = () => { resolve(true); cleanup(); };
            cancelBtn.onclick = () => { resolve(false); cleanup(); };
            modalEl.querySelector(`[data-modal-hide="${modalId}"]`).onclick = () => { resolve(false); cleanup(); };

            modal.show();
        });
    }
}

// CRUCIAL : on expose l'objet global
window.deleteModalManager = new DeleteModalManager();