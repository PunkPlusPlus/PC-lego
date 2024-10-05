// Получаем параметры из URL
const urlParams = new URLSearchParams(window.location.search);
// Извлекаем тип ПК из URL
const pcType = urlParams.get('type');
// Поле типа в форме
const typeField = document.getElementById('id_type');
// Устанавливаем значение поля
typeField.value = pcType;


// Добавляем обработчик события на изменение выбора типа ПК
typeField.addEventListener('change', function() {
    const selectedType = this.value; // Получаем выбранный тип
    if (selectedType) {
        // Перенаправляем на URL с выбранным типом
        window.location.href = "{% url 'assembler_PC' %}?type=" + selectedType;
    }
});