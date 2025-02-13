def echo(text: str, repetitions: int = 3) -> str:
    "Imitate a real-world echo."
    echoes = []
    for i in range(repetitions, 0, -1):
        echoes.append(text[-i:])
    echoes.append(".")
    return "\n".join(echoes)


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
