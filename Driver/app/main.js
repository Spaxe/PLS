const jshr = require('json-xhr');
const xhr = require('xhr');

var dynamic_pricing = document.getElementById('dynamic-pricing');
var total_price = document.getElementById('total-price');

var journey_cost = 0;

// Get current surge price
let update_current_price = () => {
  xhr.get({
    url: 'http://10.18.0.132:2999/api/current_price',
    timeout: 4900
  }, (error, resp, data) => {

    if (error) {
      console.error(error, data);
      dynamic_pricing.textContent = '$1.49/km';
      return;
    }

    try {
      let price = Number(JSON.parse(data).json[0].dynamic_price).toFixed(2);
      if (isNaN(price)) {
        dynamic_pricing.textContent = '$1.49/km';
      } else {
        dynamic_pricing.textContent = `$${price}/km`;
      }
    } catch (e) {
      dynamic_pricing.textContent = '$1.49/km';
    }

  });
};
window.setInterval(update_current_price, 5000);

// Update delta distance by driver tag
let send_distance = (distance) => {

  xhr.post({
    url: 'http://10.18.0.132:2999/api/journey',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    timeout: 1900,
    body: `distance_travelled=${distance}`
  }, (error, resp, body) => {
    if (error) {
      console.error(error);
    } else if (body.result !== 'success') {
      console.warn(body);
    }
    get_current_journey(error, distance);
  });

};
window.setInterval( () => {
  let r = Math.random();
  if (r < 0.6) {
    // send_distance(0);
  } else {
    send_distance(0.051111);
  }
}, 2000);

// Update total journey cost
let get_current_journey = (err, distance) => {

  xhr.get({
    url: 'http://10.18.0.132:2999/api/user',
    timeout: 1900
  }, (error, resp, data) => {

    if (error || err) {
      console.log(error);
      let fake_unit = 1.49;
      let cost = fake_unit * distance;
      journey_cost += cost;
      let price = journey_cost.toFixed(2);
      total_price.textContent = `$${price}`;
      return;
    }

    // XXX FIX ME

    try {
      journey_cost = Number(JSON.parse(data).json[0].current_journey_cost);
      var price = journey_cost.toFixed(2);
      if (isNaN(price) || !price) {
        total_price.textContent = '$0.00';
      } else {
        total_price.textContent = `$${price}`;
      }
    } catch (e) {
      total_price.textContent = `$${price}`;
    }

  });

};
