document.addEventListener('DOMContentLoaded', function() {
    console.log('DOMContentLoaded');
    manipularFormulario();
});

async function carregarAnimais() {
    const response = await axios.get('http://localhost:8000/animais');
    const animais = response.data;
    const lista = document.getElementById('lista-animais');

    lista.innerHTML = ''

    animais.forEach(animal => {
        const item = document.createElement('li');
        item.innerText = animal.nome;
        lista.appendChild(item);
    });   
}

function manipularFormulario() {
    const form_animal = document.getElementById("form-animal");
    const input_nome = document.getElementById("nome");

    form_animal.addEventListener('submit', async (event) => {
        event.preventDefault();
        const nome_animal = input_nome.value;
        
        await axios.post('http://localhost:8000/animais', {
            id: '',
            nome: nome_animal,
            idade: 2,
            sexo: 'femea',
            cor: 'preta'
        })
        carregarAnimais()
        alert('Animal cadastrado...')

    });
}

console.log('Script carregado');
carregarAnimais();
