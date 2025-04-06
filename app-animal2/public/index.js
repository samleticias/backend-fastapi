const dialog = document.getElementById('detalhes-dialog');
const conteudo = document.getElementById('detalhes-conteudo');
const fecharBtn = document.getElementById('fechar-detalhes');

fecharBtn.addEventListener('click', () => {
  dialog.close();
});

async function carregarAnimais() {
  const response = await axios.get('http://localhost:8000/animais');
  const animais = response.data;
  const lista = document.getElementById('lista-animais');
  lista.innerHTML = '';

  animais.forEach(animal => {
    const item = document.createElement('li');

    const texto = document.createElement('span');
    texto.innerText = `${animal.nome} - Idade: ${animal.idade} - Cor: ${animal.cor}`;

    const botaoRemover = document.createElement('button');
    botaoRemover.innerText = 'Remover';
    botaoRemover.onclick = async () => {
      await axios.delete(`http://localhost:8000/animais/${animal.id}`);
      carregarAnimais();
    };

    const botaoDetalhes = document.createElement('button');
    botaoDetalhes.innerText = 'Detalhes';
    botaoDetalhes.onclick = () => {
    const conteudoHTML = `
        <strong>Nome:</strong> ${animal.nome}<br>
        <strong>Idade:</strong> ${animal.idade}<br>
        <strong>Sexo:</strong> ${animal.sexo}<br>
        <strong>Cor:</strong> ${animal.cor}
    `.trim();
    conteudo.innerHTML = conteudoHTML;
    dialog.showModal();
    };

    item.appendChild(texto);
    item.appendChild(botaoDetalhes);
    item.appendChild(botaoRemover);
    lista.appendChild(item);
  });
}

function manipularFormulario() {
  const form = document.getElementById('form-animal');
  const nome = document.getElementById('nome');
  const idade = document.getElementById('idade');
  const sexo = document.getElementById('sexo');
  const cor = document.getElementById('cor');

  form.onsubmit = async (event) => {
    event.preventDefault();

    await axios.post('http://localhost:8000/animais', {
      nome: nome.value.trim(),
      idade: parseInt(idade.value),
      sexo: sexo.value,
      cor: cor.value.trim()
    });

    nome.value = '';
    idade.value = '';
    sexo.value = '';
    cor.value = '';

    carregarAnimais();
    alert('Animal cadastrado com sucesso!');
  };
}

function app() {
  console.log('App iniciado');
  carregarAnimais();
  manipularFormulario();
}

app();