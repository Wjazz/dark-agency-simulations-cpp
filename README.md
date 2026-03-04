<div align="center">
  
# 🧠 Dark Agency Simulations: HR Dynamics
*High-Performance Agent-Based Modeling (ABM) for People Analytics*

<img src="https://img.shields.io/badge/Engine-C%2B%2B17-00E5FF?style=for-the-badge&logo=c%2B%2B&logoColor=121212" />
<img src="https://img.shields.io/badge/Bridge-Pybind11-FFD700?style=for-the-badge&logo=python&logoColor=121212" />
<img src="https://img.shields.io/badge/Performance-10M_ticks_in_0.3s-FF1744?style=for-the-badge&logo=speedtest&logoColor=E0E0E0" />

</div>

---

### 🎯 Visión General

Este repositorio contiene un motor de simulación estocástica de alto rendimiento diseñado para modelar **Dinámicas de Poder, Riesgo de Rotación y Visibilidad Corporativa** en organizaciones sin estructuras jerárquicas estrictas.

Se basa en una adaptación matemática del **Modelo RAE (Random Asset Exchange)** de la economía física (Econofísica), traducido al dominio de *People Analytics*. El modelo demuestra cómo el "Capital Corporativo" (visibilidad, crédito por proyectos) tiende a concentrarse espontáneamente en un ~20% de los empleados, dejando al resto en la periferia de la red corporativa, aumentando su riesgo de *attrition*.

### ⚡ Arquitectura Híbrida (C++ / Python)

Para superar el cuello de botella del *Global Interpreter Lock (GIL)* de Python en simulaciones multi-agente masivas, este proyecto utiliza una arquitectura de memoria compartida:

1. **Núcleo de Simulación (C++17):** Escrito desde cero utilizando `std::vector` para contigüidad en memoria y `std::mt19937` (Mersenne Twister) para aleatoriedad criptográfica rápida.
2. **Puente de Memoria (Pybind11):** El código C++ se compila como una librería compartida (`.so`) que se importa de forma nativa en Python, permitiendo el traspaso de matrices de agentes directamente por la memoria RAM (Zero I/O disk bottleneck).
3. **Análisis y Visualización (Python):** Se utilizan Pandas y Seaborn para transformar los arreglos de memoria en Curvas de Lorenz (distribución de poder) y Mapas de Calor (silos organizacionales).

*🚀 Benchmark: 10,000 agentes ejecutando 10,000,000 de interacciones sociales se resuelven y transforman a Pandas DataFrame en **~0.30 segundos**.*

### 🛠️ Cómo compilar y ejecutar

**Requisitos:** `CMake (3.10+)`, `Compilador C++17 (GCC/Clang)`, `Python 3.10+`, `pybind11-devel`.

```bash
# 1. Compilar el motor C++ y el módulo Pybind11
mkdir build && cd build
cmake ..
make -j$(nproc)

# 2. Ejecutar la simulación desde Python
cd ../notebooks
python run_magic.py
