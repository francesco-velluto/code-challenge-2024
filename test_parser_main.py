from input_parser.parser import Parser
import heapq
    
def main():
    file_path = "input_file.txt"
    
    parsed_data = Parser.parse_file(file_path)
    

    # Esempio di rappresentazione di un grafo ponderato
    # Dove ogni chiave è un nodo e ogni valore è una lista di tuple (nodo_destinazione, costo, silver_point)
    grafo = {
        'A': [('B', 2, 1), ('C', 3, 2)],
        'B': [('D', 1, 3)],
        'C': [('D', 4, 2), ('E', 5, 1)],
        'D': [('F', 2, 4)],
        'E': [('F', 1, 1)],
        'F': []  # Nodo finale
    }

    def dijkstra_modificato(grafo, nodo_inizio, nodo_fine):
        # Coda di priorità
        coda = [(0, 0, nodo_inizio, [])]  # (costo totale, silver_point totale, nodo attuale, percorso)
        visitati = set()

        while coda:
            cost, sp, node, path = heapq.heappop(coda)

            # Aggiorna il percorso
            path = path + [node]

            # Se il nodo è già stato visitato, raddoppia i valori
            if node in visitati:
                cost *= 2
                sp *= 2
            else:
                visitati.add(node)

            # Se abbiamo raggiunto il nodo finale
            if node == nodo_fine:
                return cost, sp, path

            # Esplora i nodi vicini
            for next_node, weight, silver_point in grafo.get(node, []):
                if next_node not in visitati or True:  # Semplificazione, normalmente qui andrebbe la logica per gestire la revisita
                    nuovo_costo = cost + weight
                    nuovo_sp = sp + silver_point
                    heapq.heappush(coda, (nuovo_costo, nuovo_sp, next_node, path))
        
        return float("inf"), 0, []

    # Assumi 'A' come nodo inizio e 'F' come nodo fine
    costo_minimo, silver_points_totali, percorso = dijkstra_modificato(grafo, 'A', 'F')
    print(f"Costo Minimo: {costo_minimo}, Silver Points Totali: {silver_points_totali}, Percorso: {' -> '.join(percorso)}")
    
    Parser.generate_output("output_file.json")
    print(parsed_data)
    

if __name__ == "__main__":
    main()