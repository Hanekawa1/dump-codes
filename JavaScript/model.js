//Modelando uma tabela em Sequelize

//Constante que instancia o módulo de modelos do Sequelize
const Model = Sequelize.Model;

//Definição de classe e herança do módulo de modelos
class Usuario extends Model {}

//Criação do modelo
Usuario.init({
    //Atributos da tabela
    //Para saber qual o tipo de data, consultar documentação do sequelize
    //https://sequelize.org/master/manual/data-types.html
    nome: { type: Sequelize.STRING, allowNull: false },
    cpf: { type: Sequelize.BIGINT, allowNull: false },
    codigo: {type: Sequelize.INTEGER} //allowNull é true por padrão
},
//Aqui ficam as opções de exportação do modelo do sequelize
{ sequelize, modelName: 'Usuario'});

//Exemplo de consultas com o modelo
Usuario.create({
    //Cria um objeto do modelo a partir de seus atributos e persiste os dados no banco
    nome: "Wender",
    cpf: 11234567890,
    codigo: 3
})
//Callback de confirmação da criação do objeto
.then(wender => {
    console.log("Usuário criado! Código: ", wender.codigo)
});