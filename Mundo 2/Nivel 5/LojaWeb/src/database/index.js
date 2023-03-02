const mongoose = require("mongoose");
/* Modifique a conexão do banco de dados MongoDB de acordo com a sua instalação.
*/
mongoose
  .connect(
    "mongodb://desenv:Fortaleza@localhost:27017/?authMechanism=DEFAULT"
  )
  .then(() => {
    console.log("Conectado ao MongoDB!");
  })
  .catch((err) => console.log(err));

mongoose.Promise = global.Promise;

module.exports = mongoose;
