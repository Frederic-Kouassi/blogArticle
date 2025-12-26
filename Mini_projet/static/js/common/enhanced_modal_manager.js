/**
 * Enhanced Modal Manager with beautiful styling and French translations
 * Provides a comprehensive modal system for CRUD operations
 * @class
 */
class EnhancedModalManager {
    constructor() {
        console.log('EnhancedModalManager: Initialisation...');
        this.modal = null;
        this.modalInstance = null;
        this.resolveCallback = null;
        this.rejectCallback = null;
        this.isClosing = false;
        this.injectStyles();
        
        if (typeof Modal === 'undefined') {
            console.warn('EnhancedModalManager: Flowbite Modal non chargé, nouvelle tentative prévue si nécessaire');
        } else {
            console.log('EnhancedModalManager: Flowbite Modal disponible');
        }
        
        console.log('EnhancedModalManager: Initialisé avec succès');
    }

    injectStyles() {
        const styles = `
            .enhanced-modal {
                backdrop-filter: blur(8px);
                background: rgba(0, 0, 0, 0.4);
            }
            .enhanced-modal-content {
                background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
                border-radius: 20px;
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
                border: 1px solid rgba(255, 255, 255, 0.2);
                backdrop-filter: blur(10px);
                max-height: 90vh;
                overflow-y: auto;
            }
            .enhanced-modal-header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border-radius: 20px 20px 0 0;
                padding: 1.5rem;
                position: relative;
            }
            .enhanced-modal-title {
                font-size: 1.5rem;
                font-weight: 700;
                margin: 0;
                display: flex;
                align-items: center;
                gap: 0.75rem;
            }
            .enhanced-modal-close {
                position: absolute;
                top: 1rem;
                right: 1rem;
                background: rgba(255, 255, 255, 0.2);
                border: none;
                color: white;
                width: 2.5rem;
                height: 2.5rem;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                transition: all 0.3s ease;
                backdrop-filter: blur(10px);
            }
            .enhanced-modal-close:hover {
                background: rgba(255, 255, 255, 0.3);
                transform: scale(1.1);
            }
            .enhanced-modal-body {
                padding: 2rem;
            }
            .enhanced-form-group {
                margin-bottom: 1.5rem;
            }
            .enhanced-form-label {
                display: block;
                font-weight: 600;
                color: #374151;
                margin-bottom: 0.5rem;
                font-size: 0.875rem;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }
            .enhanced-form-input {
                width: 100%;
                padding: 0.875rem 1rem;
                border: 2px solid #e5e7eb;
                border-radius: 12px;
                font-size: 1rem;
                transition: all 0.3s ease;
                background: rgba(255, 255, 255, 0.8);
                backdrop-filter: blur(10px);
            }
            .enhanced-form-input:focus {
                outline: none;
                border-color: #667eea;
                box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
                transform: translateY(-1px);
            }
            .enhanced-form-select {
                width: 100%;
                padding: 0.875rem 1rem;
                border: 2px solid #e5e7eb;
                border-radius: 12px;
                font-size: 1rem;
                transition: all 0.3s ease;
                background: rgba(255, 255, 255, 0.8);
                backdrop-filter: blur(10px);
                cursor: pointer;
            }
            .enhanced-form-select:focus {
                outline: none;
                border-color: #667eea;
                box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
                transform: translateY(-1px);
            }
            .enhanced-form-textarea {
                width: 100%;
                padding: 0.875rem 1rem;
                border: 2px solid #e5e7eb;
                border-radius: 12px;
                font-size: 1rem;
                transition: all 0.3s ease;
                background: rgba(255, 255, 255, 0.8);
                backdrop-filter: blur(10px);
                resize: vertical;
                min-height: 100px;
            }
            .enhanced-form-textarea:focus {
                outline: none;
                border-color: #667eea;
                box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
                transform: translateY(-1px);
            }
            .enhanced-checkbox-group {
                display: flex;
                align-items: center;
                gap: 0.75rem;
                padding: 1rem;
                background: rgba(102, 126, 234, 0.05);
                border-radius: 12px;
                border: 2px solid rgba(102, 126, 234, 0.1);
            }
            .enhanced-checkbox {
                width: 1.25rem;
                height: 1.25rem;
                accent-color: #667eea;
                cursor: pointer;
            }
            .enhanced-checkbox-label {
                font-weight: 600;
                color: #374151;
                cursor: pointer;
            }
            .enhanced-modal-footer {
                padding: 1.5rem 2rem;
                background: rgba(248, 250, 252, 0.8);
                border-radius: 0 0 20px 20px;
                display: flex;
                justify-content: flex-end;
                gap: 1rem;
            }
            .enhanced-btn {
                padding: 0.875rem 2rem;
                border-radius: 12px;
                font-weight: 600;
                font-size: 0.875rem;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                transition: all 0.3s ease;
                cursor: pointer;
                border: none;
                display: flex;
                align-items: center;
                gap: 0.5rem;
                min-width: 120px;
                justify-content: center;
            }
            .enhanced-btn-primary {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            }
            .enhanced-btn-primary:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
            }
            .enhanced-btn-secondary {
                background: rgba(107, 114, 128, 0.1);
                color: #6b7280;
                border: 2px solid rgba(107, 114, 128, 0.2);
            }
            .enhanced-btn-secondary:hover {
                background: rgba(107, 114, 128, 0.2);
                transform: translateY(-1px);
            }
            .enhanced-btn-danger {
                background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
                color: white;
                box-shadow: 0 4px 15px rgba(239, 68, 68, 0.4);
            }
            .enhanced-btn-danger:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 25px rgba(239, 68, 68, 0.6);
            }
            .modal-enter {
                animation: modalEnter 0.4s ease-out forwards;
            }
            .modal-exit {
                animation: modalExit 0.3s ease-in forwards;
            }
            @keyframes modalEnter {
                from { opacity: 0; transform: scale(0.9) translateY(-20px); }
                to { opacity: 1; transform: scale(1) translateY(0); }
            }
            @keyframes modalExit {
                from { opacity: 1; transform: scale(1) translateY(0); }
                to { opacity: 0; transform: scale(0.9) translateY(-20px); }
            }
            @media (max-width: 768px) {
                .enhanced-modal-content { margin: 1rem; max-height: 95vh; }
                .enhanced-modal-body { padding: 1.5rem; }
                .enhanced-modal-footer { padding: 1rem 1.5rem; flex-direction: column; }
                .enhanced-btn { width: 100%; }
            }
        `;
        const styleSheet = document.createElement('style');
        styleSheet.textContent = styles;
        document.head.appendChild(styleSheet);
    }

