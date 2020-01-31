//Adicionar a linha abaixo nos scripts do package.json
//"test": "mocha test --timeout 15000 --exit"

//Importação das libs
var should = require('should');
var request = require('request');
var chai = require('chai');
var expect = chai.expect;
var urlBase = "http://api.magicthegathering.io/v1";

//Descrição do teste (describe)
describe("Teste na API magicthegathering.io", () => {
    //O que será testado (it)
    it("Deve receber 100 cartas", (done) => {
        request.get({url : urlBase + '/cards'}, (err, res, body) => {
            var _body = {};

            try{
                _body = JSON.parse(body);
            } catch(e){
                _body = {}
            }

            //Verifica se o resultado é o esperado (expect)
            expect(res.statusCode).to.equal(200);

            if(_body.should.have.property('cards')){
                expect(_body.cards).to.have.lengthOf.at.most(100);
            }

            //Finaliza os testes
            done();
        });
    });


    it("Deve receber a carta 'A indiferente' ", (done) => {
        request.get({url: urlBase + "/cards?name=Heedless One"}, async (err, res, body) => {
            var _body = {};
              
            try{
                _body = JSON.parse(body);
            } catch(e){
                _body = {}
            }

            expect(res.statusCode).to.equal(200);

            if(_body.should.have.property('cards')){
                expect(_body.cards).to.have.lengthOf.at.least(1);

                if(_body.cards[0].should.have.property('artist')){
                    expect(_body.cards[0].artist).to.equal('Mark Zug');
                }

                if(_body.cards[0].should.have.property('name')){
                    expect(_body.cards[0].name).to.equal('Heedless One');
                }
            }

            done();
        });
    });
});