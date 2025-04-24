from pathlib import Path

def explorar_sistema(directorio_inicial):    
    for ruta in Path(directorio_inicial).rglob('*'):
        try:
            if ruta.is_file():
                print(f"Ruta encontrada: {str(ruta.absolute())}")
                print(f"Nombre del archivo: {ruta.name}")
                print("-" * 50)
        except Exception:
            pass
    
if __name__ == "__main__":
    directorio = "./"
    explorar_sistema(directorio)