    createLevelModal({ title, data = {}, isEdit = false }) {
        console.log('EnhancedModalManager: Création du modal de niveau avec titre:', title);
        console.log('EnhancedModalManager: Données:', data);
        const modalId = `enhanced-level-modal-${Date.now()}`;
        this.modal = document.createElement('div');
        this.modal.id = modalId;
        this.modal.className = 'enhanced-modal hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full';
        this.modal.setAttribute('data-modal', 'true');

        this.modal.innerHTML = `
            <div class="relative p-4 w-full max-w-2xl max-h-full">
                <div class="enhanced-modal-content modal-enter">
                    <div class="enhanced-modal-header">
                        <h3 class="enhanced-modal-title">
                            <i class="fas fa-graduation-cap"></i>
                            ${title}
                        </h3>
                        <button type="button" class="enhanced-modal-close" data-modal-hide="${modalId}">
                            <i class="fas fa-times"></i>
                        </button>
                    </div>
                    <div class="enhanced-modal-body">
                        <form id="enhanced-level-form">
                            <input type="hidden" id="enhanced-level-id" value="${data.id || ''}">
                            <div class="enhanced-form-group">
                                <label class="enhanced-form-label" for="enhanced-level-name">
                                    <i class="fas fa-tag"></i> Nom du niveau
                                </label>
                                <input type="text" id="enhanced-level-name" class="enhanced-form-input" 
                                       value="${data.name || ''}" required>
                            </div>
                            <div class="enhanced-form-group">
                                <label class="enhanced-form-label" for="enhanced-level-price">
                                    <i class="fas fa-money-bill-wave"></i> Prix (FCFA)
                                </label>
                                <input type="number" id="enhanced-level-price" class="enhanced-form-input" 
                                       value="${data.price || ''}" step="0.01" required>
                            </div>
                            <div class="enhanced-form-group">
                                <label class="enhanced-form-label" for="enhanced-level-prerequisites">
                                    <i class="fas fa-list-check"></i> Prérequis
                                </label>
                                <textarea id="enhanced-level-prerequisites" class="enhanced-form-textarea" 
                                          placeholder="Décrivez les prérequis pour ce niveau...">${data.prerequisites || ''}</textarea>
                            </div>
                            <div class="enhanced-form-group">
                                <label class="enhanced-form-label" for="enhanced-level-objectives">
                                    <i class="fas fa-target"></i> Objectifs d'apprentissage
                                </label>
                                <textarea id="enhanced-level-objectives" class="enhanced-form-textarea" 
                                          placeholder="Décrivez les objectifs d'apprentissage...">${data.learning_objectives || ''}</textarea>
                            </div>
                            <div class="enhanced-form-group">
                                <label class="enhanced-form-label" for="enhanced-level-description">
                                    <i class="fas fa-align-left"></i> Description
                                </label>
                                <textarea id="enhanced-level-description" class="enhanced-form-textarea" 
                                          placeholder="Décrivez ce niveau...">${data.description || ''}</textarea>
                            </div>
                            <div class="enhanced-checkbox-group">
                                <input type="checkbox" id="enhanced-level-active" class="enhanced-checkbox" 
                                       ${data.is_active !== false ? 'checked' : ''}>
                                <label for="enhanced-level-active" class="enhanced-checkbox-label">
                                    <i class="fas fa-toggle-on"></i> Niveau actif
                                </label>
                            </div>
                        </form>
                    </div>
                    <div class="enhanced-modal-footer">
                        <button type="button" class="enhanced-btn enhanced-btn-secondary" data-modal-hide="${modalId}">
                            <i class="fas fa-times"></i> Annuler
                        </button>
                        <button type="submit" form="enhanced-level-form" class="enhanced-btn enhanced-btn-primary">
                            <i class="fas fa-save"></i> ${isEdit ? 'Mettre à jour' : 'Créer'}
                        </button>
                    </div>
                </div>
            </div>
        `;

        document.body.appendChild(this.modal);
        console.log('EnhancedModalManager: Modal de niveau créé et ajouté au DOM');
        this.initializeModal(modalId);
    }

