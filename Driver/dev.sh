node_modules/.bin/watchify app/main.js -v -t [ babelify --presets [ es2015 ] ] -o app/public/bundle.js &

node node_modules/.bin/http-server -p 8002 app/public
