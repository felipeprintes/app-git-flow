"""Main function responsible to set user information"""
def main():
    nome  = "fulano"
    idade = 25

    json_construct(nome, idade)

"""Function responsible to build a json with user data"""
def json_construct(nome, idade):
    json_user_information = {
        "nome": nome,
        "idade": idade
    }

    return json_user_information 


if __name__=="__main__":
    main()