    createInstallmentModal({ title, data = {}, levels = [], installmentTypes = [], isEdit = false }) {
        const modalId = `enhanced-installment-modal-${Date.now()}`;
        this.modal = document.createElement('div');
        this.modal.id = modalId;
        this.modal.className = 'enhanced-modal hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full';
        this.modal.setAttribute('data-modal', 'true');

        const levelOptions = levels.map(level => 
            `<option value="${level.id}" ${data.level_id == level.id ? 'selected' : ''}>${level.name}</option>`
        ).join('');

        const installmentTypeOptions = installmentTypes.map(([value, label]) => 
            `<option value="${value}" ${data.installment_type == value ? 'selected' : ''}>${label}</option>`
        ).join('');

        this.modal.innerHTML = `
            <div class="relative p-4 w-full max-w-2xl max-h-full">
                <div class="enhanced-modal-content modal-enter">
                    <div class="enhanced-modal-header">
                        <h3 class="enhanced-modal-title">
                            <i class="fas fa-credit-card"></i>
                            ${title}
                        </h3>
                        <button type="button" class="enhanced-modal-close" data-modal-hide="${modalId}">
                            <i class="fas fa-times"></i>
                        </button>
                    </div>
                    <div class="enhanced-modal-body">
                        <form id="enhanced-installment-form">
                            <input type="hidden" id="enhanced-installment-id" value="${data.id || ''}">
                            <div class="enhanced-form-group">
                                <label class="enhanced-form-label" for="enhanced-installment-level">
                                    <i class="fas fa-graduation-cap"></i> Niveau
                                </label>
                                <select id="enhanced-installment-level" class="enhanced-form-select" required>
                                    <option value="">Sélectionner un niveau</option>
                                    ${levelOptions}
                                </select>
                            </div>
                            <div class="enhanced-form-group">
                                <label class="enhanced-form-label" for="enhanced-number-installments">
                                    <i class="fas fa-hashtag"></i> Nombre de tranches
                                </label>
                                <input type="number" id="enhanced-number-installments" class="enhanced-form-input" 
                                       value="${data.number_of_installments || 1}" min="1" max="10">
                            </div>
                            <div class="enhanced-form-group">
                                <label class="enhanced-form-label" for="enhanced-installment-title">
                                    <i class="fas fa-tag"></i> Titre
                                </label>
                                <input type="text" id="enhanced-installment-title" class="enhanced-form-input" 
                                       value="${data.title || ''}" required>
                            </div>
                            <div class="enhanced-form-group">
                                <label class="enhanced-form-label" for="enhanced-installment-amount">
                                    <i class="fas fa-money-bill-wave"></i> Montant (FCFA)
                                </label>
                                <input type="number" id="enhanced-installment-amount" class="enhanced-form-input" 
                                       value="${data.amount || ''}" step="0.01" required>
                            </div>
                            <div class="enhanced-form-group">
                                <label class="enhanced-form-label" for="enhanced-installment-type">
                                    <i class="fas fa-list"></i> Type de tranche
                                </label>
                                <select id="enhanced-installment-type" class="enhanced-form-select">
                                    ${installmentTypeOptions}
                                </select>
                            </div>
                            <div class="enhanced-form-group">
                                <label class="enhanced-form-label" for="enhanced-installment-days-offset">
                                    <i class="fas fa-calendar-days"></i> Délai en jours
                                </label>
                                <input type="number" id="enhanced-installment-days-offset" class="enhanced-form-input" 
                                       value="${data.days_offset || 0}" min="0">
                            </div>
                            <div class="enhanced-form-group">
                                <label class="enhanced-form-label" for="enhanced-installment-due-date">
                                    <i class="fas fa-calendar"></i> Date d'échéance
                                </label>
                                <input type="date" id="enhanced-installment-due-date" class="enhanced-form-input" 
                                       value="${data.due_date || ''}">
                            </div>
                            <div class="enhanced-form-group">
                                <label class="enhanced-form-label" for="enhanced-installment-late-fee">
                                    <i class="fas fa-exclamation-triangle"></i> Frais de retard (FCFA)
                                </label>
                                <input type="number" id="enhanced-installment-late-fee" class="enhanced-form-input" 
                                       value="${data.late_fee || 0}" step="0.01">
                            </div>
                            <div class="enhanced-form-group">
                                <label class="enhanced-form-label" for="enhanced-installment-description">
                                    <i class="fas fa-align-left"></i> Description
                                </label>
                                <textarea id="enhanced-installment-description" class="enhanced-form-textarea" 
                                          placeholder="Description de la tranche...">${data.description || ''}</textarea>
                            </div>
                            <div class="enhanced-checkbox-group">
                                <input type="checkbox" id="enhanced-installment-mandatory" class="enhanced-checkbox" 
                                       ${data.is_mandatory !== false ? 'checked' : ''}>
                                <label for="enhanced-installment-mandatory" class="enhanced-checkbox-label">
                                    <i class="fas fa-exclamation-circle"></i> Tranche obligatoire
                                </label>
                            </div>
                        </form>
                    </div>
                    <div class="enhanced-modal-footer">
                        <button type="button" class="enhanced-btn enhanced-btn-secondary" data-modal-hide="${modalId}">
                            <i class="fas fa-times"></i> Annuler
                        </button>
                        <button type="submit" form="enhanced-installment-form" class="enhanced-btn enhanced-btn-primary">
                            <i class="fas fa-save"></i> ${isEdit ? 'Mettre à jour' : 'Créer'}
                        </button>
                    </div>
                </div>
            </div>
        `;

        document.body.appendChild(this.modal);
        this.initializeModal(modalId);
    }

