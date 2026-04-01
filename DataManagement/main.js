// ========================================
// HƏFTƏ 1-8: HTML, CSS, JavaScript Layihəsi
// 8 həftəlik öyrənmə planına uyğun kod
// ========================================

// Global dəyişənlər
let counter = 0;
let todos = JSON.parse(localStorage.getItem('todos')) || [];
let isDarkMode = localStorage.getItem('darkMode') === 'true';

// ========================================
// DOM Elementləri
// ========================================
const elements = {
    // Navigation elements
    navToggle: document.getElementById('navToggle'),
    navMenu: document.getElementById('navMenu'),
    darkModeToggle: document.getElementById('darkModeToggle'),
    
    // Counter elements
    counterValue: document.getElementById('counterValue'),
    increaseBtn: document.getElementById('increaseBtn'),
    decreaseBtn: document.getElementById('decreaseBtn'),
    resetBtn: document.getElementById('resetBtn'),
    
    // Todo elements
    todoInput: document.getElementById('todoInput'),
    addTodoBtn: document.getElementById('addTodoBtn'),
    todoList: document.getElementById('todoList'),
    
    // Contact form
    contactForm: document.getElementById('contactForm'),
    
    // Scroll to top button
    scrollToTop: document.getElementById('scrollToTop'),
    
    // Loading screen
    loadingScreen: document.getElementById('loadingScreen'),
    
    // Statistics
    statNumbers: document.querySelectorAll('.stat-number')
};

// ========================================
// HƏFTƏ 4: JavaScript əsasları və DOM
// ========================================

// Dark Mode funksionallığı
function toggleDarkMode() {
    isDarkMode = !isDarkMode;
    document.body.classList.toggle('dark', isDarkMode);
    localStorage.setItem('darkMode', isDarkMode);
    
    // Dark mode icon dəyişdirməsi
    elements.darkModeToggle.textContent = isDarkMode ? '☀️' : '🌙';
    
    // Smooth transition effekti
    document.body.style.transition = 'background-color 0.3s ease, color 0.3s ease';
}

// Sayğac funksionallığı
function updateCounter(operation) {
    switch(operation) {
        case 'increase':
            counter++;
            break;
        case 'decrease':
            counter--;
            break;
        case 'reset':
            counter = 0;
            break;
        default:
            console.warn('Bilinməyən əməliyyat:', operation);
    }
    
    // Counter dəyərini yeniləmək
    if (elements.counterValue) {
        elements.counterValue.textContent = counter;
        
        // Animasiya effekti
        elements.counterValue.style.transform = 'scale(1.2)';
        setTimeout(() => {
            elements.counterValue.style.transform = 'scale(1)';
        }, 200);
    }
}

// Navigation menu toggle (mobil üçün)
function toggleNavMenu() {
    const isActive = elements.navMenu.classList.contains('active');
    elements.navMenu.classList.toggle('active', !isActive);
    
    // Hamburger menu animasiyası
    const spans = elements.navToggle.querySelectorAll('span');
    spans.forEach((span, index) => {
        if (!isActive) {
            if (index === 0) span.style.transform = 'rotate(-45deg) translate(-5px, 6px)';
            if (index === 1) span.style.opacity = '0';
            if (index === 2) span.style.transform = 'rotate(45deg) translate(-5px, -6px)';
        } else {
            span.style.transform = 'none';
            span.style.opacity = '1';
        }
    });
}

// ========================================
// HƏFTƏ 5: Massivlər, obyektlər, localStorage
// ========================================

// Todo obyekt strukturu
class TodoItem {
    constructor(text, id = Date.now()) {
        this.id = id;
        this.text = text;
        this.completed = false;
        this.createdAt = new Date().toISOString();
    }
    
    toggle() {
        this.completed = !this.completed;
    }
}

