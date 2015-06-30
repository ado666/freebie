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
	if (map == 'main'){
			$.ajax({
		url: "/offer/all",
		method: "GET",
		success: function(data){
			for (var i = 0, l = data.length; i < l; i++){
				var offer	= data[i];
				gmap.addPin('main', [offer.lat, offer.lng], offer.name, offer.icon, offer.id)
			}
		}
	});
	}
	if (map == 'offer'){
		map = gmap['map-offer'];
		infowindow = new google.maps.InfoWindow();

		var input = (document.getElementById('pac-input'));

//		map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
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
			gmap.offerPin	= gmap.addPin('offer', [x,y])[0]
			var marker	= gmap.addPin('offer', [x,y])[1]

			$('#offer_lat').text(x);
			$('#offer_lng').text(y);

			marker.setPosition(place.geometry.location);
			marker.offerPin.setVisible(true);

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
	if (type)	return 'img/pins/'+type+'.png';
	return;
	var icon	= gmap.iconbase;
	icon		= '/img/offers/';

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

gmap.addPin = function(map, cords, title, icon, offer_id){
	var icon	= gmap.getIcon(icon);
	var point	= new google.maps.LatLng(cords[0], cords[1]);

	var marker = new google.maps.Marker({
		position: point,
		icon: icon,
		map: gmap['map-'+map],
		title: title
	});

	if (map == 'main'){
		google.maps.event.addListener(marker, 'click', function() {
			fb.openoffer(offer_id);
		});
	}

	var id	= ++gmap.seq;
	gmap.markers[map+'-'+id]	= marker;

	return [id, marker];
};
gmap.removePin = function(map, id){
	gmap.markers[map+'-'+id].setMap(null);
}


google.maps.event.addDomListener(window, 'load', gmap.initAll);