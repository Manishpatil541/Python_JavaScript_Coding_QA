// program for sorting object

var obj  = {
    'mon':50,
    'tue':25,
    'wed':0,
    'thu':250,
    'fri':100,
    'sat':125,
    'sun':530
};
let new_obj = {};
while (Object.keys(obj ).length) {
    var key = Object.keys(obj ).reduce((a, b) => obj [a] > obj [b] ? a : b);
    new_obj[key] = obj [key];
    delete obj [key];
}
obj  = new_obj;
console.log(obj );