// Todo əlavə etmək
function addTodo() {
    const todoText = elements.todoInput.value.trim();
    
    if (todoText === '') {
        showNotification('Boş tapşırıq əlavə edilə bilməz!', 'error');
        return;
    }
    
    const newTodo = new TodoItem(todoText);
    todos.push(newTodo);
    
    // LocalStorage-ə saxlamaq
    saveTodosToStorage();
    
    // Input-u təmizləmək
    elements.todoInput.value = '';
    
    // Siyahını yeniləmək
    renderTodos();
    
    showNotification('Tapşırıq əlavə edildi!', 'success');
}

// Todo-ları render etmək
function renderTodos() {
    if (!elements.todoList) return;
    
    elements.todoList.innerHTML = '';
    
    // Todo-ları tarixi ilə çeşidləmək
    const sortedTodos = todos.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));
    
    sortedTodos.forEach(todo => {
        const listItem = createTodoElement(todo);
        elements.todoList.appendChild(listItem);
    });
    
    // Əgər todo yoxdursa, məlumat mesajı göstərmək
    if (todos.length === 0) {
        elements.todoList.innerHTML = '<li style="text-align: center; color: var(--text-secondary); padding: 1rem;">Hələ tapşırıq yoxdur. Yeni tapşırıq əlavə edin!</li>';
    }
}

// Todo element yaratmaq
function createTodoElement(todo) {
    const listItem = document.createElement('li');
    listItem.className = `todo-item ${todo.completed ? 'completed' : ''}`;
    listItem.dataset.todoId = todo.id;
    
    listItem.innerHTML = `
        <span class="todo-text">${escapeHtml(todo.text)}</span>
        <div class="todo-actions">
            <button class="complete-btn" onclick="toggleTodo(${todo.id})" title="${todo.completed ? 'Tamamlanmamış' : 'Tamamlanmış'} işarələ">
                ${todo.completed ? '↶' : '✓'}
            </button>
            <button class="delete-btn" onclick="deleteTodo(${todo.id})" title="Sil">
                🗑️
            </button>
        </div>
    `;
    
    return listItem;
}

// Todo vəziyyətini dəyişdirmək
function toggleTodo(id) {
    const todoIndex = todos.findIndex(todo => todo.id === id);
    if (todoIndex !== -1) {
        todos[todoIndex].toggle();
        saveTodosToStorage();
        renderTodos();
        
        const status = todos[todoIndex].completed ? 'tamamlandı' : 'tamamlanmadı';
        showNotification(`Tapşırıq ${status}!`, 'info');
    }
}

// Todo silmək
function deleteTodo(id) {
    const todoIndex = todos.findIndex(todo => todo.id === id);
    if (todoIndex !== -1) {
        // Silmə təsdiq dialoquu
        if (confirm('Bu tapşırığı silmək istədiyinizə əminsiniz?')) {
            todos.splice(todoIndex, 1);
            saveTodosToStorage();
            renderTodos();
            showNotification('Tapşırıq silindi!', 'warning');
        }
    }
}

// Todo-ları localStorage-ə saxlamaq
function saveTodosToStorage() {
    try {
        localStorage.setItem('todos', JSON.stringify(todos));
    } catch (error) {
        console.error('Todo-lar saxlanılarkən xəta:', error);
        showNotification('Məlumatlar saxlanılarkən xəta baş verdi!', 'error');
    }
}

// ========================================
// HƏFTƏ 6: Asinxron JS və Fetch API
// ========================================

// API-dən fake məlumatlar çəkmək
async function fetchPlaceholderData() {
    try {
        showNotification('Məlumatlar yüklənir...', 'info');
        
        const response = await fetch('https://jsonplaceholder.typicode.com/posts?_limit=3');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const posts = await response.json();
        displayApiData(posts);
        showNotification('Məlumatlar uğurla yükləndi!', 'success');
        
    } catch (error) {
        console.error('API xətası:', error);
        showNotification('Məlumatlar yüklənərkən xəta baş verdi!', 'error');
        
        // Fallback məlumatları göstərmək
        displayFallbackData();
    }
}

