import sys
import os
import time
import pandas as pd

# Calcular la ruta exacta de la carpeta 'build' sin importar desde dónde se ejecute
current_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.abspath(os.path.join(current_dir, "../build"))
sys.path.append(build_dir)

# Ahora sí, invocamos la magia
import dark_agency
from RAE_Organizational_Viz import plot_lorenz_and_heatmap

def main():
    print(f"🔍 Buscando motor C++ en: {build_dir}")
    print("⚡ Invocando el motor nativo C++ desde Python...")
    
    # EL DISPARO DE MAGIA NEGRA
    start_time = time.time()
    results = dark_agency.run_rae_simulation(
        num_agents=10000, 
        initial_capital=100.0, 
        iterations=10000000
    )
    end_time = time.time()
    
    print(f"✅ 10 millones de conflictos corporativos resueltos en {end_time - start_time:.4f} segundos.")
    
    # Transformar los objetos C++ a un DataFrame de Pandas
    print("🔄 Transformando memoria C++ a Pandas DataFrame...")
    data = [{
        'employee_id': emp.id, 
        'corporate_capital': emp.corporate_capital, 
        'department_id': emp.department_id
    } for emp in results]
    
    df = pd.DataFrame(data)
    
    # Generar el arte visual
    temp_csv = os.path.join(build_dir, "simulation_results_ram.csv")
    df.to_csv(temp_csv, index=False)
    
    print("🎨 Trazando el lienzo analítico...")
    plot_lorenz_and_heatmap(temp_csv)
    print("Misión Cumplida.")

if __name__ == "__main__":
    main()
