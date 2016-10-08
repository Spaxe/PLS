const jshr = require('json-xhr');
const xhr = require('xhr');

var dynamic_pricing = document.getElementById('dynamic-pricing');
var total_price = document.getElementById('total-price');

var journey_cost = 0;

// Get current surge price
let update_current_price = () => {
  xhr.get({
    url: 'http://10.18.0.132:2999/api/current_price',
    timeout: 1900
  }, (error, resp, data) => {

    if (error) {
      console.error(error);
      dynamic_pricing.textContent = '$14.99/km';
      return;
    }

    let price = Number(data.response.json[0].dynamic_price).toFixed(2);
    if (isNaN(price)) {
      dynamic_pricing.textContent = '$14.99/km';
    } else {
      dynamic_pricing.textContent = `$${price}/km`;
    }

  });
};
window.setInterval(update_current_price, 2000);

// Update delta distance by driver tag
let send_distance = (distance) => {

  xhr({
    url: 'http://10.18.0.132:2999/api/journey',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    method: 'POST',
    timeout: 1900,
    body: `distance_travelled=${distance}`
  }, (error, resp, body) => {
    if (error) {
      console.error(error);
    } else if (body.result !== 'success') {
      console.warn(body);
    }
  });

  get_current_journey(distance);

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
let get_current_journey = (distance) => {

  xhr.get({
    url: 'http://10.18.0.132:2999/api/user',
    timeout: 1900
  }, (error, resp, data) => {

    if (error) {
      console.log(error);
      let fake_unit = 14.99;
      let cost = fake_unit * distance;
      journey_cost += cost;
      let price = journey_cost.toFixed(2);
      total_price.textContent = `$${price}`;
      return;
    }

    // XXX FIX ME
    journey_cost = Number(data.response.json[0].total_cost);
    let price = journey_cost.toFixed(2);
    if (isNaN(price)) {
      total_price.textContent = '$0.00';
    } else {
      total_price.textContent = `$${price}`;
    }

  });

};