// API məlumatlarını göstərmək
function displayApiData(posts) {
    const apiSection = document.querySelector('.api-data-section');
    if (!apiSection) return;
    
    const postsContainer = apiSection.querySelector('.posts-container');
    postsContainer.innerHTML = '';
    
    posts.forEach(post => {
        const postElement = document.createElement('div');
        postElement.className = 'api-post-card';
        postElement.innerHTML = `
            <h4>${escapeHtml(post.title)}</h4>
            <p>${escapeHtml(post.body.substring(0, 100))}...</p>
            <span class="post-id">ID: ${post.id}</span>
        `;
        postsContainer.appendChild(postElement);
    });
}

// Fallback məlumatları
function displayFallbackData() {
    const fallbackPosts = [
        { id: 1, title: 'Veb developmentin əsasları', body: 'HTML, CSS və JavaScript öyrənmək üçün addım-addım plan...' },
        { id: 2, title: 'Responsiv dizaynın vacibliyi', body: 'Müxtəlif cihazlar üçün uyğunlaşan veb saytlar yaratmaq...' },
        { id: 3, title: 'JavaScript ES6+ xüsusiyyətləri', body: 'Müasir JavaScript-in güclü imkanları və istifadə sahələri...' }
    ];
    
    displayApiData(fallbackPosts);
}

// ========================================
// Utility funksiyalar
// ========================================

// HTML-in təhlükəsiz göstərilməsi (XSS protection)
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}

