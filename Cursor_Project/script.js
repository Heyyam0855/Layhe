// Search functionality
const searchInput = document.getElementById('searchInput');
const searchIcon = document.querySelector('.search-box i');

searchInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        performSearch();
    }
});

searchIcon.addEventListener('click', performSearch);

function performSearch() {
    const searchTerm = searchInput.value.trim();
    if (searchTerm) {
        alert(`Axtarılır: ${searchTerm}`);
        // Here you would typically redirect to a search results page
        // window.location.href = `/search?q=${encodeURIComponent(searchTerm)}`;
    }
}

// Cart functionality
const cartIcon = document.querySelector('.fa-shopping-cart');
let cartCount = 0;

cartIcon.addEventListener('click', function() {
    alert('Səbət açıldı! Səbətdəki məhsullar: ' + cartCount);
    // Here you would typically open a cart modal or redirect to cart page
});

// Product card interactions
const productCards = document.querySelectorAll('.product-card');

productCards.forEach(card => {
    card.addEventListener('click', function() {
        const productName = this.querySelector('.product-name').textContent;
        const productPrice = this.querySelector('.product-price').textContent;
        
        // Add to cart animation
        this.style.transform = 'scale(0.95)';
        setTimeout(() => {
            this.style.transform = '';
        }, 200);
        
        // Simulate adding to cart
        cartCount++;
        updateCartBadge();
        
        // Show notification
        showNotification(`${productName} səbətə əlavə edildi!`);
    });
});

// Category card interactions
const categoryCards = document.querySelectorAll('.category-card');

categoryCards.forEach(card => {
    card.addEventListener('click', function() {
        const categoryName = this.querySelector('.category-name').textContent;
        alert(`${categoryName} kateqoriyasına baxılır`);
        // Here you would typically redirect to category page
        // window.location.href = `/category/${categoryName.toLowerCase()}`;
    });
});

// Newsletter subscription
const emailInput = document.getElementById('emailInput');
const subscribeBtn = document.querySelector('.btn-subscribe');

subscribeBtn.addEventListener('click', function() {
    const email = emailInput.value.trim();
    
    if (validateEmail(email)) {
        // Simulate subscription
        subscribeBtn.textContent = 'Abunə olundu!';
        subscribeBtn.style.backgroundColor = '#2ecc71';
        subscribeBtn.disabled = true;
        emailInput.value = '';
        
        showNotification('Abunə olduğunuz üçün təşəkkürlər!');
        
        setTimeout(() => {
            subscribeBtn.textContent = 'Abunə Ol';
            subscribeBtn.style.backgroundColor = '';
            subscribeBtn.disabled = false;
        }, 3000);
    } else {
        emailInput.style.border = '2px solid #e74c3c';
        emailInput.placeholder = 'Zəhmət olmasa düzgün e-poçt daxil edin';
        setTimeout(() => {
            emailInput.style.border = '';
            emailInput.placeholder = 'E-poçt ünvanınızı daxil edin';
        }, 2000);
    }
});

emailInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        subscribeBtn.click();
    }
});

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Wishlist functionality
const wishlistIcon = document.querySelector('.fa-heart');
let wishlistItems = [];

wishlistIcon.addEventListener('click', function() {
    this.classList.toggle('fas');
    this.classList.toggle('far');
    
    if (this.classList.contains('fas')) {
        this.style.color = '#e74c3c';
        showNotification('İstək siyahısına əlavə edildi!');
    } else {
        this.style.color = '';
        showNotification('İstək siyahısından silindi');
    }
});

// User profile icon
const userIcon = document.querySelector('.fa-user');

userIcon.addEventListener('click', function() {
    alert('İstifadəçi profili açıldı!');
    // Here you would typically open a login modal or redirect to profile page
});

// Notification system
function showNotification(message) {
    // Remove existing notification if any
    const existingNotification = document.querySelector('.notification');
    if (existingNotification) {
        existingNotification.remove();
    }
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background-color: #4A90E2;
        color: white;
        padding: 15px 25px;
        border-radius: 5px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        z-index: 10000;
        animation: slideIn 0.3s ease-out;
    `;
    
    document.body.appendChild(notification);
    
    // Remove notification after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 3000);
}

// Add CSS animations for notifications
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
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

// Cart badge update function
function updateCartBadge() {
    // Create or update cart badge
    let badge = document.querySelector('.cart-badge');
    if (!badge) {
        badge = document.createElement('span');
        badge.className = 'cart-badge';
        badge.style.cssText = `
            position: absolute;
            top: -8px;
            right: -8px;
            background-color: #e74c3c;
            color: white;
            border-radius: 50%;
            width: 20px;
            height: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            font-weight: bold;
        `;
        cartIcon.parentElement.style.position = 'relative';
        cartIcon.parentElement.appendChild(badge);
    }
    badge.textContent = cartCount;
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Header scroll effect
let lastScroll = 0;
const header = document.querySelector('.header');

window.addEventListener('scroll', function() {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 100) {
        header.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.15)';
    } else {
        header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    }
    
    lastScroll = currentScroll;
});

// Product card hover effects enhancement
productCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transition = 'all 0.3s ease';
    });
});

// Initialize cart badge
updateCartBadge();