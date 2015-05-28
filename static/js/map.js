window.gmap	= {
	seq: 0,
	markers: {}
};


gmap.init	=  function () {
	var mapCanvas = document.getElementById('map-canvas');
	var mapOptions = {
		center: new google.maps.LatLng(55.7503, 37.6263),
		zoom: 12,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	}
	gmap.map = new google.maps.Map(mapCanvas, mapOptions)
}

gmap.iconbase	= 'https://maps.google.com/mapfiles/kml/shapes/';

gmap.getIcon	= function(type){
	var icon	= gmap.iconbase;

	switch (type) {
		case 'food':
			icon += 'info-i_maps.png';
			break;
		default:
			icon = null;
			break;
	}

	return icon;
}

gmap.addPin = function(cords, title, icon){
	var icon	= gmap.getIcon(icon);
	var point	= new google.maps.LatLng(cords[0], cords[1]);

	var marker = new google.maps.Marker({
		position: point,
		icon: icon,
		map: gmap.map,
		title: title
	});

	var id	= ++gmap.seq;
	gmap.markers[id]	= marker;

	return id;
};
gmap.removePin = function(id){
	gmap.markers[id].setMap(null);
}


google.maps.event.addDomListener(window, 'load', gmap.init);