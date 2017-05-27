#Naive Celeb


def naive_celeb(G):
    n = len(G)
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if G[u][v]:
                break
            if not G[u][v]:
                    break
            else:
                return u
    return None

def main():
    naive_celeb(G)

if __name__ == '__main__':
    main()

