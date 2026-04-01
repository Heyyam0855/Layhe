// Seller Dashboard JavaScript

// Image Upload Functionality
const imageUploadArea = document.getElementById('imageUploadArea');
const imageInput = document.getElementById('imageInput');
const imagePreviewContainer = document.getElementById('imagePreviewContainer');
let uploadedImages = [];

// Click to upload
imageUploadArea.addEventListener('click', () => {
    imageInput.click();
});

// File input change
imageInput.addEventListener('change', (e) => {
    handleFiles(e.target.files);
});

// Drag and drop functionality
imageUploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    imageUploadArea.classList.add('dragover');
});

imageUploadArea.addEventListener('dragleave', () => {
    imageUploadArea.classList.remove('dragover');
});

imageUploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    imageUploadArea.classList.remove('dragover');
    handleFiles(e.dataTransfer.files);
});

function handleFiles(files) {
    Array.from(files).forEach(file => {
        if (file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = (e) => {
                const imageData = {
                    file: file,
                    url: e.target.result
                };
                uploadedImages.push(imageData);
                displayImagePreview(imageData, uploadedImages.length - 1);
            };
            reader.readAsDataURL(file);
        }
    });
}

function displayImagePreview(imageData, index) {
    const preview = document.createElement('div');
    preview.className = 'image-preview';
    preview.innerHTML = `
        <img src="${imageData.url}" alt="Preview">
        <button type="button" class="image-preview-remove" data-index="${index}">
            <i class="fas fa-times"></i>
        </button>
    `;
    
    imagePreviewContainer.appendChild(preview);
    
    // Remove image functionality
    const removeBtn = preview.querySelector('.image-preview-remove');
    removeBtn.addEventListener('click', () => {
        uploadedImages.splice(index, 1);
        preview.remove();
        updateImageIndices();
    });
}

function updateImageIndices() {
    const removeButtons = imagePreviewContainer.querySelectorAll('.image-preview-remove');
    removeButtons.forEach((btn, index) => {
        btn.setAttribute('data-index', index);
    });
}

// Price Input Controls
const priceInput = document.getElementById('productPrice');
const priceIncrease = document.getElementById('priceIncrease');
const priceDecrease = document.getElementById('priceDecrease');
const priceError = document.getElementById('priceError');

priceIncrease.addEventListener('click', () => {
    const currentValue = parseFloat(priceInput.value) || 0;
    priceInput.value = (currentValue + 1).toFixed(2);
    validatePrice();
});

priceDecrease.addEventListener('click', () => {
    const currentValue = parseFloat(priceInput.value) || 0;
    if (currentValue > 0) {
        priceInput.value = Math.max(0, currentValue - 1).toFixed(2);
        validatePrice();
    }
});

priceInput.addEventListener('input', validatePrice);
priceInput.addEventListener('blur', validatePrice);

function validatePrice() {
    const value = priceInput.value.trim();
    if (!value || parseFloat(value) <= 0) {
        priceError.classList.remove('hidden');
        priceInput.style.borderColor = '#e74c3c';
    } else {
        priceError.classList.add('hidden');
        priceInput.style.borderColor = '#ddd';
    }
}

// Form Validation and Submission
const productForm = document.getElementById('productForm');
const saveBtn = document.getElementById('saveBtn');
const publishBtn = document.getElementById('publishBtn');

// Save changes (draft)
saveBtn.addEventListener('click', () => {
    if (validateForm()) {
        const formData = collectFormData();
        console.log('Saving draft:', formData);
        showNotification('Dəyişikliklər yadda saxlanıldı!', 'success');
    }
});

// Publish product
productForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    if (validateForm()) {
        const formData = collectFormData();
        console.log('Publishing product:', formData);
        showNotification('Məhsul uğurla dərc edildi!', 'success');
        
        // Reset form after successful submission
        setTimeout(() => {
            productForm.reset();
            uploadedImages = [];
            imagePreviewContainer.innerHTML = '';
            priceError.classList.add('hidden');
        }, 2000);
    }
});

function validateForm() {
    let isValid = true;
    
    // Validate product name
    const productName = document.getElementById('productName');
    if (!productName.value.trim()) {
        showFieldError(productName, 'Bu sahə boş qala bilməz');
        isValid = false;
    } else {
        clearFieldError(productName);
    }
    
    // Validate category
    const productCategory = document.getElementById('productCategory');
    if (!productCategory.value) {
        showFieldError(productCategory, 'Kateqoriya seçilməlidir');
        isValid = false;
    } else {
        clearFieldError(productCategory);
    }
    
    // Validate price
    const price = priceInput.value.trim();
    if (!price || parseFloat(price) <= 0) {
        priceError.classList.remove('hidden');
        priceInput.style.borderColor = '#e74c3c';
        isValid = false;
    } else {
        priceError.classList.add('hidden');
        priceInput.style.borderColor = '#ddd';
    }
    
    return isValid;
}

function showFieldError(field, message) {
    field.style.borderColor = '#e74c3c';
    let errorMsg = field.parentElement.querySelector('.field-error');
    if (!errorMsg) {
        errorMsg = document.createElement('span');
        errorMsg.className = 'error-message field-error';
        field.parentElement.appendChild(errorMsg);
    }
    errorMsg.textContent = message;
}

function clearFieldError(field) {
    field.style.borderColor = '#ddd';
    const errorMsg = field.parentElement.querySelector('.field-error');
    if (errorMsg) {
        errorMsg.remove();
    }
}

function collectFormData() {
    return {
        name: document.getElementById('productName').value,
        description: document.getElementById('productDescription').value,
        category: document.getElementById('productCategory').value,
        price: parseFloat(document.getElementById('productPrice').value),
        deliveryTime: document.getElementById('deliveryTime').value,
        images: uploadedImages.map(img => img.url)
    };
}

// Notification System
function showNotification(message, type = 'info') {
    const existingNotification = document.querySelector('.seller-notification');
    if (existingNotification) {
        existingNotification.remove();
    }
    
    const notification = document.createElement('div');
    notification.className = 'seller-notification';
    notification.textContent = message;
    
    const colors = {
        success: '#2ecc71',
        error: '#e74c3c',
        info: '#4A90E2'
    };
    
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background-color: ${colors[type] || colors.info};
        color: white;
        padding: 15px 25px;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        z-index: 10000;
        animation: slideInRight 0.3s ease-out;
        font-weight: 500;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease-out';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 3000);
}

// Add CSS animations for notifications
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Navigation active state
document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', function(e) {
        if (!this.classList.contains('active')) {
            document.querySelectorAll('.nav-item').forEach(nav => {
                nav.classList.remove('active');
            });
            this.classList.add('active');
        }
    });
});

// View Store button
document.querySelector('.btn-view-store').addEventListener('click', () => {
    window.location.href = 'index.html';
});

