// Mobile menu toggle
const mobileMenuButton = document.getElementById('mobile-menu-button');
const mobileMenu = document.getElementById('mobile-menu');

if (mobileMenuButton && mobileMenu) {
    mobileMenuButton.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });
}

// Sticky header effect on scroll
const header = document.querySelector('.sticky-header');

if (header) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('header-scrolled');
        } else {
            header.classList.remove('header-scrolled');
        }
    });

    // Initialize with header state
    if (window.scrollY > 50) {
        header.classList.add('header-scrolled');
    }
}

// Featured slider functionality
const slider = document.getElementById('featured-slider');
const prevButton = document.querySelector('.slider-prev');
const nextButton = document.querySelector('.slider-next');

if (slider && prevButton && nextButton) {
    prevButton.addEventListener('click', () => {
        slider.scrollBy({ left: -slider.offsetWidth * 0.8, behavior: 'smooth' });
    });
    
    nextButton.addEventListener('click', () => {
        slider.scrollBy({ left: slider.offsetWidth * 0.8, behavior: 'smooth' });
    });
}

// Load more button functionality
const loadMoreButton = document.getElementById('load-more');

if (loadMoreButton) {
    loadMoreButton.addEventListener('click', () => {
        loadMoreButton.textContent = 'Loading...';
        loadMoreButton.disabled = true;
        
        // Simulate loading delay
        setTimeout(() => {
            // In a real implementation, this would fetch more posts from an API
            alert('In a real implementation, this would load more blog posts from the server.');
            loadMoreButton.textContent = 'Load More Articles';
            loadMoreButton.disabled = false;
        }, 1000);
    });
}

// Newsletter form submission
const newsletterForm = document.getElementById('newsletter-form');

if (newsletterForm) {
    newsletterForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const emailInput = newsletterForm.querySelector('input[type="email"]');
        
        if (emailInput && emailInput.value && emailInput.value.includes('@')) {
            alert('Thank you for subscribing to our newsletter!');
            emailInput.value = '';
        } else {
            alert('Please enter a valid email address.');
        }
    });
}

// Contact form submission
const contactForm = document.getElementById('contact-form');

if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // Get form values
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const subject = document.getElementById('subject').value;
        const message = document.getElementById('message').value;
        
        // Basic validation
        if (name && email && subject && message) {
            // In a real implementation, this would send data to a server
            alert(`Thank you, ${name}! Your message has been sent. We'll get back to you at ${email} within 1-2 business days.`);
            contactForm.reset();
        } else {
            alert('Please fill in all required fields.');
        }
    });
}

// FAQ accordion functionality
const faqToggles = document.querySelectorAll('.faq-toggle');

faqToggles.forEach(toggle => {
    toggle.addEventListener('click', () => {
        const content = toggle.nextElementSibling;
        const icon = toggle.querySelector('i');
        
        // Toggle current FAQ
        content.classList.toggle('hidden');
        
        // Rotate icon
        if (content.classList.contains('hidden')) {
            icon.classList.remove('fa-chevron-up');
            icon.classList.add('fa-chevron-down');
        } else {
            icon.classList.remove('fa-chevron-down');
            icon.classList.add('fa-chevron-up');
        }
        
        // Close other FAQs (optional - remove if you want multiple open)
        faqToggles.forEach(otherToggle => {
            if (otherToggle !== toggle) {
                const otherContent = otherToggle.nextElementSibling;
                const otherIcon = otherToggle.querySelector('i');
                
                if (otherContent && otherContent.classList) {
                    otherContent.classList.add('hidden');
                }
                if (otherIcon) {
                    otherIcon.classList.remove('fa-chevron-up');
                    otherIcon.classList.add('fa-chevron-down');
                }
            }
        });
    });
});


// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const targetId = this.getAttribute('href');
        
        // Handle links that might be just "#"
        if (targetId === '#' || !targetId) return;

        // Make sure it's a valid ID selector
        if (!targetId.startsWith('#')) return;
        
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            e.preventDefault();
            window.scrollTo({
                top: targetElement.offsetTop - 100,
                behavior: 'smooth'
            });
            
            // Close mobile menu if open
            if (mobileMenu) {
                mobileMenu.classList.add('hidden');
            }
        }
    });
});
