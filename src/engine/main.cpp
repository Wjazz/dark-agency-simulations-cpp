#include <iostream>
#include <vector>
#include <random>
#include <fstream>
#include <chrono>
#include "agent.hpp"

using namespace DarkAgency;

class RAESimulation {
private:
    std::vector<Employee> employees;
    std::mt19937 rng; // Mersenne Twister: El estándar de oro en simulación estocástica
    std::uniform_int_distribution<int> agent_dist;
    std::uniform_real_distribution<double> fraction_dist;

public:
    RAESimulation(int num_agents, double initial_capital) 
        : rng(std::random_device{}()), 
          agent_dist(0, num_agents - 1), 
          fraction_dist(0.0, 1.0) 
    {
        employees.reserve(num_agents);
        for (int i = 0; i < num_agents; ++i) {
            // Asignamos departamentos del 1 al 5 aleatoriamente
            int dept = (i % 5) + 1;
            employees.push_back({i, initial_capital, dept});
        }
    }

    void tick() {
        // Elegimos dos empleados al azar
        int i = agent_dist(rng);
        int j = agent_dist(rng);
        
        while (i == j) { j = agent_dist(rng); } // Evitar que interactúe consigo mismo

        // Modelo RAE Clásico: Juntan su capital y lo reparten al azar
        double pool = employees[i].corporate_capital + employees[j].corporate_capital;
        double share = fraction_dist(rng);

        employees[i].corporate_capital = pool * share;
        employees[j].corporate_capital = pool * (1.0 - share);
    }

    void run(int iterations) {
        for (int i = 0; i < iterations; ++i) {
            tick();
        }
    }

    void export_to_csv(const std::string& filename) {
        std::ofstream file(filename);
        file << "employee_id,department_id,corporate_capital\n";
        for (const auto& emp : employees) {
            file << emp.id << "," << emp.department_id << "," << emp.corporate_capital << "\n";
        }
        file.close();
    }
};

int main() {
    int NUM_EMPLOYEES = 10000;
    int INITIAL_CAPITAL = 100;
    int ITERATIONS = 10000000; // 10 Millones de interacciones

    std::cout << "🚀 Iniciando Simulación RAE HR...\n";
    std::cout << "Agentes: " << NUM_EMPLOYEES << " | Iteraciones: " << ITERATIONS << "\n";

    auto start_time = std::chrono::high_resolution_clock::now();

    RAESimulation sim(NUM_EMPLOYEES, INITIAL_CAPITAL);
    sim.run(ITERATIONS);

    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff = end_time - start_time;

    std::cout << "✅ Simulación completada en: " << diff.count() << " segundos.\n";
    
    std::string output_file = "simulation_results.csv";
    sim.export_to_csv(output_file);
    std::cout << "📊 Resultados exportados a " << output_file << "\n";

    return 0;
}
