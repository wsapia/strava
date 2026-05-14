let page = 1;
let useImperial = true;
let activities = [];

// ------------------
// Navigation
// ------------------

function showPage(name) {
    document.querySelectorAll('.page').forEach(p => p.style.display='none');
    document.getElementById(name).style.display='block';

    if(name==="activities") loadActivities();
    if(name==="bikes") loadBikes();
}

// ------------------
// Unit Conversion
// ------------------

function dist(d){
    return useImperial ? (d*0.000621).toFixed(2)+" mi"
                       : (d/1000).toFixed(2)+" km"
}

function elev(e){
    return useImperial ? (e*3.280).toFixed(0)+" ft"
                       : e.toFixed(0)+" m"
}

function toggleUnits(){
    useImperial = !useImperial;
    renderActivities();
}

// ------------------
// Activities (paginated)
// ------------------

async function loadActivities(p=1){
    page = p;

    let res = await fetch(`/api/activities/?page=${page}`);
    activities = await res.json();

    renderActivities();
}

function renderActivities(){

    let html = "<tr><th>Name</th><th>Distance</th><th>Elevation</th></tr>";

    for(let a of activities){
        html += `
        <tr onclick="analyze(${a.id})">
            <td>${a.name}</td>
            <td>${dist(a.distance)}</td>
            <td>${elev(a.total_elevation_gain)}</td>
        </tr>
        `;
    }

    document.getElementById("activityTable").innerHTML = html;

    document.getElementById("pagination").innerHTML = `
        <button onclick="loadActivities(${page-1})" ${page==1?'disabled':''}>Prev</button>
        Page ${page}
        <button onclick="loadActivities(${page+1})">Next</button>
    `;
}

// ------------------
// Search
// ------------------

function filterActivities(q){
    q = q.toLowerCase();

    let filtered = activities.filter(a =>
        a.name.toLowerCase().includes(q)
    );

    let html = "<tr><th>Name</th><th>Distance</th><th>Elevation</th></tr>";

    for(let a of filtered){
        html += `
        <tr onclick="analyze(${a.id})">
            <td>${a.name}</td>
            <td>${dist(a.distance)}</td>
            <td>${elev(a.total_elevation_gain)}</td>
        </tr>
        `;
    }

    document.getElementById("activityTable").innerHTML = html;
}

// ------------------
// Segments
// ------------------

async function loadSegments(){

    let res = await fetch('/api/segments/');
    let data = await res.json();

    let html = "";

    for(let s of data){
        html += `<div>${s.name}</div>`;
    }

    document.getElementById("content").innerHTML = html;
}

// ------------------
// Ride Analysis
// ------------------

async function analyze(id){

    let res = await fetch('/api/activities/detail/'+id);
    let data = await res.json();

    let poly = decodePolyline(data.polyline);

    if (polylineLayer) map.removeLayer(polylineLayer);

    polylineLayer = L.polyline(poly).addTo(map);
    map.fitBounds(polylineLayer.getBounds());

    let streams = await fetch('/api/streams/'+id).then(r=>r.json());

    Plotly.newPlot('chart', [
        {x:streams.distance, y:streams.altitude, name:"Elevation"},
        {x:streams.distance, y:streams.velocity, name:"Speed"},
        {x:streams.distance, y:streams.heartrate, name:"HR"}
    ], {
        title:"Ride Metrics",
        xaxis:{title:"Distance"},
        yaxis:{title:"Value"}
    });

    // ✅ hover sync
    document.getElementById('chart').on('plotly_hover', e=>{
        let i = e.points[0].pointIndex;
        if(poly[i]) hoverMarker.setLatLng(poly[i]);
    });
}

// ------------------
// Bikes (formatted)
// ------------------

async function loadBikes(){

    let res = await fetch('/api/bikes/');
    let data = await res.json();

    let html = "<table><tr><th>Name</th><th>Miles</th><th>Rides</th></tr>";

    for(let id in data){
        let b = data[id];

        html += `
        <tr>
            <td>${b.name}</td>
            <td>${dist(b.distance)}</td>
            <td>${b.rides}</td>
        </tr>
        `;
    }

    html += "</table>";

    document.getElementById("bikeTable").innerHTML = html;
}

function decodePolyline(str) {
    let index = 0, lat = 0, lng = 0, coordinates = [];

    while (index < str.length) {
        let shift = 0, result = 0, byte;

        do {
            byte = str.charCodeAt(index++) - 63;
            result |= (byte & 0x1f) << shift;
            shift += 5;
        } while (byte >= 0x20);

        let dlat = ((result & 1) ? ~(result >> 1) : (result >> 1));
        lat += dlat;

        shift = 0;
        result = 0;

        do {
            byte = str.charCodeAt(index++) - 63;
            result |= (byte & 0x1f) << shift;
            shift += 5;
        } while (byte >= 0x20);

        let dlng = ((result & 1) ? ~(result >> 1) : (result >> 1));
        lng += dlng;

        coordinates.push([lat / 1e5, lng / 1e5]);
    }

    return coordinates;
}



async function sync(){
    await fetch('/api/activities/sync');
    alert("Sync complete");
}



let map = L.map('map').setView([37.8, -122.4], 10);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png')
.addTo(map);

let polylineLayer;
let hoverMarker = L.marker([0,0]).addTo(map);


Plotly.newPlot('chart', data, layout);

document.getElementById('chart').on('plotly_hover', function(d){

    let idx = d.points[0].pointIndex;

    // fake mapping for now (replace with lat/lng streams later)
    marker.setLatLng([37.8 + idx*0.0001, -122.4]);
});
