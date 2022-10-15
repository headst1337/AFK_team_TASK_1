ymaps.ready(init);

function init(){
	var myMap = new ymaps.Map("map", {
		center: [55.04, 82.93],
		zoom: 10
	}, {
		searchControlProvider: 'yandex#search'
	});

	// Создаем круг.
    var myCircle = new ymaps.Circle([
        // Координаты центра круга.
        [55.04, 82.93],
        // Радиус круга в метрах.
        10000
    ], {
        // Описываем свойства круга.
        // Содержимое балуна.
        balloonContent: "Радиус круга - 10 км",
    }, {
        // Задаем опции круга.
        // Цвет заливки.
        // Последний байт (77) определяет прозрачность.
        // Прозрачность заливки также можно задать используя опцию "fillOpacity".
        fillColor: "#DB709377",
        // Цвет обводки.
        strokeColor: "#990066",
        // Прозрачность обводки.
        strokeOpacity: 0.8,
        // Ширина обводки в пикселях.
        strokeWidth: 5
    });

    // Добавляем круг на карту.
    myMap.geoObjects.add(myCircle);
}

// function search() {
	
// }