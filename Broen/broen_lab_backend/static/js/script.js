// Mobile Navigation Toggle
const mobileMenu = document.getElementById('mobile-menu');
const navMenu = document.querySelector('.nav-menu');

if (mobileMenu && navMenu) {
    mobileMenu.addEventListener('click', () => {
        mobileMenu.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Close mobile menu when clicking on a link
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });
}

// Price Filter Functionality
const filterButtons = document.querySelectorAll('.filter-btn');
const priceTables = document.querySelectorAll('.price-table');

if (filterButtons.length > 0 && priceTables.length > 0) {
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            button.classList.add('active');
            
            const category = button.getAttribute('data-category');
            
            // Show/hide price tables based on category
            priceTables.forEach(table => {
                if (category === 'all') {
                    table.style.display = 'block';
                } else if (table.hasAttribute('data-category')) {
                    if (table.getAttribute('data-category') === category) {
                        table.style.display = 'block';
                    } else {
                        table.style.display = 'none';
                    }
                }
            });
        });
    });
}

// FAQ Accordion
const faqItems = document.querySelectorAll('.faq-item');

faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    if (question) {
        question.addEventListener('click', () => {
            // Close other open FAQ items
            faqItems.forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove('active');
                }
            });
            
            // Toggle current FAQ item
            item.classList.toggle('active');
        });
    }
});

// Contact Form Handler
const contactForms = document.querySelectorAll('#contact-form, #main-contact-form');

contactForms.forEach(form => {
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(form);
            const formObject = {};
            
            for (let [key, value] of formData.entries()) {
                formObject[key] = value;
            }
            
            // Simple validation
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = '#E74C3C';
                    
                    // Reset border color after 3 seconds
                    setTimeout(() => {
                        field.style.borderColor = '#E9ECEF';
                    }, 3000);
                } else {
                    field.style.borderColor = '#E9ECEF';
                }
            });
            
            // Email validation
            const emailField = form.querySelector('input[type="email"]');
            if (emailField && emailField.value) {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(emailField.value)) {
                    isValid = false;
                    emailField.style.borderColor = '#E74C3C';
                    setTimeout(() => {
                        emailField.style.borderColor = '#E9ECEF';
                    }, 3000);
                }
            }
            
            // Phone validation (basic)
            const phoneField = form.querySelector('input[type="tel"]');
            if (phoneField && phoneField.value) {
                const phoneRegex = /^[\+\d\s\-\(\)]{10,}$/;
                if (!phoneRegex.test(phoneField.value)) {
                    isValid = false;
                    phoneField.style.borderColor = '#E74C3C';
                    setTimeout(() => {
                        phoneField.style.borderColor = '#E9ECEF';
                    }, 3000);
                }
            }
            
            if (isValid) {
                // Show success message
                showNotification('Mesajınız uğurla göndərildi! Tezliklə sizinlə əlaqə saxlayacağıq.', 'success');
                
                // Reset form
                form.reset();
                
                // In a real application, you would send the data to your server
                console.log('Form data:', formObject);
            } else {
                showNotification('Xahiş olunur bütün sahələri düzgün doldurun.', 'error');
            }
        });
    }
});

// Notification System
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotification = document.querySelector('.notification');
    if (existingNotification) {
        existingNotification.remove();
    }
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <span class="notification-message">${message}</span>
            <button class="notification-close">&times;</button>
        </div>
    `;
    
    // Add styles
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        max-width: 400px;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        color: white;
        font-weight: 500;
        z-index: 10000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    `;
    
    // Set background color based on type
    switch (type) {
        case 'success':
            notification.style.background = '#4CAF50';
            break;
        case 'error':
            notification.style.background = '#E74C3C';
            break;
        default:
            notification.style.background = '#FF6B35';
    }
    
    // Add notification to body
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Close button functionality
    const closeBtn = notification.querySelector('.notification-close');
    closeBtn.style.cssText = `
        background: none;
        border: none;
        color: white;
        font-size: 1.5rem;
        cursor: pointer;
        padding: 0;
        margin-left: 1rem;
    `;
    
    closeBtn.addEventListener('click', () => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => notification.remove(), 300);
    });
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (document.body.contains(notification)) {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => notification.remove(), 300);
        }
    }, 5000);
}

// Smooth scrolling for anchor links
document.addEventListener('DOMContentLoaded', () => {
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    
    anchorLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            
            const targetId = link.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = targetElement.offsetTop - headerHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Counter Animation for Stats
function animateCounter(element, target, duration = 2000) {
    let start = 0;
    const increment = target / (duration / 16);
    
    const updateCounter = () => {
        start += increment;
        if (start < target) {
            element.textContent = Math.floor(start).toLocaleString();
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = target.toLocaleString();
        }
    };
    
    updateCounter();
}

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const element = entry.target;
            
            // Counter animation
            if (element.classList.contains('stat-number')) {
                const target = parseInt(element.textContent.replace(/[^\d]/g, ''));
                if (target && !element.classList.contains('animated')) {
                    element.classList.add('animated');
                    animateCounter(element, target);
                }
            }
            
            // Fade in animation
            if (element.classList.contains('fade-in')) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
            
            // Slide in animation
            if (element.classList.contains('slide-in')) {
                element.style.opacity = '1';
                element.style.transform = 'translateX(0)';
            }
        }
    });
}, observerOptions);