// Bildiriş sistemi
function showNotification(message, type = 'info') {
    // Mövcud bildirişləri silmək
    const existingNotifications = document.querySelectorAll('.notification');
    existingNotifications.forEach(notification => notification.remove());
    
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Stil əlavə etmək
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        padding: 1rem 1.5rem;
        border-radius: 5px;
        color: white;
        font-weight: 600;
        z-index: 10000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
        max-width: 300px;
        word-wrap: break-word;
    `;
    
    // Rəng sxemi
    const colors = {
        success: '#10b981',
        error: '#ef4444',
        warning: '#f59e0b',
        info: '#3b82f6'
    };
    
    notification.style.backgroundColor = colors[type] || colors.info;
    
    document.body.appendChild(notification);
    
    // Animasiya
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Avtomatik silmək
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Smooth scroll funksiyası
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ 
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Scroll to top funksiyası
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// ========================================
// Statistika animasiyası
// ========================================
function animateStatNumbers() {
    elements.statNumbers.forEach(element => {
        const target = parseInt(element.dataset.target);
        const duration = 2000; // 2 saniyə
        const increment = target / (duration / 16); // 60fps
        let current = 0;
        
        const timer = setInterval(() => {
            current += increment;
            element.textContent = Math.floor(current);
            
            if (current >= target) {
                element.textContent = target;
                clearInterval(timer);
            }
        }, 16);
    });
}

// Intersection Observer ilə animasiya başlatmaq
function setupScrollAnimations() {
    const observerOptions = {
        threshold: 0.3,
        rootMargin: '-50px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                if (entry.target.classList.contains('about-section')) {
                    animateStatNumbers();
                }
            }
        });
    }, observerOptions);
    
    // Müşahidə ediləcək elementlər
    const aboutSection = document.querySelector('.about-section');
    if (aboutSection) {
        observer.observe(aboutSection);
    }
}

// ========================================
// Form validation və submit
// ========================================
function handleContactForm(event) {
    event.preventDefault();
    
    const formData = new FormData(event.target);
    const data = {
        name: formData.get('name'),
        email: formData.get('email'),
        message: formData.get('message')
    };
    
    // Sadə validation
    if (!data.name || !data.email || !data.message) {
        showNotification('Bütün sahələri doldurun!', 'error');
        return;
    }
    
    // Email formatını yoxlamaq
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(data.email)) {
        showNotification('Düzgün email ünvanı daxil edin!', 'error');
        return;
    }
    
    // Simulasiya: form göndərmək
    showNotification('Mesajınız göndərilir...', 'info');
    
    setTimeout(() => {
        showNotification('Mesajınız uğurla göndərildi!', 'success');
        event.target.reset();
    }, 1500);
}

// ========================================
// Scroll event handlers
// ========================================
function handleScroll() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    // Scroll to top düyməsini göstər/gizlət
    if (elements.scrollToTop) {
        elements.scrollToTop.classList.toggle('visible', scrollTop > 300);
    }
    
    // Navigation-a paralax effekti
    const header = document.querySelector('.main-header');
    if (header && scrollTop > 100) {
        header.style.backgroundColor = isDarkMode ? 'rgba(17, 24, 39, 0.95)' : 'rgba(255, 255, 255, 0.95)';
        header.style.backdropFilter = 'blur(10px)';
    } else if (header) {
        header.style.backgroundColor = '';
        header.style.backdropFilter = '';
    }
}

// ========================================
// Layihə modal funksiyaları
// ========================================
function openProject(projectType) {
    const projectDetails = {
        todo: {
            title: 'Todo Tətbiqi',
            description: 'LocalStorage ilə məlumatları saxlayan tam funksional todo tətbiqi. Tapşırıq əlavə etmək, silmək və tamamlandı işarələmək imkanları.',
            technologies: ['JavaScript ES6+', 'LocalStorage API', 'CSS Grid', 'DOM Manipulation'],
            features: ['Məlumat saxlama', 'Real-time yenilənmə', 'Responsiv dizayn', 'Form validation']
        },
        weather: {
            title: 'Hava Proqnozu Tətbiqi',
            description: 'Async/await və Fetch API istifadə edərək real hava məlumatları alan tətbiq.',
            technologies: ['Fetch API', 'Async/Await', 'JSON', 'Error Handling'],
            features: ['API inteqrasiyası', 'Şəhər axtarışı', 'Hava ikonları', 'Yüklənmə animasiyası']
        },
        counter: {
            title: 'İnteraktiv Sayğac',
            description: 'Dark mode dəstəyi olan, animasiyalı sayğac tətbiqi.',
            technologies: ['Event Listeners', 'CSS Transitions', 'LocalStorage', 'Theme Toggle'],
            features: ['Dark/Light tema', 'Smooth animasiyalar', 'Keyboard dəstəyi', 'Vəziyyət saxlama']
        }
    };
    
    const project = projectDetails[projectType];
    if (!project) return;
    
    showNotification(`${project.title} layihəsi açılır...`, 'info');
    
    // Modal yaratmaq və göstərmək
    createProjectModal(project);
}

function createProjectModal(project) {
    // Mövcud modalı silmək
    const existingModal = document.querySelector('.project-modal');
    if (existingModal) {
        existingModal.remove();
    }
    
    const modal = document.createElement('div');
    modal.className = 'project-modal';
    modal.innerHTML = `
        <div class="modal-overlay" onclick="closeProjectModal()"></div>
        <div class="modal-content">
            <button class="modal-close" onclick="closeProjectModal()">×</button>
            <h2>${project.title}</h2>
            <p>${project.description}</p>
            
            <h3>İstifadə edilən texnologiyalar:</h3>
            <div class="tech-tags">
                ${project.technologies.map(tech => `<span class="tech-tag">${tech}</span>`).join('')}
            </div>
            
            <h3>Xüsusiyyətlər:</h3>
            <ul class="feature-list">
                ${project.features.map(feature => `<li>${feature}</li>`).join('')}
            </ul>
            
            <div class="modal-actions">
                <button onclick="showDemo('${project.title}')" class="demo-btn">Demo göstər</button>
                <button onclick="closeProjectModal()" class="close-btn">Bağla</button>
            </div>
        </div>
    `;
    
    // Modal stillərini əlavə etmək
    modal.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 10000;
        display: flex;
        justify-content: center;
        align-items: center;
        opacity: 0;
        transition: opacity 0.3s ease;
    `;
    
    document.body.appendChild(modal);
    
    // Animasiya
    setTimeout(() => {
        modal.style.opacity = '1';
    }, 10);
    
    // ESC düyməsi ilə bağlamaq
    const handleEscape = (e) => {
        if (e.key === 'Escape') {
            closeProjectModal();
            document.removeEventListener('keydown', handleEscape);
        }
    };
    document.addEventListener('keydown', handleEscape);
}

