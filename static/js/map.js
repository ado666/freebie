window.gmap	= {
	seq: 0,
	markers: {}
};

gmap.initAll = function(){
	gmap.init('main');
//	gmap.init('offer');
}

gmap.init	=  function (map) {
	var mapCanvas = document.getElementById('map-canvas-'+map);
	var mapOptions = {
		center: new google.maps.LatLng(55.7503, 37.6263),
		zoom: 12
	}
	gmap['map-'+map] = new google.maps.Map(mapCanvas, mapOptions);
	if (map == 'offer'){
		map = gmap['map-offer'];
		infowindow = new google.maps.InfoWindow();

		var input = (document.getElementById('pac-input'));

		map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
		var autocomplete = new google.maps.places.Autocomplete(input);
		autocomplete.bindTo('bounds', gmap['map-offer']);

		google.maps.event.addListener(autocomplete, 'place_changed', function() {
			infowindow.close();
			var place = autocomplete.getPlace();
			if (!place.geometry) {
				window.alert("Autocomplete's returned place contains no geometry");
				return;
			}

			// If the place has a geometry, then present it on a map.
			if (place.geometry.viewport) {
				map.fitBounds(place.geometry.viewport);
			} else {
				map.setCenter(place.geometry.location);
				map.setZoom(17);  // Why 17? Because it looks good.
			}

//			var marker = new google.maps.Marker({
//				map: gmap['map-offer'],
//				icon: gmap.getIcon(),
//				anchorPoint: new google.maps.Point(0, -29)
//			});м
			var x = place.geometry.location.A;
			var y = place.geometry.location.F;

			if (gmap.offerPin)	gmap.removePin('offer', gmap.offerPin)
			gmap.offerPin	= gmap.addPin('offer', [x,y])

			$('#offer_lat').text(x);
			$('#offer_lng').text(y);

			gmap.offerPin.setPosition(place.geometry.location);
			gmap.offerPin.setVisible(true);

			var address = '';
			if (place.address_components) {
				address = [
					(place.address_components[0] && place.address_components[0].short_name || ''),
					(place.address_components[1] && place.address_components[1].short_name || ''),
					(place.address_components[2] && place.address_components[2].short_name || '')
				].join(' ');
			}
			infowindow.setContent('<div><strong>' + place.name + '</strong><br>' + address);
			infowindow.open(map, gmap.offerPin);
		});
	}
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

gmap.addPin = function(map, cords, title, icon){
	var icon	= gmap.getIcon(icon);
	var point	= new google.maps.LatLng(cords[0], cords[1]);

	var marker = new google.maps.Marker({
		position: point,
		icon: icon,
		map: gmap['map-'+map],
		title: title
	});

	var id	= ++gmap.seq;
	gmap.markers[map+'-'+id]	= marker;

	return id;
};
gmap.removePin = function(map, id){
	gmap.markers[map+'-'+id].setMap(null);
}


google.maps.event.addDomListener(window, 'load', gmap.initAll);