// Observe elements when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Add animation classes to elements
    const statNumbers = document.querySelectorAll('.stat-number');
    statNumbers.forEach(stat => {
        observer.observe(stat);
    });
    
    // Add fade-in class to feature cards
    const featureCards = document.querySelectorAll('.feature-card, .service-card, .team-member');
    featureCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        card.style.transitionDelay = `${index * 0.1}s`;
        card.classList.add('fade-in');
        observer.observe(card);
    });
});

// Loading Screen (optional)
window.addEventListener('load', () => {
    const loader = document.querySelector('.loader');
    if (loader) {
        loader.style.opacity = '0';
        setTimeout(() => {
            loader.style.display = 'none';
        }, 300);
    }
});

// Back to top button
const backToTopButton = document.createElement('button');
backToTopButton.innerHTML = '<i class="fas fa-arrow-up"></i>';
backToTopButton.className = 'back-to-top';
backToTopButton.style.cssText = `
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 50px;
    height: 50px;
    background: linear-gradient(45deg, #FF6B35, #FFA726);
    color: white;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    font-size: 1.2rem;
    box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3);
    transform: translateY(100px);
    transition: all 0.3s ease;
    z-index: 1000;
`;

document.body.appendChild(backToTopButton);

// Show/hide back to top button
window.addEventListener('scroll', () => {
    if (window.pageYOffset > 300) {
        backToTopButton.style.transform = 'translateY(0)';
    } else {
        backToTopButton.style.transform = 'translateY(100px)';
    }
});

// Back to top functionality
backToTopButton.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// Hover effects for buttons
backToTopButton.addEventListener('mouseenter', () => {
    backToTopButton.style.transform = 'translateY(0) scale(1.1)';
});

backToTopButton.addEventListener('mouseleave', () => {
    backToTopButton.style.transform = 'translateY(0) scale(1)';
});

// Search functionality (if search input exists)
const searchInput = document.querySelector('.search-input');
const searchResults = document.querySelector('.search-results');

if (searchInput) {
    searchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase().trim();
        
        if (searchTerm.length > 2) {
            // In a real application, you would search through your content
            // For now, we'll just show a placeholder result
            if (searchResults) {
                searchResults.innerHTML = `
                    <div class="search-item">
                        <h4>Test axtarışı: "${searchTerm}"</h4>
                        <p>Bu funksionallıq backend ilə birlikdə işləyəcək</p>
                    </div>
                `;
                searchResults.style.display = 'block';
            }
        } else {
            if (searchResults) {
                searchResults.style.display = 'none';
            }
        }
    });
    
    // Hide search results when clicking outside
    document.addEventListener('click', (e) => {
        if (!searchInput.contains(e.target) && searchResults && !searchResults.contains(e.target)) {
            searchResults.style.display = 'none';
        }
    });
}

// Print functionality for test results (future feature)
function printResults() {
    window.print();
}

// Download PDF functionality (placeholder)
function downloadPDF() {
    showNotification('PDF yükləmə funksiyası backend ilə birlikdə işləyəcək', 'info');
}

// WhatsApp contact functionality
function contactWhatsApp() {
    const phoneNumber = '+994505555555';
    const message = 'Salam, BRO-EN Laboratoriya ilə əlaqə saxlamaq istəyirəm.';
    const whatsappURL = `https://wa.me/${phoneNumber.replace(/[^\d]/g, '')}?text=${encodeURIComponent(message)}`;
    window.open(whatsappURL, '_blank');
}

// Add WhatsApp button if needed
const whatsappButtons = document.querySelectorAll('.whatsapp-contact');
whatsappButtons.forEach(button => {
    button.addEventListener('click', contactWhatsApp);
});

// Form field validation helpers
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validatePhone(phone) {
    const re = /^[\+\d\s\-\(\)]{10,}$/;
    return re.test(phone);
}

// Real-time form validation
document.addEventListener('DOMContentLoaded', () => {
    const emailInputs = document.querySelectorAll('input[type="email"]');
    const phoneInputs = document.querySelectorAll('input[type="tel"]');
    
    emailInputs.forEach(input => {
        input.addEventListener('blur', () => {
            if (input.value && !validateEmail(input.value)) {
                input.style.borderColor = '#E74C3C';
                showValidationMessage(input, 'Düzgün email adresi daxil edin');
            } else {
                input.style.borderColor = '#E9ECEF';
                hideValidationMessage(input);
            }
        });
    });
    
    phoneInputs.forEach(input => {
        input.addEventListener('blur', () => {
            if (input.value && !validatePhone(input.value)) {
                input.style.borderColor = '#E74C3C';
                showValidationMessage(input, 'Düzgün telefon nömrəsi daxil edin');
            } else {
                input.style.borderColor = '#E9ECEF';
                hideValidationMessage(input);
            }
        });
    });
});

function showValidationMessage(input, message) {
    hideValidationMessage(input);
    
    const validationMessage = document.createElement('div');
    validationMessage.className = 'validation-message';
    validationMessage.textContent = message;
    validationMessage.style.cssText = `
        color: #E74C3C;
        font-size: 0.8rem;
        margin-top: 0.3rem;
        display: block;
    `;
    
    input.parentNode.insertBefore(validationMessage, input.nextSibling);
}

function hideValidationMessage(input) {
    const existingMessage = input.parentNode.querySelector('.validation-message');
    if (existingMessage) {
        existingMessage.remove();
    }
}

// Console log for debugging (remove in production)
console.log('BRO-EN Laboratoriya - JavaScript yükləndi');
console.log('Veb sayt hazırdır və işləyir!');