const fields = {
    cpu: document.getElementById('id_cpu'),
    gpu: document.getElementById('id_gpu'),
    motherboard: document.getElementById('id_motherboard'),
    ram: document.getElementById('id_ram'),
    storage_drive: document.getElementById('id_storage_drive'),
    power_supply: document.getElementById('id_power_supply'),
    cooling_system: document.getElementById('id_cooling_system'),
    case: document.getElementById('id_case'),
};
const priceField = document.getElementById('id_price_all');
let totalPrice = 0;
const oldPrices = {};

// Функция для обновления поля цены
const updateTotalPrice = () => {
    priceField.value = totalPrice.toFixed(2);
};

// Логика получения цены
const fetchPrice = async (id, model) => {
    const response = await fetch('/api/price?' + new URLSearchParams({ id, model }));
    return parseFloat(await response.text()) || 0;
};

// Универсальный обработчик изменений, к общей цене прибавляем/вычитаем стоимость компонента
const handleChange = async (event, model) => {
    const newId = event.target.value;
    const newPrice = await fetchPrice(newId, model);

    totalPrice = totalPrice - (oldPrices[model] || 0) + newPrice;
    oldPrices[model] = newPrice;

    updateTotalPrice();
};

// Добавляем обработчики событий для каждого поля
Object.keys(fields).forEach(model => {
    fields[model].addEventListener('change', event => handleChange(event, model));
});