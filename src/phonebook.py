class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome invalido'

        if len(number) <= 0:
            return 'Numero invalido'  # erro na escrita

        # Validar com o cliente a regra correta
        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome invalido'

        result = []
        for key, value in self.entries.items():
            if name in key:
                return value
        else:
            return 'Contato não encontrado'

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        resultado = []
        for nome in self.entries.keys():
            resultado.append(nome)
        return resultado

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        resultado = []
        for numero in self.entries.values():
            resultado.append(numero)
        return resultado

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name in name:
                result.append({name, number})
        if len(result) == 0:
            return "Nome não encontrado"
        else:
            return result

    def get_phonebook_sorted(self):
        """
        :return: return phonebook in sorted order
        """
        # Correção: o método foi alterado para retornar todos os números em ordem crescente.
        lista_numeros = self.get_numbers()

        lista_numeros.sort()
        return lista_numeros

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """

        # Correção: o método foi alterado para retornar todos os números em ordem decrescente.

        lista_numeros = self.get_numbers()

        lista_numeros.sort(reverse=True)
        return lista_numeros

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        tamanho = int(len(self.entries))
        if tamanho > 0:
            if name != None:
                for key, number in self.entries.items():
                    if name == key:
                        self.entries.pop(key, number)
                        return "Numero deletado"
                return "Usuario não encontrado"
            else:
                return "O nome passado não pode ser None"
        else:
            return "Não existe registrados cadastrados"

    def change_number(self, name, number):
        tamanho = int(len(self.entries))
        if tamanho > 0:
            if (name != None) or (number != None):
                for key, value in self.entries.items():
                    if name == key:
                        self.entries.update({name: number})
                        return "Numero atualizado"
                return "Usuario não encontrado"
            else:
                return "O nome ou o número passado não pode ser None"
        else:
            return "Não existe registrados cadastrados"

    def get_name_by_number(self, number):
        tamanho = int(len(self.entries))
        if tamanho > 0:
            if number != None:
                for key, value in self.entries.items():
                    if number == value:
                        return key
            else:
                return "O nome ou o número passado não pode ser None"
        else:
            return "Não existe registrados cadastrados"