    createDeleteModal({ title, message, itemName }) {
        const modalId = `enhanced-delete-modal-${Date.now()}`;
        this.modal = document.createElement('div');
        this.modal.id = modalId;
        this.modal.className = 'enhanced-modal hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full';
        this.modal.setAttribute('data-modal', 'true');

        this.modal.innerHTML = `
            <div class="relative p-4 w-full max-w-md max-h-full">
                <div class="enhanced-modal-content modal-enter">
                    <div class="enhanced-modal-header" style="background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);">
                        <h3 class="enhanced-modal-title">
                            <i class="fas fa-exclamation-triangle"></i>
                            ${title}
                        </h3>
                        <button type="button" class="enhanced-modal-close" data-modal-hide="${modalId}">
                            <i class="fas fa-times"></i>
                        </button>
                    </div>
                    <div class="enhanced-modal-body text-center">
                        <div class="mb-6">
                            <div class="w-20 h-20 mx-auto mb-4 bg-red-100 rounded-full flex items-center justify-center">
                                <i class="fas fa-trash-alt text-red-600 text-3xl"></i>
                            </div>
                            <h4 class="text-xl font-semibold text-gray-900 mb-2">${message}</h4>
                            <p class="text-gray-600">Cette action ne peut pas être annulée.</p>
                        </div>
                    </div>
                    <div class="enhanced-modal-footer">
                        <button type="button" class="enhanced-btn enhanced-btn-secondary" data-modal-hide="${modalId}">
                            <i class="fas fa-times"></i> Annuler
                        </button>
                        <button type="button" class="enhanced-btn enhanced-btn-danger" id="confirm-delete-btn">
                            <i class="fas fa-trash-alt"></i> Supprimer
                        </button>
                    </div>
                </div>
            </div>
        `;

        document.body.appendChild(this.modal);
        this.initializeModal(modalId);
    }

