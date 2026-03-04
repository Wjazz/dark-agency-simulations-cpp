import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_gini(array):
    """Calcula el coeficiente de Gini para medir la desigualdad corporativa."""
    array = np.array(array, dtype=np.float64)
    array = array.flatten()
    if np.amin(array) < 0:
        array -= np.amin(array) # Valores no negativos
    array += 0.0000001 # Evitar divisiones por cero
    array = np.sort(array)
    index = np.arange(1, array.shape[0] + 1)
    n = array.shape[0]
    return ((np.sum((2 * index - n  - 1) * array)) / (n * np.sum(array)))

def plot_lorenz_and_heatmap(csv_path):
    print(f"Cargando datos de simulación desde {csv_path}...")
    df = pd.read_csv(csv_path)
    
    capital = df['corporate_capital'].values
    gini_index = calculate_gini(capital)
    
    # Preparar datos para la curva de Lorenz
    X_lorenz = np.cumsum(np.sort(capital)) / np.sum(capital)
    X_lorenz = np.insert(X_lorenz, 0, 0)
    
    # --- CONFIGURACIÓN ESTÉTICA (El Jailbreak) ---
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(16, 8))
    fig.patch.set_facecolor('#121212')
    
    # 1. CURVA DE LORENZ
    ax1 = plt.subplot(1, 2, 1)
    ax1.set_facecolor('#121212')
    ax1.plot(np.linspace(0.0, 1.0, X_lorenz.size), X_lorenz, color='#00E5FF', lw=2, label=f'Curva de Lorenz (Capital Corporativo)')
    ax1.plot([0,1], [0,1], color='#FF1744', linestyle='--', lw=2, label='Igualdad Perfecta')
    ax1.set_title(f"Distribución de Poder (Gini: {gini_index:.3f})", color='#FFD700', fontsize=14)
    ax1.set_xlabel("Fracción Acumulada de Empleados", color='#E0E0E0')
    ax1.set_ylabel("Fracción Acumulada de Capital", color='#E0E0E0')
    ax1.legend()
    ax1.grid(color='#333333', linestyle=':', linewidth=1)

    # 2. MAPA DE CALOR POR DEPARTAMENTOS
    ax2 = plt.subplot(1, 2, 2)
    ax2.set_facecolor('#121212')
    
    # Agrupar capital por departamento y crear una matriz sintética para el heatmap
    dept_capital = df.groupby('department_id')['corporate_capital'].sum().reset_index()
    # Simular una matriz espacial (red corporativa)
    heatmap_data = np.zeros((5, 5))
    for i in range(5):
        heatmap_data[i, i] = dept_capital.iloc[i]['corporate_capital'] if i < len(dept_capital) else 0

    sns.heatmap(heatmap_data, cmap="YlOrRd", annot=False, cbar=True, ax=ax2, square=True)
    ax2.set_title("Mapa de Calor: Concentración de Influencia", color='#FFD700', fontsize=14)
    ax2.set_xlabel("Silos", color='#E0E0E0')
    ax2.set_ylabel("Departamentos", color='#E0E0E0')

    plt.tight_layout()
    plt.savefig("simulacion_jailbreak.png", facecolor=fig.get_facecolor(), edgecolor='none')
    print("✅ Gráfico guardado como 'simulacion_jailbreak.png'")

if __name__ == "__main__":
    plot_lorenz_and_heatmap("../build/simulation_results.csv")
