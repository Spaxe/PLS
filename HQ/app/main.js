const _ = require('lodash');
const L = require('leaflet');
const xhr = require('xhr');
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

  xhr.get({
    url: 'http://10.18.0.132:2999/api/current_priority_congestion',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    timeout: 1900
  }, (error, resp, data) => {
    if (error) {
      console.error(error);
    } else if (JSON.parse(data).result !== 'success') {
      console.error('Failed to fetch priority congestion: ', data, error);
    }

    // FIXME, as we need data
    var delay = 0;
    try {
      delay = Number(data.response.json[0].priority_congestion);
    } catch (e) {
      console.error(e);
    }
    if (!delay) delay = 0;

    // Remove it from map for a moment
    freeway_layer.clearLayers();

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

    let inbound_text = `<p class="road-name">Eastern Freeway Priority Lane (Inbound)</p>`;
    if (delay > 3) {
      inbound_text += `<p>Congested: delayed by ${delay} minutes.</p>`;
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
      color: speed_colors[delay > 3 ? 2 : 0],
      weight: 5,
      interactive: true
    });
    freeway_layer.addLayer(outbound_polyline);

    let outbound_text = `<p class="road-name">Eastern Freeway Priority Lane (Outbound)</p>`;
    if (delay > 3) {
      outbound_text += `<p>Congested</p>`;
    } else {
      outbound_text += `<p>Low Utilisation</p>`;
    }

    // Add tooltip for traffic details
    let outbound_popup = L.popup().setContent(outbound_text);

    outbound_polyline.addEventListener('mousemove', event => {
      outbound_popup.setLatLng(event.latlng);
      map.openPopup(outbound_popup);
    });
  });

};
window.setInterval(draw_freeway, 2000);
draw_freeway();

let draw_real_time = () => {
  // Load all eastern freeway related segments from VicRoads real time API
  jshr.get("http://api.vicroads.vic.gov.au/vicroads/wfs?SERVICE=WFS&VERSION=1.1.0&REQUEST=GetFeature&TYPENAMES=vicroads%3Abluetooth_links&OUTPUTFORMAT=json&SRSNAME=EPSG%3A4326&CQL_FILTER=name+like+'%25Eastern+Fwy%25'&AUTH=eyJraWQiOiJRRFFQWDZVSDlQRExOOU9GQVowMlNFRFVYIiwic3R0IjoiYWNjZXNzIiwiYWxnIjoiSFMyNTYifQ.eyJqdGkiOiIzVGJlcmZuNmI0MnBzNTFVdkN3a3VOIiwiaWF0IjoxNDc1NTU1NTAwLCJpc3MiOiJodHRwczovL2FwaS5zdG9ybXBhdGguY29tL3YxL2FwcGxpY2F0aW9ucy80QXk3eUYybVFDaUJacVB6OUN5UVU4Iiwic3ViIjoiaHR0cHM6Ly9hcGkuc3Rvcm1wYXRoLmNvbS92MS9hY2NvdW50cy8zU01zbEJ0VVZGTFROc2wyVGY1N3ZVIiwiZXhwIjoxNDkxNDUzMTAwfQ.-LHSNHNyyg-n2wsKEkMGTpi9gXem4uKvw0cJGfOoTm4").then( data => {

    road_layer.clearLayers();

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

      // Update non-priority congestion delays to server
      if (name === 'Eastern Fwy, Blackburn Rd to Wellington St') {
        update_non_priority_delay(delay);
      }
    });
  }).catch( error => {
    console.error(error);
  });

};
window.setInterval(() => {
  draw_real_time();
}, 2000);
draw_real_time();
road_layer.addTo(map);


let update_non_priority_delay = (delay) => {
  xhr.post({
    url: 'http://10.18.0.132:2999/api/current_non_priority_congestion',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: `congestion=${Math.max(delay, 0)}`
  }, (error, resp, data) => {
    if (error) {
      console.error(error);
    } else if (JSON.parse(data).result !== 'success') {
      console.error('Failed to update delay: ', delay, error, data);
    }
  });
};


// Query dynamic pricing
var outbound_price = document.getElementById('outbound-price');
var inbound_price = document.getElementById('inbound-price');

jshr.get('http://10.18.0.132:2999/api/current_price').then( data => {

  let price = Number(data.response.json[0].dynamic_price).toFixed(2);
  if (isNaN(price)) {
    outbound_price.textContent = '$1.49/km';
    inbound_price.textContent = '$1.49/km';
  } else {
    outbound_price.textContent = `$${price}/km`;
    inbound_price.textContent = `$${price}/km`;
  }

}).catch( error => {
  console.error(error);
  inbound_price.textContent = '$1.49/km';
  outbound_price.textContent = '$1.49/km';
});

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