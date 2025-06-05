/**
 * Main JavaScript file for Elon Musk profile website
 */

(function() {
    'use strict';

    // Enable smooth scrolling for all hash links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            if (this.getAttribute('href') !== '#') {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    window.scrollTo({
                        top: target.offsetTop - 70,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // Counter animation for stats
    function initCounters() {
        const counters = document.querySelectorAll('.counter');
        const speed = 200;
        
        counters.forEach(counter => {
            const animate = () => {
                const value = +counter.getAttribute('data-count');
                const data = +counter.innerText;
                const time = value / speed;
                
                if (data < value) {
                    counter.innerText = Math.ceil(data + time);
                    setTimeout(animate, 1);
                } else {
                    counter.innerText = formatNumber(value);
                }
            };
            
            animate();
        });
    }

    // Format large numbers with commas
    function formatNumber(num) {
        return num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,');
    }

    // Activate counter when element is in viewport
    function handleScrollAnimations() {
        const statsSection = document.querySelector('.counter');
        if (statsSection && isElementInViewport(statsSection) && !statsSection.classList.contains('counted')) {
            statsSection.classList.add('counted');
            initCounters();
        }
    }

    // Check if element is in viewport
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    // Initialize lightbox/gallery for project images
    function initializeLightbox() {
        const galleryItems = document.querySelectorAll('.gallery-item');
        if (galleryItems.length > 0) {
            galleryItems.forEach(item => {
                item.addEventListener('click', (e) => {
                    e.preventDefault();
                    const imgSrc = item.getAttribute('href');
                    const lightbox = document.createElement('div');
                    lightbox.id = 'lightbox';
                    lightbox.innerHTML = `
                        <div class="lightbox-container">
                            <img src="${imgSrc}" alt="Gallery Image">
                            <span class="lightbox-close">&times;</span>
                        </div>
                    `;
                    document.body.appendChild(lightbox);
                    
                    // Add close functionality
                    lightbox.querySelector('.lightbox-close').addEventListener('click', () => {
                        document.body.removeChild(lightbox);
                    });
                    
                    lightbox.addEventListener('click', (e) => {
                        if (e.target === lightbox) {
                            document.body.removeChild(lightbox);
                        }
                    });
                });
            });
        }
    }

    // Initialize portfolio filters
    function initializePortfolioFilters() {
        const filterButtons = document.querySelectorAll('.portfolio-filter button');
        const portfolioItems = document.querySelectorAll('.portfolio-item');
        
        if (filterButtons.length > 0) {
            filterButtons.forEach(button => {
                button.addEventListener('click', () => {
                    // Remove active class from all buttons
                    filterButtons.forEach(btn => {
                        btn.classList.remove('active');
                    });
                    
                    // Add active class to clicked button
                    button.classList.add('active');
                    
                    const filterValue = button.getAttribute('data-filter');
                    
                    // Filter portfolio items
                    portfolioItems.forEach(item => {
                        if (filterValue === 'all') {
                            item.style.display = 'block';
                        } else if (item.classList.contains(filterValue)) {
                            item.style.display = 'block';
                        } else {
                            item.style.display = 'none';
                        }
                    });
                });
            });
        }
    }

    // Show/hide mobile menu
    function setupMobileMenu() {
        const navbarToggler = document.querySelector('.navbar-toggler');
        const navbarCollapse = document.querySelector('.navbar-collapse');
        
        if (navbarToggler) {
            // Close mobile menu when clicking on a link
            document.querySelectorAll('.navbar-nav .nav-link').forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth < 992) {
                        navbarCollapse.classList.remove('show');
                    }
                });
            });
            
            // Close mobile menu when clicking outside
            document.addEventListener('click', (e) => {
                if (navbarCollapse.classList.contains('show') && 
                    !navbarCollapse.contains(e.target) && 
                    e.target !== navbarToggler) {
                    navbarCollapse.classList.remove('show');
                }
            });
        }
    }

    // Lazy load images
    function lazyLoadImages() {
        const lazyImages = document.querySelectorAll('img[data-src]');
        
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src;
                        img.classList.add('loaded');
                        imageObserver.unobserve(img);
                    }
                });
            });
            
            lazyImages.forEach(img => {
                imageObserver.observe(img);
            });
        } else {
            // Fallback for browsers that don't support IntersectionObserver
            lazyImages.forEach(img => {
                img.src = img.dataset.src;
            });
        }
    }

    // Form validation
    function setupFormValidation() {
        const contactForm = document.querySelector('#contactForm');
        
        if (contactForm) {
            contactForm.addEventListener('submit', function(e) {
                let isValid = true;
                const requiredFields = contactForm.querySelectorAll('[required]');
                
                requiredFields.forEach(field => {
                    if (!field.value.trim()) {
                        isValid = false;
                        field.classList.add('is-invalid');
                    } else {
                        field.classList.remove('is-invalid');
                    }
                });
                
                const emailField = contactForm.querySelector('input[type="email"]');
                if (emailField && emailField.value.trim()) {
                    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                    if (!emailPattern.test(emailField.value)) {
                        isValid = false;
                        emailField.classList.add('is-invalid');
                    }
                }
                
                if (!isValid) {
                    e.preventDefault();
                }
            });
            
            // Remove invalid class on input
            contactForm.querySelectorAll('.form-control').forEach(input => {
                input.addEventListener('input', function() {
                    this.classList.remove('is-invalid');
                });
            });
        }
    }

    // Initialize on document load
    document.addEventListener('DOMContentLoaded', function() {
        // Initialize all functions
        handleScrollAnimations();
        initializeLightbox();
        initializePortfolioFilters();
        setupMobileMenu();
        lazyLoadImages();
        setupFormValidation();
        
        // Add scroll event listeners
        window.addEventListener('scroll', handleScrollAnimations);
    });
})(); 