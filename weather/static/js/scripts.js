document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('.weather-form');
    
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            const cityInput = form.querySelector('#city-input');
            const submitBtn = form.querySelector('#submit-btn');
            
            // Validate input
            if (!cityInput.value.trim()) {
                e.preventDefault();
                alert('Please enter a city name.');
                return;
            }

            // Show loading state
            submitBtn.disabled = true;
            submitBtn.textContent = 'Loading...';
            
            // Re-enable button after submission (handled by page reload)
            setTimeout(() => {
                submitBtn.disabled = false;
                submitBtn.textContent = 'Get Weather';
            }, 5000); // Fallback in case of network issues
        });
    });
});