    initializeModal(modalId) {
        console.log('EnhancedModalManager: Initialisation du modal avec ID:', modalId);
        
        if (typeof Modal === 'undefined') {
            console.error('EnhancedModalManager: Classe Modal introuvable ! Assurez-vous que Flowbite est chargé.');
            setTimeout(() => {
                if (typeof Modal !== 'undefined') {
                    console.log('EnhancedModalManager: Classe Modal chargée après délai, nouvelle tentative...');
                    this.initializeModal(modalId);
                } else {
                    console.error('EnhancedModalManager: Classe Modal toujours indisponible après délai');
                }
            }, 1000);
            return;
        }
        console.log('EnhancedModalManager: Classe Modal disponible');
        
        try {
            this.modalInstance = new Modal(this.modal, {
                backdrop: 'dynamic',
                backdropClasses: 'bg-gray-900/50 fixed inset-0 z-40',
                closable: true,
                onHide: () => {
                    if (!this.isClosing) {
                        this.isClosing = true;
                        if (this.resolveCallback) {
                            this.resolveCallback(false);
                        }
                        this.closeModal();
                    }
                }
            });
            console.log('EnhancedModalManager: Instance de modal créée avec succès');
        } catch (error) {
            console.error('EnhancedModalManager: Erreur lors de la création de l’instance de modal:', error);
        }

        const closeBtn = this.modal.querySelector(`[data-modal-hide="${modalId}"]`);
        const confirmBtn = this.modal.querySelector('#confirm-delete-btn');
        
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                if (this.resolveCallback) {
                    this.resolveCallback(false);
                }
                this.modalInstance.hide();
            });
        }

        if (confirmBtn) {
            confirmBtn.addEventListener('click', () => {
                if (this.resolveCallback) {
                    this.resolveCallback(true);
                }
                this.modalInstance.hide();
            });
        }
    }

    show() {
        console.log('EnhancedModalManager: Affichage du modal');
        return new Promise((resolve) => {
            this.resolveCallback = resolve;
            try {
                this.modalInstance.show();
                console.log('EnhancedModalManager: Modal affiché avec succès');
            } catch (error) {
                console.error('EnhancedModalManager: Erreur lors de l’affichage du modal:', error);
            }
        });
    }

    closeModal() {
        if (this.modal && this.modalInstance && !this.isClosing) {
            this.isClosing = true;
            this.modal.remove();
            this.modal = null;
            this.modalInstance = null;
            this.resolveCallback = null;
            this.isClosing = false;
        }
    }
}

const enhancedModalManager = new EnhancedModalManager();
window.enhancedModalManager = enhancedModalManager;