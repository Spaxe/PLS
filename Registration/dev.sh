node_modules/.bin/watchify app/main.js -v -t [ babelify --presets [ es2015 ] ] -o app/public/bundle.js &

node app.js