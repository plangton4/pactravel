// gets pixel coordinates
function PixelCoords(map: any, latLong : any) : number[] {
    var scale = Math.pow(2, map.getZoom());
    var nw = new google.maps.LatLng(
        map.getBounds().getNorthEast().lat(),
        map.getBounds().getSouthWest().lng()
    );
    var worldCoordinateNW = map.getProjection().fromLatLngToPoint(nw);
    var worldCoordinate = map.getProjection().fromLatLngToPoint(latLong);
    var pixelOffset = new google.maps.Point(
        Math.floor((worldCoordinate.x - worldCoordinateNW.x) * scale),
        Math.floor((worldCoordinate.y - worldCoordinateNW.y) * scale)
    );
    return [0,0];
}

// Distance using lat/long isn't really euclidean...
function Distance(latLng1: any, latLng2: any) {
    return Math.sqrt(
        (latLng1.lat - latLng2.lat)**2 + 
        (latLng1.lng - latLng2.lng)**2
    )
}