// Mobile sidebar toggle functionality
document.addEventListener('DOMContentLoaded', function () {
    const mobileSidebar = document.getElementById('mobileSidebar');
    const sidebarBackdrop = document.getElementById('sidebarBackdrop');
    const closeSidebar = document.getElementById('closeSidebar');

    // Toggle sidebar when hamburger button is clicked
    document.querySelector('button.md\\:hidden').addEventListener('click', function () {
        mobileSidebar.classList.remove('hidden');
        mobileSidebar.classList.add('flex');
    });

    // Close sidebar when backdrop is clicked
    sidebarBackdrop.addEventListener('click', function () {
        mobileSidebar.classList.add('hidden');
        mobileSidebar.classList.remove('flex');
    });

    // Close sidebar when close button is clicked
    closeSidebar.addEventListener('click', function () {
        mobileSidebar.classList.add('hidden');
        mobileSidebar.classList.remove('flex');
    });

    // Add active class to sidebar items on click
    document.querySelectorAll('.sidebar-item').forEach(item => {
        item.addEventListener('click', function (e) {
            e.preventDefault();

            // Remove active class from all items
            document.querySelectorAll('.sidebar-item').forEach(el => {
                el.classList.remove('active');
            });

            // Add active class to clicked item
            this.classList.add('active');

            // If on mobile, close sidebar after selection
            if (window.innerWidth < 768) {
                mobileSidebar.classList.add('hidden');
                mobileSidebar.classList.remove('flex');
            }
        });
    });

    // Book cover hover effects
    document.querySelectorAll('.book-cover').forEach(cover => {
        cover.addEventListener('mouseenter', function () {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 10px 25px rgba(0, 0, 0, 0.2)';
        });

        cover.addEventListener('mouseleave', function () {
            this.style.transform = '';
            this.style.boxShadow = '';
        });
    });
});