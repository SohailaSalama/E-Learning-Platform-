document.addEventListener('DOMContentLoaded', function () {
    // Set User Name Dynamically
    const userName = 'Sohaila'; // Replace with a dynamic name if needed
    document.getElementById('user-name').textContent = userName;

    // Dropdown Interaction
    const userMenu = document.querySelector('.user-account');
    const dropdown = document.querySelector('.dropdown-content');

    userMenu.addEventListener('mouseenter', () => {
        dropdown.style.display = 'block';
    });

    userMenu.addEventListener('mouseleave', () => {
        dropdown.style.display = 'none';
    });
});