function closeProjectModal() {
    const modal = document.querySelector('.project-modal');
    if (modal) {
        modal.style.opacity = '0';
        setTimeout(() => modal.remove(), 300);
    }
}

function showDemo(projectTitle) {
    showNotification(`${projectTitle} - Demo funksiyası aktiv!`, 'success');
    closeProjectModal();
}

// ========================================
// Event Listeners və inicializasiya
// ========================================
function initializeEventListeners() {
    // Dark mode toggle
    if (elements.darkModeToggle) {
        elements.darkModeToggle.addEventListener('click', toggleDarkMode);
    }
    
    // Navigation toggle
    if (elements.navToggle) {
        elements.navToggle.addEventListener('click', toggleNavMenu);
    }
    
    // Counter düymələri
    if (elements.increaseBtn) elements.increaseBtn.addEventListener('click', () => updateCounter('increase'));
    if (elements.decreaseBtn) elements.decreaseBtn.addEventListener('click', () => updateCounter('decrease'));
    if (elements.resetBtn) elements.resetBtn.addEventListener('click', () => updateCounter('reset'));
    
    // Todo functionality
    if (elements.addTodoBtn) elements.addTodoBtn.addEventListener('click', addTodo);
    if (elements.todoInput) {
        elements.todoInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') addTodo();
        });
    }
    
    // Contact form
    if (elements.contactForm) {
        elements.contactForm.addEventListener('submit', handleContactForm);
    }
    
    // Scroll to top
    if (elements.scrollToTop) {
        elements.scrollToTop.addEventListener('click', scrollToTop);
    }
    
    // Scroll event
    window.addEventListener('scroll', handleScroll);
    
    // Navigation linklər
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            scrollToSection(targetId);
            
            // Mobil menunu bağlamaq
            if (elements.navMenu.classList.contains('active')) {
                toggleNavMenu();
            }
        });
    });
}

// ========================================
// Başlanğıc inicializasiya
// ========================================
function initializeApp() {
    // Loading screen-i gizlətmək
    setTimeout(() => {
        if (elements.loadingScreen) {
            elements.loadingScreen.classList.add('hidden');
        }
    }, 1000);
    
    // Dark mode-u tənzimləmək
    if (isDarkMode) {
        document.body.classList.add('dark');
        elements.darkModeToggle.textContent = '☀️';
    }
    
    // Todo-ları render etmək
    renderTodos();
    
    // Event listener-ləri quraşdırmaq
    initializeEventListeners();
    
    // Scroll animasiyalarını quraşdırmaq
    setupScrollAnimations();
    
    // API məlumatlarını çəkmək (optional)
    // fetchPlaceholderData();
    
    // Başlanğıc mesajı
    setTimeout(() => {
        showNotification('8 həftəlik layihəyə xoş gəlmisiniz! 🎉', 'success');
    }, 1500);
}

// ========================================
// DOM yüklənəndə başlatmaq
// ========================================
document.addEventListener('DOMContentLoaded', initializeApp);

// ========================================
// Global funksiyalar (HTML-dən çağırılması üçün)
// ========================================
window.scrollToSection = scrollToSection;
window.openProject = openProject;
window.closeProjectModal = closeProjectModal;
window.toggleTodo = toggleTodo;
window.deleteTodo = deleteTodo;
window.showDemo = showDemo;
