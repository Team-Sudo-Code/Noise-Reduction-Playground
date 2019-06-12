var DeepAffects = require('deep-affects');
var deepAffectsAPIkey=require("../api-keys.js").deepAffectsAPIkey;
var fs = require("fs");

var defaultClient = DeepAffects.ApiClient.instance;

// Configure API key authorization: UserSecurity
var UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = deepAffectsAPIkey;

var api = new DeepAffects.DenoiseApi();

var body = DeepAffects.Audio.fromFile("input.wav"); // {Audio} Audio object that needs to be denoised.

//webhook = "http://your/webhook/"
var callback = function (error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('API called successfully. Returned data: ', Object.keys(data));
        fs.writeFile("output.wav", new Buffer.alloc(data.content, "base64"), function (err) { });
    }
};
api.syncDenoiseAudio(body, callback);
//api.asyncDenoiseAudio(body, webhook, callback);