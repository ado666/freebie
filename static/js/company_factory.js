fb.cfactory	= function(){
	this.__cache	= {};
	this.__pool		= {};
	this.init();
}
fb.cfactory.prototype = {
	init: function(){
		var self	= this;
		$.ajax({
			url: "/company/getall",
			method: "GET",
			cache: false,
			contentType: false,
			processData: false,
			success: function(data){
				for (var i = 0, l = data.length; i < l; i++){
					self.__cache[data[i].id]	= data[i];
				}
			}
		});
	},
	get: function (id){
		if (this.__cache.hasOwnProperty(id))	return this.__cache[id];
		console.error('error');
	}
}
fb.cfactory.__instance = null;
fb.cfactory.me = function(){
	if (!fb.cfactory.__instance)	fb.cfactory.__instance = new fb.cfactory();
	return fb.cfactory.__instance;
}

fb.ofactory	= function(){
	this.__cache	= {};
	this.__pool		= {};
	this.init();
}
fb.ofactory.prototype = {
	init: function(){
		$.ajax({
			url: "/offer/getall",
			method: "GET",
			cache: false,
			contentType: false,
			processData: false,
			success: function(data){
				for (var i = 0, l = data.length; i < l; i++){
					this.__cache[data[i].id]	= data[i];
				}
			}
		});
	},
	get: function (id){
		if (this.__cache.hasOwnProperty(id))	return this.__cache[id];
		console.error('error');
	}
}
fb.ofactory.__instance = null;
fb.ofactory.me = function(){
	if (!fb.cfactory.__instance)	fb.cfactory.__instance = new fb.cfactory();
	return fb.cfactory.__instance;
}