const _ = require('lodash');
const L = require('leaflet');
const jshr = require('json-xhr');
const eastern_freeway = require('./eastern-freeway');

// Create map container
var mapDiv = document.getElementById('map')
var map = L.map(mapDiv).setView([-37.8020905, 145.0918024], 13);

// Add basemap for background
var basemap = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',
            { attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="https://carto.com/attributions">CARTO</a>' }).addTo(map);

var speed_colors = ['#01b3fd', '#ff9e00', '#ff0000'];
var road_layer = L.layerGroup();
var freeway_layer = L.layerGroup();

// Display mode
var mode = 'non-priority';

// Draw eastern freeway inbound / outbound
let draw_freeway = () => {

  // Invert lat lng for leaflet
  let inbound_coords = eastern_freeway.inbound.map(([x, y]) => {
    return [y, x];
  });
  let outbound_coords = eastern_freeway.outbound.map(([x, y]) => {
    return [y, x];
  });

  // Draw the eastern freeway line in colour
  let inbound_polyline = L.polyline(inbound_coords, {
    className: 'road-segment',
    color: speed_colors[0],
    weight: 5,
    interactive: true
  });
  freeway_layer.addLayer(inbound_polyline);

  // XXX FIXME TEMPORARY, as we need data
  let delay = 0;

  let inbound_text = `<p class="road-name">Eastern Freeway Priority Lane (Inbound)</p>`;
  if (delay > 0) {
    inbound_text += `<p>Congested</p>`;
  } else {
    inbound_text += `<p>Low Utilisation</p>`;
  }

  // Add tooltip for traffic details
  let inbound_popup = L.popup()
    .setContent(inbound_text);

  inbound_polyline.addEventListener('mousemove', event => {
    inbound_popup.setLatLng(event.latlng);
    map.openPopup(inbound_popup);
  });

  // Draw the eastern freeway line in colour
  let outbound_polyline = L.polyline(outbound_coords, {
    className: 'road-segment',
    color: speed_colors[0],
    weight: 5,
    interactive: true
  });
  freeway_layer.addLayer(outbound_polyline);

  let outbound_text = `<p class="road-name">Eastern Freeway Priority Lane (Outbound)</p>`;
  if (delay > 0) {
    outbound_text += `<p>Congested</p>`;
  } else {
    outbound_text += `<p>Low Utilisation</p>`;
  }

  // Add tooltip for traffic details
  let outbound_popup = L.popup()
    .setContent(outbound_text);

  outbound_polyline.addEventListener('mousemove', event => {
    outbound_popup.setLatLng(event.latlng);
    map.openPopup(outbound_popup);
  });
};
draw_freeway();

let draw_real_time = () => {
  // Load all eastern freeway related segments from VicRoads real time API
  jshr.get("http://api.vicroads.vic.gov.au/vicroads/wfs?SERVICE=WFS&VERSION=1.1.0&REQUEST=GetFeature&TYPENAMES=vicroads%3Abluetooth_links&OUTPUTFORMAT=json&SRSNAME=EPSG%3A4326&CQL_FILTER=name+like+'%25Eastern+Fwy%25'&AUTH=eyJraWQiOiJRRFFQWDZVSDlQRExOOU9GQVowMlNFRFVYIiwic3R0IjoiYWNjZXNzIiwiYWxnIjoiSFMyNTYifQ.eyJqdGkiOiIzVGJlcmZuNmI0MnBzNTFVdkN3a3VOIiwiaWF0IjoxNDc1NTU1NTAwLCJpc3MiOiJodHRwczovL2FwaS5zdG9ybXBhdGguY29tL3YxL2FwcGxpY2F0aW9ucy80QXk3eUYybVFDaUJacVB6OUN5UVU4Iiwic3ViIjoiaHR0cHM6Ly9hcGkuc3Rvcm1wYXRoLmNvbS92MS9hY2NvdW50cy8zU01zbEJ0VVZGTFROc2wyVGY1N3ZVIiwiZXhwIjoxNDkxNDUzMTAwfQ.-LHSNHNyyg-n2wsKEkMGTpi9gXem4uKvw0cJGfOoTm4").then( data => {

    let features = data.response.features;
    features.forEach(feature => {
      let coords = feature.geometry.coordinates;
      let name = feature.properties.name;
      let delay = feature.properties.excess_delay;

      // Flip coords long lat to lat long for Leaflet
      coords = coords.map(([x, y]) => {
        return [y, x];
      });

      // calculate speed category for blue, amber, and red
      let speed_category = Math.max(Math.min(Math.floor(delay), 2), 0);

      // Draw the traffic line in colour
      let polyline = L.polyline(coords, {
        className: 'road-segment',
        color: speed_colors[speed_category],
        weight: 5,
        interactive: true
      });
      road_layer.addLayer(polyline);

      // Copy properties and calculate the congestion details and delays, if any
      polyline.properties = feature.properties;

      let text = `<p class="road-name">${name}</p>`;
      if (delay > 0) {
        text += `<p>Delayed by ${delay} minutes</p>`;
      } else if (delay == 0) {
        text += `<p>No delay</p>`;
      } else {
        text += `<p>${-delay} minutes early</p>`;
      }

      // Add tooltip for traffic details
      let popup = L.popup()
        .setContent(text);

      polyline.addEventListener('mousemove', event => {
        popup.setLatLng(event.latlng);
        map.openPopup(popup);
      });
    });
  });

};
draw_real_time();
road_layer.addTo(map);

// Interaction
var priority_mode = document.getElementById('priority');
var non_priority_mode = document.getElementById('non-priority');

priority_mode.addEventListener('click', event => {
  map.removeLayer(road_layer);
  map.addLayer(freeway_layer);
  priority_mode.classList.add('selected');
  non_priority_mode.classList.remove('selected');
  map.closePopup();
});

non_priority_mode.addEventListener('click', event => {
  map.addLayer(road_layer);
  map.removeLayer(freeway_layer);
  non_priority_mode.classList.add('selected');
  priority_mode.classList.remove('selected');
  map.closePopup();
});