ymaps.ready(init);

function init(){
	var myMap = new ymaps.Map("map", {
		center: [55.04, 82.93],
		zoom: 10
	}, {
		searchControlProvider: 'yandex#search'
	});


    {% for name, address, index, coords in data_from_server %}

    var Point = new ymaps.Placemark([{{ coords[0] }}, {{ coords[1] }}], {
        balloonContent: 'почтовое отделение'
    }, {
        preset: 'islands#icon',
        iconColor: '#0095b6'
    });

    myMap.geoObjects.add(Point);
    {% endfor %}

    
    
	// Создаем круг.
    var myCircle = new ymaps.Circle([
        // Координаты центра круга.
        [55.041389, 82.934444],
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