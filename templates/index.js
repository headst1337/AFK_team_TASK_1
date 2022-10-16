ymaps.ready(init);

function init(){
    {% if data %}
    {% set index = data.get("index") %}
    {% if not index %}
    {% set lon = data.get("geo_coords_longitude_dd") %}
    {% set lat = data.get("geo_coords_latitude_dd") %}
    {% set range = data.get("geo_range") %}
    {% endif %}
    {% endif %}

	var myMap = new ymaps.Map("map", {
	    {% if index%}
		center: [{{data_from_server[0][3][0]}}, {{data_from_server[0][3][1]}}],
		{%else%}
		center: [parseFloat({{ lon }}), parseFloat({{ lat }})],
		{% endif %}
		zoom: 10
	}, {
		searchControlProvider: 'yandex#search'
	});


    {% for name, address, index, coords in data_from_server %}

    var Point = new ymaps.Placemark([{{ coords[0] }}, {{ coords[1] }}], {
        balloonContent: "{{address}}"
    }, {
        preset: 'islands#icon',
        iconColor: '#0095b6'
    });

    myMap.geoObjects.add(Point);
    {% endfor %}

    {% if not index %}
	// Создаем круг.
    var myCircle = new ymaps.Circle([
        // Координаты центра круга.
        [{{ lon }}, {{ lat }}],
        // Радиус круга в метрах.
        {{ range }}
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
    {% endif %}
}
