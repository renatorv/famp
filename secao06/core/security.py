from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verificar_senha(senha: str, hash_senha: str) -> bool:
    """
        Função para verificar se a senha informada é igual a senha criptografada, comparando
        a senha em texto puro,  informada pelo usuário, e o hash da senha que estara salva no
        banco de dados durante a criação da conta.
    """
    return CRIPTO.verify(senha, hash_senha)

def gerar_hash_senha(senha: str) -> str:
    """
        Função para gera e retorna o hash da senha.
    """
    return CRIPTO.hash(senha)