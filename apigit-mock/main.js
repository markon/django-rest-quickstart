// generated from example.json

mock.define("/pets", "get", function(req, res) {

  res.type("application/json");

  res.json(200, "Architect Einsteinium system");
});