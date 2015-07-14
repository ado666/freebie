window.gmap	= {
	seq: 0,
	markers: {},
	geocoder: null
};

gmap.initAll = function(){
	gmap.init('main');
//	gmap.init('offer');
}

gmap.init	=  function (map) {
	var mapCanvas = document.getElementById('map-canvas-'+map);
	gmap.geocoder = new google.maps.Geocoder();
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
				for (var n = 0, m = offer.addresses.length; n < m; n++){
					gmap.addPin('main', [offer.addresses[n].lat, offer.addresses[n].lng], offer.name, offer.icon, offer.id)
				}
			}
		}
	});
	}
	if (map == 'offer1'){
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

			var x = place.geometry.location.A;
			var y = place.geometry.location.F;

			var pin	= gmap.addPin('offer', [x,y]);
			gmap.offerPin	= pin[0]
			var marker	= pin[1];

			$('#offer_lat').text(x);
			$('#offer_lng').text(y);

			marker.setPosition(place.geometry.location);
			if (marker.offerPin)marker.offerPin.setVisible(true);

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
	if (map == 'address'){
		map = gmap['map-address'];
		infowindow = new google.maps.InfoWindow();

		var input = (document.getElementById('pac-input-address'));

//		map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
		var autocomplete = new google.maps.places.Autocomplete(input);
		autocomplete.bindTo('bounds', gmap['map-address']);

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

			var x = place.geometry.location.A;
			var y = place.geometry.location.F;

			if (gmap.addressPin)	gmap.removePin('address', gmap.addressPin)
			var pin	= gmap.addPin('address', [x,y]);
			gmap.addressPin	= pin[0]
			var marker	= pin[1];

			$('#address_lat').text(x);
			$('#address_lng').text(y);

			marker.setPosition(place.geometry.location);
			if (marker.addressPin) marker.addressPin.setVisible(true);

			var address = '';
			if (place.address_components) {
				address = [
					(place.address_components[0] && place.address_components[0].short_name || ''),
					(place.address_components[1] && place.address_components[1].short_name || ''),
					(place.address_components[2] && place.address_components[2].short_name || '')
				].join(' ');
			}
			infowindow.setContent('<div><strong>' + place.name + '</strong><br>' + address);
			infowindow.open(map, gmap.addressPin);
		});
	}
}

gmap.iconbase	= 'https://maps.google.com/mapfiles/kml/shapes/';

gmap.getIcon	= function(type){
	return;
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

gmap.getAddress = function(lat, lng, cb){
	var geocoder = gmap.geocoder;
var latlng = new google.maps.LatLng(lat, lng);
  geocoder.geocode({
    'latLng': latlng
  }, function (results, status) {
    if (status === google.maps.GeocoderStatus.OK) {
      if (results[0]) {
        cb(results[0]);
      } else {
        alert('No results found');
      }
    } else {
      alert('Geocoder failed due to: ' + status);
    }
  });
}


google.maps.event.addDomListener(window, 'load', gmap.initAll);