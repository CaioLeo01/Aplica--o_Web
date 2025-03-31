<template>
  <div id="app">
    <h1>Dados do CSV</h1>
 
    <!-- Tabela para mostrar os dados -->
    <table v-if="dados.length > 0">
      <thead>
        <tr>
          <th v-for="(value, key) in dados[0]" :key="key">{{ key }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(dado, index) in dados" :key="index">
          <td v-for="(value, key) in dado" :key="key">{{ value }}</td>
        </tr>
      </tbody>
    </table>
    
    <!-- Caso não haja dados, exibe uma mensagem -->
    <p v-else>Não há dados para exibir</p>

    <!-- Formulário para adicionar novos dados -->
    <form @submit.prevent="adicionarDado">
      <input v-model="novoDado.nome" placeholder="Nome" required />
      <input v-model="novoDado.idade" placeholder="Idade" required />
      <button type="submit">Adicionar</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      dados: [], // Armazena os dados lidos do backend
      novoDado: {
        nome: '',
        idade: ''
      }
    };
  },
  mounted() {
    // Quando o componente é montado, faça uma requisição para obter os dados
    this.obterDados();
  },
  methods: {
    // Método para obter os dados do backend (CSV)
    async obterDados() {
      try {
        const response = await axios.get('http://localhost:5000/dados');
        this.dados = response.data; // Armazena os dados recebidos na variável 'dados'
      } catch (error) {
        console.error('Erro ao obter dados:', error);
      }
    },
    // Método para adicionar um novo dado no backend
    async adicionarDado() {
      try {
        const response = await axios.post('http://localhost:5000/dados', this.novoDado);
        
        // Após adicionar o dado, atualiza a lista de dados
        this.dados.push(response.data); // Adiciona o dado à lista de dados local

        // Limpa os campos do formulário
        this.novoDado.nome = '';
        this.novoDado.idade = '';
      } catch (error) {
        console.error('Erro ao adicionar dado:', error);
      }
    }
  }
};
</script>

<style scoped>
/* Estilos simples */
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: left;
}

form {
  margin-top: 20px;
}

input {
  margin-right: 10px;
}
</style>
