console.log("✅ JS завантажено");

function updateUI() {
    fetch("api/stats")
        .then((res) => res.json())
        .then((data) => {
            document.getElementById('online-count').textContent = data.online;
            document.getElementById('all-members-count').textContent = data.allmembers;
            document.getElementById('invoice-count').textContent = data.invoice;

            // оновлення часу в футері
            document.getElementById('updated-time').textContent = `Last update: ${updateFooterTime()}`;
        })
}

function loadData() {
    fetch('api/refresh_stats', { method: 'POST' })
        .then((res) => res.json())
        .then((data) => {
            if (data.status) {
                console.log("Дані оновлено...")
                updateUI();
            } else {
                console.error("Помилка оновлення статистики")
            }
        })
        .catch((err) => console.error("Помилка fetch:", err))
}

function updateFooterTime() {
    const now = new Date();
    return now.toLocaleString('en-US', {
        month: 'numeric',
        day: 'numeric',
        year: 'numeric',
        hour: 'numeric',
        minute: '2-digit',
        hour12: true
    });
}

// при завантажені сайту
document.addEventListener('DOMContentLoaded', () => {
    // оновлюємо дані
    loadData();
    // при натисканні на кнопку обновить оновлюємо дані
    document.getElementById('update-button').addEventListener('click', loadData);
});
