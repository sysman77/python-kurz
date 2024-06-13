# potrebujem nacitat data zo suboru

# potrebujem vyfiltrovat slova o dlžke 7+ pismen

# potrebuujem nove data zapisat do suboru

def load_data(path="data/text.txt"):
    f = open(path, "r")
    data = f.read()
    f.close()
    return data


def filter7(data):
    words = data.split(" ")
    #filtered_words = [w for w in words if len(w) > 6]
    filtered_words = []
    for w in words:
        if len(w) > 6:
            filtered_words.append(w)

    return filtered_words


def save_data(path, data):
    try:
        f = open(path, "w")
        f.write(", ".join(data))

    except:
        print("Došlo k chybe")

    finally:
        f.close()



data = load_data()
new_data = filter7(data)
save_data("data/filtered_text.txt", new_data)