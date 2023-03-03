from src.phonebook import Phonebook

class TestPhonebook:

    def test_add_name_and_number_valid(self):
        # Setup
        phonebook = Phonebook()
        name = "Joao"
        number = "8212"
        message = "Numero adicionado"

        # Chamada
        result = phonebook.add(name, number)

        # Avaliacao
        assert message == result

    def test_add_name_with_special_characters_arroba(self):
        # Setup
        phonebook = Phonebook()
        name = "Jo@o"
        number = "12345"
        message = "Nome invalido"

        # Chamada
        result = phonebook.add(name, number)

        # Avaliacao
        assert message == result

    def test_add_name_with_special_characters_exclamation(self):
        # Setup
        phonebook = Phonebook()
        name = "Jo!o"
        number = "12345"
        message = "Nome invalido"

        # Chamada
        result = phonebook.add(name, number)

        # Avaliacao
        assert message == result

    def test_add_name_with_special_characters_hashtag(self):
        # Setup
        phonebook = Phonebook()
        name = "Jo#o"
        number = "12345"
        message = "Nome invalido"

        # Chamada
        result = phonebook.add(name, number)

        # Avaliacao
        assert message == result

    def test_add_name_with_special_characters_dollar_sign(self):
        # Setup
        phonebook = Phonebook()
        name = "Jo$o"
        number = "12345"
        message = "Nome invalido"

        # Chamada
        result = phonebook.add(name, number)

        # Avaliacao
        assert message == result

    def test_add_name_with_special_characters_percent(self):
        # Setup
        phonebook = Phonebook()
        name = "Jo%o"
        number = "12345"
        message = "Nome invalido"

        # Chamada
        result = phonebook.add(name, number)

        # Avaliacao
        assert message == result

    def test_add_number_with_string_empty(self):
        # Setup
        phonebook = Phonebook()
        name = "Joao"
        number = ""
        message = "Numero invalido"

        # Chamada
        result = phonebook.add(name, number)

        # Avaliacao
        assert message == result

    def test_clear(self):
        # Setup
        phonebook = Phonebook()
        name = "Joao"
        number = "123456"
        message = "phonebook limpado"
        phonebook.add(name, number)

        # Chamada
        result = phonebook.clear()

        # Avaliacao
        assert message == result

    def test_delete_by_name(self):
        # Setup
        phonebook = Phonebook()
        name = "Joao"
        number = "123456"
        message = "Numero deletado"
        phonebook.add(name, number)

        # Chamada
        result = phonebook.delete(name)

        # Avaliacao
        assert message == result

    def test_delete_by_name_not_registred(self):
        # Setup
        phonebook = Phonebook()
        message = "Usuario não encontrado"
        name_search = "Felipe"

        # Chamada
        result = phonebook.delete(name_search)

        # Avaliacao
        assert message == result

    def test_delete_by_name_none(self):
        #Setup
        phonebook = Phonebook()
        message = "O nome passado não pode ser None"
        name = None

        #Chamada
        result = phonebook.delete(name)

        #Avaliacao
        assert message == result

    def test_delete_by_dictionary_empty(self):
        #Setup
        phonebook = Phonebook()
        name = "Joao"
        phonebook.entries = {}
        message = "Não existe registrados cadastrados"

        #Chamada
        result = phonebook.delete(name)

        #Avaliacao
        assert message == result

    def test_change_number_by_name_exists(self):
        # Setup
        phonebook = Phonebook()
        name = "Joao"
        number = "1234"
        phonebook.add(name,number)
        new_number = "12345"
        message = "Numero atualizado"

        # Chamada
        result = phonebook.change_number(name, new_number)

        # Avaliacao
        assert message == result

    def test_change_number_by_name_not_exists(self):
        # Setup
        phonebook = Phonebook()
        name = "Joao"
        number = "1234"
        phonebook.add(name, number)
        name_search = "Felipe"
        new_number = "12345"
        message = "Usuario não encontrado"

        # Chamada
        result = phonebook.change_number(name_search, new_number)

        # Avaliacao
        assert message == result

    def test_get_name_by_number(self):
        # Setup
        phonebook = Phonebook()
        name = "Joao"
        number = "12345"
        phonebook.add(name, number)

        # Chamada
        result = phonebook.get_name_by_number(number)

        # Avaliacao
        assert name == result

    def test_get_names(self):
        # Setup
        phonebook = Phonebook()
        name = "Joao"
        number = "12345"
        phonebook.add(name, number)
        expected = ['POLICIA', 'Joao']

        # Chamada
        result = phonebook.get_names()

        # Avaliacao
        assert expected == result

    def test_get_numbers(self):
        # Setup
        phonebook = Phonebook()
        name = "Joao"
        number = "12345"
        phonebook.add(name, number)
        expected = ['190', '12345']

        # Chamada
        result = phonebook.get_numbers()

        # Avaliacao
        assert expected == result

    def test_lookup_nome_cadastrado(self):
        # Setup
        phonebook = Phonebook()
        name = "Joao"
        number = "12345"
        phonebook.add(name, number)

        # Chamada
        result = phonebook.lookup(name)

        # Avaliacao
        assert number == result

    def test_lookup_nome_nao_cadastrado(self):
        # Setup
        phonebook = Phonebook()
        name = "Joao"
        message_expected = "Contato não encontrado"
        # Chamada
        result = phonebook.lookup(name)

        # Avaliacao
        assert message_expected == result

    def test_search_nome_cadastrado(self):
        # Setup
        phonebook = Phonebook()
        name = "Joao"
        number = "12345"
        phonebook.add(name, number)
        message_expected = [{'Joao','12345'}]

        # Chamada
        result = phonebook.search(name)

        # Avaliacao
        assert message_expected == result

    def test_search_nome_nao_cadastrado(self):
        # Setup
        phonebook = Phonebook()
        name = "Joao"
        message_expected =  "Nome não encontrado"

        # Chamada
        result = phonebook.search(name)

        # Avaliacao
        assert message_expected == result