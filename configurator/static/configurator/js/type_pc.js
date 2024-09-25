const urlParams = new URLSearchParams(window.location.search);
const pcType = urlParams.get('type');
const typeField = document.getElementById('id_type')
typeField.value = pcType